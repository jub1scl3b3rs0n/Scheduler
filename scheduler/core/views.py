from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ServiceProvider

def index(request):
    return render(request, "core/index.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        is_provider = request.POST.get("is_provider") == "on"

        if password != confirm:
            return render(request, "core/register.html", {
                "error": "As senhas não coincidem."
            })

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            if is_provider:
                ServiceProvider.objects.create(user=user)
        except:
            return render(request, "core/register.html", {
                "error": "Erro ao criar usuário."
            })

        login(request, user)
        return redirect("dashboard")

    return render(request, "core/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "core/login.html", {
                "error": "Usuário ou senha inválidos."
            })

    return render(request, "core/login.html")

def logout_view(request):
    logout(request)
    return redirect("index")

@login_required
def dashboard(request):
    try:
        request.user.serviceprovider  # tenta acessar o prestador
        return render(request, "core/dashboard_provider.html")
    except ServiceProvider.DoesNotExist:
        return render(request, "core/dashboard_client.html")
