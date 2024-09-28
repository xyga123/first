from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

def newshome(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/newshome.html', {'news':news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/newsdetail.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model= Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model= Articles
    success_url = '/news/'
    template_name = 'news/newsdelete.html'

def create(request):
    error=''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newshome')
        else:
            error = "Форма заполнена неверно"

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)