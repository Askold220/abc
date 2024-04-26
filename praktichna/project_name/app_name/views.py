from django.shortcuts import render
from .models import Author, Post, Comment

def stats_view(request):
    author = Author.objects.first()

    if author:
        post_count = author.posts.count()
        comment_count = Comment.objects.filter(post__author=author).count()
        long_comment_count = sum(1 for comment in Comment.objects.filter(post__author=author) if len(comment.text) >= 5)
        posts = Post.objects.filter(author=author)
    else:
        post_count = 0
        comment_count = 0
        long_comment_count = 0
        posts = []

    context = {
        'author': author,
        'post_count': post_count,
        'comment_count': comment_count,
        'long_comment_count': long_comment_count,
        'posts': posts,
    }
    return render(request, 'author.html', context)
