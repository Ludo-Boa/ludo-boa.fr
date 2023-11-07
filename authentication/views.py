from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from  django.contrib import messages


def logout_user(request):
    
    logout(request)
    return redirect('login')


def login_user(request):
    message = ""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirection vers une page de réussite.
            return redirect("movie-list")
        else:
            # Renvoie un message d'erreur « Connexion invalide 
            message = "Connexion invalide"
            return render(request, "authentication/login.html", {'message': message})     
    else:
        return render(request, "authentication/login.html", {})


# def logout_user(request):
#     logout(request)
#     return redirect("login")
    

