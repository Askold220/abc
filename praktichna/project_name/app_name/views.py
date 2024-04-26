from django.shortcuts import render, redirect
from .models import Author, Post, Comment

def add_comment_view(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        text = request.POST.get('text', '')
        comment = Comment.objects.create(text=text, post=post)
        author = post.author
        author.refresh_from_db()  
        comment_count = Comment.objects.filter(post__author=author).count()
        long_comment_count = sum(1 for comment in Comment.objects.filter(post__author=author) if len(comment.text) >= 5)
        return redirect('stats')
    else:
        pass

def stats_view(request):
    author = Author.objects.first()

    if author:
        post_count = author.posts.count()
        comment_count = Comment.objects.filter(post__author=author).count()
        long_comment_count = sum(1 for comment in Comment.objects.filter(post__author=author) if len(comment.text) >= 5)
        posts = Post.objects.filter(author=author)
        long_post_count = sum(1 for comment in Comment.objects.filter(post__author=author) if len(comment.post.content) >= 5)
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
        'long_post_count': long_post_count,
        'posts': posts,
    }
    return render(request, 'author.html', context)

