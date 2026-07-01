from django import template
from blog.models import Post
from blog.models import Category
from blog.models import Comment


register = template.Library() 

@register.inclusion_tag("blog/latest.html")
def latestpost():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {"posts":posts}


@register.inclusion_tag("blog/category.html")
def categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()

    return {"categories":cat_dict}


@register.inclusion_tag("mostwatched.html")
def mostwatched():
    posts = Post.objects.filter(status=1).order_by('counted_views')[:5]
    return {"posts":posts}
    
@register.inclusion_tag("index_latest.html")
def index_latestpost():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    return {"posts":posts}