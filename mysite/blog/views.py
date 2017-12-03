from .models import Post
from django.shortcuts import render, get_object_or_404


def post_list(request):
    post = Post.published.all()
    return render(request, 'blog/post/list.html', {'post': post})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=Post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {{'post': post}})
