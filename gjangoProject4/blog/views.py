from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post

def home(request):
    last_posts = Post.objects.all().order_by('-created_at')[:3] # Используем created_at
    return render(request, 'blog/home.html', {'last_posts': last_posts})

def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'posts': posts, 'paginator': paginator})