from typing import Any
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView, DetailView

from .models import Experience, KnowHow, TechnicalSkills, Education, Social

# Create your views here.


class ResumeView(ListView):
    model = Experience
    template_name = 'page/resume.html'
    context_object_name = "experience_list"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ResumeView, self).get_context_data(**kwargs)
        context.update({
            'know_how_list': KnowHow.objects.all(),
            'technical_skills_list': TechnicalSkills.objects.all(),
            'educations_list': Education.objects.all(),
        })
        return context
    

