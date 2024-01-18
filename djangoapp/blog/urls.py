from blog.views import index
from django.urls import path

# namespace
app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
]
