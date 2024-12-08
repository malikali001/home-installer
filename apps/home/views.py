# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from apps.base.models import CustomUser, Query


def index(request):

    # if not request.user.image:
    #     current_user = CustomUser.objects.get(email=request.user.email)
    #     social_acc = current_user.socialaccount_set.first()
    #     if social_acc:
    #         current_user.image = social_acc.get_avatar_url()
    #         current_user.save()

    context = {"segment": "index"}

    html_template = loader.get_template("home/index.html")
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split("/")[-1]

        if load_template == "admin":
            return HttpResponseRedirect(reverse("admin:index"))
        context["segment"] = load_template

        html_template = loader.get_template("home/" + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template("home/page-404.html")
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template("home/page-500.html")
        return HttpResponse(html_template.render(context, request))


def process(request):

    context = {"segment": "index"}

    html_template = loader.get_template("home/page-about-c.html")
    return HttpResponse(html_template.render(context, request))


def product(request):

    context = {"segment": "index"}

    html_template = loader.get_template("home/page-blog-post-c.html")
    return HttpResponse(html_template.render(context, request))


def about(request):

    context = {"segment": "index"}

    html_template = loader.get_template("home/about.html")
    return HttpResponse(html_template.render(context, request))


def home(request):

    context = {"segment": "index"}

    html_template = loader.get_template("home/home.html")
    return HttpResponse(html_template.render(context, request))


def contact(request):

    if request.method == "POST":
        import pdb

        pdb.set_trace()
        data = {key: value for key, value in request.POST.items()}
        data["interested_in"] = request.POST.getlist("interested_in")
        if data.get("password") != data.get("confirm_password"):
            raise ValidationError("Passwords do not match")
        new_user = CustomUser(
            email=data.get("email"),
            name=data.get("name"),
            surname=data.get("surname"),
            phone=data.get("phone"),
            address=data.get("address"),
        )
        new_user.set_password(data.get("password"))
        new_user.save()
        query = Query(
            message=data.get("message"),
            address=data.get("address"),
            tiles_type=data.get("tiles_type"),
            electricity_consumption=data.get("electricity_consumption"),
            building_height=data.get("building_height"),
            available_surface_for_pv=data.get("available_surface"),
            orientation=data.get("orientation"),
            interested_in=data.get("interested_in"),
            user=new_user,
        )
        query.save()
    context = {"segment": "index"}

    html_template = loader.get_template("home/page-contact-c.html")
    return HttpResponse(html_template.render(context, request))
