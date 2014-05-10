from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from manozodynas.models import *
from django.views.generic import CreateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy

class WordList(ListView):
    model = Word
    paginate_by = 3
    success_url = 'index/'
    def get_context_data(self, **kwargs):
        context = super(WordList, self).get_context_data(**kwargs)
        return context

class WordCreate(CreateView):
    model = Word
    template_name = 'manozodynas/word.html'
    success_url = '/words'

class WordDelete(DeleteView):
    model = Word
    success_url = '/words'


def index_view(request):
    print "main page"
    return render(request, 'manozodynas/index.html', {})
