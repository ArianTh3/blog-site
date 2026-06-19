from django.shortcuts import render
from django.http import request
# Create your views here.
def index_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def contact_view(reqquset):
    return render(request, "contact.html")