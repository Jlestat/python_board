from django.urls import path
from .views import home, post_create


urlpatterns = [
    path('', home, name='home'),
    path('create/', post_create, name='post_create'),
]