# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from apps.base.models import CustomUser


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

    html_template = loader.get_template("home/page-about.html")
    return HttpResponse(html_template.render(context, request))


def product(request):

    context = {"segment": "index"}

    html_template = loader.get_template("home/page-blog-post.html")
    return HttpResponse(html_template.render(context, request))
