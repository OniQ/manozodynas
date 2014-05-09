from django.shortcuts import render
from django.views.generic.list import ListView
from manozodynas.models import *
from django.views.generic import CreateView

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
    success_url = 'zodziai/'

def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def words_view(request):
    words = Word.objects.all()
    return render(request, 'manozodynas/words.html', {'words': words})
