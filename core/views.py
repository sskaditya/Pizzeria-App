from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Category, MenuItem
from django.contrib import messages


def home(request):
    return render(request, "home.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def dashboard(request):
    categories = Category.objects.all()
    menu_items = MenuItem.objects.all()

    context = {
        "categories": categories,
        "menu_items": menu_items,
    }

    return render(request, "dashboard.html", context)


def menu(request):
    categories = Category.objects.all()

    context = {
        "categories": categories,
    }

    return render(request, "menu.html", context)
