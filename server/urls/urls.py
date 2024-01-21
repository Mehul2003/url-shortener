from django.urls import re_path
from urls import views

urlpatterns = [
    re_path(r'^path$', views.pathApi),
    re_path(r'path/$', views.pathApi),
]