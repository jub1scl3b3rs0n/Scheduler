from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Appointment, ServiceProvider
from datetime import datetime, timedelta, time

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
        provider = request.user.serviceprovider
        appointments = provider.appointments.all().order_by("date", "time")
        return render(request, "core/dashboard_provider.html", {
            "appointments": appointments
        })
    except ServiceProvider.DoesNotExist:
        appointments = request.user.bookings.all().order_by("date", "time")
        return render(request, "core/dashboard_client.html", {
            "appointments": appointments
        })

def provider_list(request):
    providers = ServiceProvider.objects.all()
    return render(request, "core/provider_list.html", {
        "providers": providers
    })

def provider_detail(request, provider_id):
    provider = ServiceProvider.objects.get(pk=provider_id)

    # Gerar horários disponíveis dos próximos 7 dias
    today = datetime.today().date()
    available_slots = []

    for i in range(7):
        day = today + timedelta(days=i)
        weekday = day.strftime('%A').lower()  # ex: 'monday'
        hours = provider.available_days.get(weekday, [])

        for hour_str in hours:
            hour = datetime.strptime(hour_str, "%H:%M").time()
            # Verifica se o horário já está agendado
            if not Appointment.objects.filter(provider=provider, date=day, time=hour).exists():
                available_slots.append({
                    "date": day,
                    "time": hour
                })

    return render(request, "core/provider_detail.html", {
        "provider": provider,
        "available_slots": available_slots
    })

@login_required
def book_appointment(request, provider_id):
    if request.method == "POST":
        provider = ServiceProvider.objects.get(pk=provider_id)
        date = request.POST["date"]
        time_str = request.POST["time"]
        time_obj = datetime.strptime(time_str, "%H:%M").time()
        # time_obj = datetime.strptime(time_str, "%H:%M:%S").time() if ":" in time_str else datetime.strptime(time_str, "%H:%M").time()

        # Verificar se já existe agendamento no mesmo horário
        exists = Appointment.objects.filter(provider=provider, date=date, time=time_obj).exists()
        if not exists:
            Appointment.objects.create(
                provider=provider,
                client=request.user,
                date=date,
                time=time_obj,
                status="pending"
            )
        return redirect("dashboard")
    return redirect("index")
