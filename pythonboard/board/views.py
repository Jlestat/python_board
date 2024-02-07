from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils.timezone import now


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'base.html', {'posts': posts, 'year': now().year})

