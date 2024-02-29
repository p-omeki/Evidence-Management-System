from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Officer, OfficerRank
from django.contrib.auth import authenticate, login
from .forms import OfficerRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from user_app.decorators import guest_required, itofficer_required

# Added recently from this point
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


@itofficer_required
def register_user(request):
    officer = request.user

    if request.method != "POST":
        form = OfficerRegistrationForm()
    else:
        form = OfficerRegistrationForm(data=request.POST)
        if form.is_valid():
            new_officer = form.save(commit=False)
            form.save()
            messages.success(
                request,
                f"Officer {new_officer.get_full_name()} ({new_officer.get_officer_rank_display()}), Badge ID {new_officer.username},  has been added to the system",
            )
            return redirect("user_app:home")
        else:
            messages.error(request, "Error creating officer")

    return render(request, "user_app/register.html", {"form": form})


@guest_required
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            officer = authenticate(request, username=username, password=password)

            if officer is not None:
                login(request, officer)
                messages.success(request, f"Welcome back, {username}")
                return redirect("home")

        messages.error(request, "Invalid username or password")

    context = {"section": "login"}
    template_name = "user_app/login.html"
    return render(request, template_name, context)


def homepage(request):
    if request.method == "POST":
        username = request.POST.get("badgenumber")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(
                "user_app:home"
            )  # Redirect to the home page after successful login

    return render(request, "home.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("user_app:login")


@itofficer_required
def officer_list(request):
    officers = Officer.objects.all()

    context = {"officers": officers}
    template_name = "user_app/officer_list.html"
    return render(request, template_name, context)


@itofficer_required
def delete_officer(request, badge_number):
    officer = Officer.objects.get(username=badge_number)
    officer.delete()
    messages.success(
        request, f"You have successfully deleted the officer account for {badge_number}"
    )
    return redirect("user_app:officer_list")


@itofficer_required
def update_officer(request, badge_number):
    try:
        officer = Officer.objects.get(username=badge_number)
    except Officer.DoesNotExist:
        messages.error(request, "Officer account does not exist")
        return redirect("user_app:officer_list")

    if request.method != "POST":
        form = OfficerRegistrationForm(instance=officer)
    else:
        form = OfficerRegistrationForm(instance=officer, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Officer account has been updated")
            return redirect("user_app:officer_list")
        else:
            messages.error(request, "Error updating officer account")

    context = {"officer": officer, "form": form}
    template_name = "user_app/update_officer.html"
    return render(request, template_name, context)
