from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from django.utils import timezone
# Create your views here.

class BlogListView(ListView):
    context_object_name = "posts"
    paginate_by = 6
    def get_queryset(self):
        posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
        return posts



def bb(request):
    return render(request, "blog-details.html")