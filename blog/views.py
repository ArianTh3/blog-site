from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,  DetailView
from .models import *
from django.utils import timezone
from django.db.models import F
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.contrib import messages

# Create your views here.

class BlogListView(ListView):
    context_object_name = "posts"
    paginate_by = 6
    def get_queryset(self):
        posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).select_related('author__profile')
        return posts




class BlogDetailView(FormMixin, DetailView):
    model = Post
    template_name = "blog/blog-details.html"
    context_object_name = "post"
    form_class = CommentForm

    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now(),
            status=1,
        ).select_related('author__profile').prefetch_related("blocks")

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        post = get_object_or_404(queryset, pk=self.kwargs.get("pk"))
        Post.objects.filter(pk=post.pk).update(counted_views=F("counted_views") + 1)
        post.refresh_from_db(fields=["counted_views"])
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(
            posts=self.object,
            approved=True,
        ).order_by("-created_date")
        context["form"] = context.get("form") or self.get_form()
        return context

    def get_success_url(self):
        return reverse("blog:postdetail", kwargs={"pk": self.object.pk})

    # --- handle POST (form submission) ---
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # DetailView normally only sets this on GET
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.posts = self.object
        comment.approved = False
        comment.save()

        messages.success(self.request, "Your comment has been submitted")

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was a problem with your comment.")
        return super().form_invalid(form)
        

    

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


