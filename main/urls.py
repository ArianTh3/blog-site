from django.urls import path
from main.views import *
urlpatterns = [
    path("", index_view, name="index_view"),
    path("about/", about_view, name="about_view"),
    path("contact/", ContactView.as_view(), name="contact_view"),
]
