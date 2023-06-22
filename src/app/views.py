from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Genre, Anime, Genres, Utility

class FirstIndexView(generic.TemplateView):
    template_name = 'index.html'

class IndexView(generic.ListView):
    model = Anime
    template_name = 'list.html'
    context_object_name = 'anime_list'
    paginate_by = 50
    def get_queryset(self):
        word = self.request.GET.get('word')
        if word:
            anime_list = Anime.objects.filter(
                title__icontains=word)
        else:
            anime_list = Anime.objects.all()
            
        return anime_list
        #return Anime.objects.all()

class GenreView(generic.ListView):
    template_name = 'list_genre.html'
    context_object_name = 'genre_list'
    paginate_by = 2
    def get_queryset(self):
        return Anime.objects.all()
    
class DetailView(generic.DetailView):
    model = Anime
    template_name = 'detail.html'