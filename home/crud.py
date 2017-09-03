from crudbuilder.abstract import BaseCrudBuilder
from home.models import Technology,Repository,Author

class TechnologyCrud(BaseCrudBuilder):
        model = Technology
        search_fields = ['name']
        tables2_fields = ('name', 'repo_count')
        tables2_css_class = "table table-bordered table-condensed"
        tables2_pagination = 15  # default is 10
        modelform_excludes = ['created_by', 'updated_by']
        login_required=False
        permission_required=False
        # permissions = {
        #   'list': 'example.person_list',
        #       'create': 'example.person_create'
        # }

class AuthorCrud(BaseCrudBuilder):
        model = Author
        search_fields = ['name']
        tables2_fields = ('name', 'desc')
        tables2_css_class = "table table-bordered table-condensed"
        tables2_pagination = 15  # default is 10
        modelform_excludes = ['created_by', 'updated_by']
        login_required=False
        permission_required=False

class RepositoryCrud(BaseCrudBuilder):
        model = Repository
        search_fields = ['name']
        tables2_fields = ('name', 'desc')
        tables2_css_class = "table table-bordered table-condensed"
        tables2_pagination = 15  # default is 10
        modelform_excludes = ['created_by', 'updated_by']
        login_required=False
        permission_required=False
