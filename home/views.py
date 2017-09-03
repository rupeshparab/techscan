from django.shortcuts import render  # noqa
from django.views import View
from home.models import Author, Repository
from django.http import HttpResponseNotFound
import logging

logger = logging.getLogger(__name__)
#from .forms import MyForm

# Create your views here.
class RepositoriesView(View):
    template_name = 'home/repositories.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'search': self.kwargs.get('search')})#, {'form': form})

class AuthorView(View):
    template_name = 'home/author.html'

    def get(self, request, *args, **kwargs):
        logger.error(self.kwargs.get('username'))
        user = None
        repos = []
        try:
            user = Author.objects.get(username=self.kwargs.get('username'))
        except Author.DoesNotExist as e:
            logger.error(e)
            return HttpResponseNotFound('<h1>User not found</h1>')

        if user is None:
            return HttpResponseNotFound('<h1>User not found</h1>')

        try:
            repos = Repository.objects.filter(author=user.id).all()
        except Author.DoesNotExist as e:
            logger.error(e)
        return render(request, self.template_name, {'user': user, 'repos': repos})
