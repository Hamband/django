from datetime import datetime

from django.shortcuts import render

from blog.models import BlogPost


def home_page(request):
    posts = BlogPost.objects.filter(published_at__lte=datetime.now())[:10]
    return render(request, 'blog/home.html', {
        'posts': posts
    })
