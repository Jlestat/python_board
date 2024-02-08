from django.shortcuts import render, redirect
from .models import Post
from django.utils.timezone import now
from .forms import PostForm


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts, 'year': now().year})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})
