from django.urls import path
from .views import home, post_create, PostDetailView


urlpatterns = [
    path('', home, name='home'),
    path('create/', post_create, name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail')
]