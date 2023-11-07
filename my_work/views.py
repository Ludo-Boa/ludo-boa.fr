from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project, Category



class ProjectListView(ListView):
    model = Project
    context_object_name = 'portfolio_list' 
    template_name = "page/portfolio.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        # Appelez d'abord l'implémentation de base pour obtenir le contexte
        context = super(ProjectListView, self).get_context_data(**kwargs)
        # Créez n'importe quelle donnée et ajoutez-la au contexte
        context["categories_list"] = Category.objects.all()
        return context



class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'portfolio_detail' 
    template_name = "page/portfolio-detail.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        return context
    


def categories_list(request):
    categories_list = Category.objects.all()

    context = {
        "categories_list": categories_list,
    }

    return render(request, "page/portfolio.html", context)

