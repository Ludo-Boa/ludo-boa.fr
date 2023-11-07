from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from cinema.models import Movie, Genre


# @login_required est ajouté à URL
class MovieListView(ListView):
    model = Movie 
    context_object_name = 'movie_list' 
    template_name = "cinema/movie_list.html"
    paginate_by = 18

    def get_context_data(self, **kwargs) -> dict[str]:
        # Appelez d'abord l'implémentation de base pour obtenir le contexte
        context = super(MovieListView, self).get_context_data(**kwargs)
        # Créez n'importe quelle donnée et ajoutez-la au contexte
        
        return context


# @login_required est ajouté à URL
class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movie_detail' 
    template_name = "cinema/movie_detail.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        return context
    

class GenreListView(ListView):
    model = Genre
    context_object_name = "genre_list"
    
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        
        return context