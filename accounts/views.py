from django.shortcuts import render, redirect
from accounts.forms import LogInForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LogInForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            password_confirmation = form.cleaned_data["password_confirmation"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            if password_confirmation == password:
                user = User.objects.create_user(username, password=password)
                login(request, user)
                return redirect("home")
            else:
                raise ValueError("The Passwords Do not match")
    else:
        form = SignUpForm()
    context = {"form": form}
    return render(request, "registration/signup.html", context)
