"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static
from django.urls import path, include, re_path 
from django.views.generic import ListView

import authentication.views
import page.views
from cinema.views import MovieListView, MovieDetailView
from my_profile.views import ResumeView
from my_work.views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filer/', include('filer.urls')),
    path('tinymce/', include('tinymce.urls')),
    path("", page.views.index, name="home"),
    path("a-propos/", page.views.about, name="about"),
    path("cv/", ResumeView.as_view(), name="resume"),
    path("portfolio/", ProjectListView.as_view(), name="portfolio"),
    path("portfolio/<int:pk>/", ProjectDetailView.as_view(), name="portfolio-detail"),
    path("contact/", page.views.contact, name="contact"),
    path('login/', authentication.views.login_user, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path("cinema/", login_required(MovieListView.as_view()), name='movie-list'),
    path('movie/<slug:slug>/', login_required(MovieDetailView.as_view()), name="movie-detail"), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Ajoutez cette ligne pour servir le fichier robots.txt
from django.views.generic import TemplateView

urlpatterns += [
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]
