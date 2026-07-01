from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path("", BlogListView.as_view(), name="postlist"),
    #path('<int:pid>', bb),
    path("<int:pk>/", BlogDetailView.as_view(), name="postdetail"),
    path('category/<str:cat_name>', blog_category, name='category'),
     path("search/", blog_search, name='search'),
]
