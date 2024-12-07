from django.urls import path, re_path

from apps.home import views

urlpatterns = [
    # The home page
    path("", views.index, name="home"),
    path("process", views.process, name="process"),
    path("product", views.product, name="product"),
    # Matches any html file
    re_path(r"^.*\.*", views.pages, name="pages"),
]
