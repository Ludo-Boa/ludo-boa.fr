from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView

from my_profile.models import Social, KnowHow, TechnicalSkills, Interest
from my_work.models import Project, Category
from datetime import date


def index(request):
    social_list = Social.objects.all()
    context = {
        "social_list": social_list,
    }
    return render(request, "page/index.html", context)


def about(request):
    knowHow_list = KnowHow.objects.all()
    skills_list = TechnicalSkills.objects.all()
    interest_list = Interest.objects.all()
    nb_projects = Project.objects.count()

    date_start = date(2016,2,6)
    current_date = date.today()
    delta = current_date - date_start
    
    
    # Compte le nombre de jours depuis le 6/02/2016
    # Qui correspond à 1 tasse de café par jour
    coffe_cups = str(delta.days)

    # Calcule : nombre de ligne de code (moyenne) par projets 
    codeline_average = 5400
    codeline = codeline_average * nb_projects


    # Années d'expérience
    exp = str(delta.days / 365 -1)

    

    context = {
        "knowHow_list": knowHow_list,
        "skills_list": skills_list,
        "interest_list": interest_list,
        "coffe_cups": coffe_cups,
        "nb_projects": nb_projects,
        "codeline": codeline,
        "exp": exp,
    }
    return render(request, "page/about.html", context)


def resume(request):
    return render(request, "page/resume.html", {})


# def portfolio(request):
#     projects_list = Project.objects.all()
#     category_list = Category.objects.all()
    
#     context = {
#         "projects_list": projects_list,
#         "project_category_list": category_list,
#     }

#     return render(request, "page/portfolio.html", context)
    


def portfolio_detail(request, id):
    project_detail = get_object_or_404(Project, id=id)

    context = {
        'project_detail': project_detail,
    }

    return render(request, "page/portfolio.html", context)


def contact(request):
    social_list = Social.objects.all()
    context = {
            "social_list": social_list, 
    }

    if request.method == "POST":
        contact_name =request.POST["contact-name"]
        contact_email =request.POST["contact-email"]
        contact_subject =request.POST["contact-subject"]
        contact_message =request.POST["contact-message"]

        # send an email
        send_mail(
            subject = contact_subject, 
            message = contact_message, 
            from_email = contact_name + " / " + contact_email,
            recipient_list = ["hello@ludo-boa.fr"],
        )

        context = {
            "social_list": social_list, 
            "contact_name": contact_name, 
            "contact_email": contact_email,
            "contact_subject": contact_subject,
            "contact_message": contact_message,
        }

        return render(request, "page/contact.html", context)
    else:
        return render(request, "page/contact.html", context)