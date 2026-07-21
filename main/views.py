from django.shortcuts import render
from django.http import request
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView , UpdateView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Contact
from .urls import *

# Create your views here.
def index_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("main:index_view")
    template_name = "contact.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ContactView, self).form_valid(form)