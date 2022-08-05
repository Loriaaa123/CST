from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PostForm, CommentForm
from .models import Post, Comment


@login_required(login_url="users:login")
def dashboard(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect("feed:dashboard")
        # TODO max length of form does not working
    return render(request, "feed/dashboard.html", {"form": form})


@login_required(login_url="users:login")
def post_detail(request, id):
    post = Post.objects.get(id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect("feed:post_detail", id=id)
    return render(request, "feed/post_detail.html", {"post": post, "form": form})


@login_required(login_url="users:login")
def update_post(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("feed:post_detail", id=id)
    return render(request, "feed/update_post.html", {"form": form, "post": post})


@login_required(login_url="users:login")
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if post.user == request.user:
        post.delete()
        messages.success(request, "Post deleted successfully")
        return redirect("feed:dashboard")
    else:
        messages.warning(request, "You can only delete your own posts")
        redirect("feed:post_detail", id=post.id)
    return redirect("feed:dashboard")


@login_required(login_url="users:login")
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    if comment.user == request.user:
        comment.delete()
        messages.success(request, "Comment deleted successfully")
    else:
        messages.warning(request, "You can only delete your own comments")
        return redirect("feed:post_detail", id=comment.post.id)
    return redirect("feed:dashboard")
