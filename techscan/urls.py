from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from crudbuilder import urls
from home.api import TechnologyResource, RepositoryResource, AuthorResource
from home import views

technology_resource = TechnologyResource()
repository_resource = RepositoryResource()
author_resource = AuthorResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^djangojs/', include('djangojs.urls')),
    url(r'^crud/',  include(urls)),
    url(r'^api/', include(technology_resource.urls)),
    url(r'^api/', include(repository_resource.urls)),
    url(r'^api/', include(author_resource.urls)),
    url(r'^repo/(?P<search>.*)/?',views.RepositoriesView.as_view(), name='repositories'),
    url(r'^author/(?P<username>.*)/?',views.AuthorView.as_view(), name='author'),
    url(r'^$', TemplateView.as_view(template_name='home/technologies.html'), name='home'),
]
