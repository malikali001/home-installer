from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render

from apps import Utils
from core.settings import GITHUB_AUTH, TWITTER_AUTH

from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(
        request,
        "accounts/login.html",
        {
            "form": form,
            "msg": msg,
            "github_login": GITHUB_AUTH,
            "twitter_login": TWITTER_AUTH,
        },
    )


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=raw_password)

            msg = "User created successfully."
            success = True

            # return redirect("/login/")

        else:
            msg = "Form is not valid"
    else:
        form = SignUpForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form, "msg": msg, "success": success},
    )


def delete_account(request, **kwargs):
    result, message = Utils.delete_user(request.user.email)
    if not result:
        return JsonResponse({"errors": message}, status=400)
    logout(request)
    return HttpResponseRedirect("/")


def change_password(request, **kwargs):
    form = SetPasswordForm(user=request.user, data=request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        message = "Password successfully changed."
        status = 200
    else:
        message = form.errors
        status = 400
    return JsonResponse({"message": message}, status=status)
