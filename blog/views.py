from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,  DetailView
from .models import *
from django.utils import timezone
# Create your views here.

class BlogListView(ListView):
    context_object_name = "posts"
    paginate_by = 6
    def get_queryset(self):
        posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
        return posts



class BlogDetailView(DetailView):
    template_name = "blog/blog-details.html"
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now(),
            status=1
        ).prefetch_related('blocks')
    
    def get_object(self):
        post_id = self.kwargs.get('pk')
        post = get_object_or_404(Post, id=post_id)

          
        if post:
            post.counted_views += 1
            post.save()
        return post
    
        

    

def blog_category(request, cat_name):
     posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
     posts = posts.filter(category__name=cat_name)
     context = {'posts': posts}
     return render(request, "blog/post_list.html",context)

def blog_search(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if request.method == "GET":
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, "blog/post_list.html",context)


