from tastypie.resources import ModelResource
from home.models import Technology,Repository,Author
from tastypie.paginator import Paginator
from tastypie.resources import ModelResource, ALL
from tastypie.fields import ListField
from django.db.models import Q
from tastypie import fields
import logging

logger = logging.getLogger(__name__)

class TechnologyResource(ModelResource):
    class Meta:
        queryset = Technology.objects.all()
        ordering = {
            'name': ALL,
            'repo_count': ALL
        }
        resource_name = 'technology'
        filtering = {
            'name': ALL,
        }
        paginator_class = Paginator

class AuthorResource(ModelResource):
    class Meta:
        queryset = Author.objects.all()
        ordering = {
            'name': ALL,
            'stars': ALL,
            'following': ALL,
            'followers': ALL
        }
        resource_name = 'author'
        filtering = {
            'name': ALL,
            'desc': ALL,
            'username': ALL
        }
        paginator_class = Paginator

class RepositoryResource(ModelResource):
    author = fields.ForeignKey(AuthorResource, attribute='author', full=True)

    def __init__(self, *args, **kwargs):
        super(RepositoryResource, self).__init__(*args, **kwargs)
        self.q_filters = []

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
        orm_filters = super(RepositoryResource, self).build_filters(filters)

        if('query' in filters):
            query = filters['query']
            qset = (
                    Q(technology__contains=query) |
                    Q(tags__contains=query)
                    )
            orm_filters.update({'custom': qset})
        return orm_filters

    def apply_filters(self, request, applicable_filters):
        if 'custom' in applicable_filters:
            custom = applicable_filters.pop('custom')
        else:
            custom = None

        semi_filtered = super(RepositoryResource, self).apply_filters(request, applicable_filters)

        return semi_filtered.filter(custom) if custom else semi_filtered

    class Meta:
        queryset = Repository.objects.select_related('author')
        ordering = {
            'name': ALL,
            'stars': ALL,
            'forks': ALL
        }
        resource_name = 'repository'
        filtering = {
            'name': ALL,
            'author': ALL,
            'technology': ALL,
            'tags': ALL
        }
        paginator_class = Paginator
