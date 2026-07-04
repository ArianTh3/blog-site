from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django.contrib.auth import get_user_model



User = get_user_model()
  



class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category) 
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_required = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return static("assets/img/blog/blog-hero-2.webp")
    
    class Meta:
        ordering = ["-created_date"]
    
    def __str__(self):
        return self.title
    
class ContentBlock(models.Model):
    BLOCK_TYPES = [
        ('heading', 'Heading'),
        ('paragraph', 'Paragraph'),
        ('image', 'Image'),
        ('quote', 'Quote'),
        ('list', 'List'),
        ('code', 'Code Block'),
        ('card', 'Card'),
        ('table', 'Table'),
    ]

    post = models.ForeignKey(Post, related_name='blocks', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    block_type = models.CharField(max_length=20, choices=BLOCK_TYPES)

    content = models.TextField(blank=True)
    heading_level = models.PositiveSmallIntegerField(default=2)
    image = models.ImageField(upload_to='blog/blocks/', blank=True, null=True)
    image_caption = models.CharField(max_length=255, blank=True)
    code_language = models.CharField(max_length=30, blank=True)
    data = models.JSONField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.post.title} - {self.block_type} ({self.order})"

    

class Comment(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.TimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
    
    def __str__(self):
        return self.name    