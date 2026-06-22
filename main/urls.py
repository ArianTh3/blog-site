from django.urls import path
from main.views import *

app_name = 'main'


urlpatterns = [
    path("", index_view, name="indexview"),
    path("about/", about_view, name="about_view"),
    path("contact/", ContactView.as_view(), name="contact_view"),
]
