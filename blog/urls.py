from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path("", BlogListView.as_view(), name="postlist"),
    path('<int:pid>', bb),
]
