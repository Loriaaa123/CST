from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post


@login_required(login_url="users:login")
def dashboard(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect("users:dashboard")
        # TODO max length of form does not working
    return render(request, "users/dashboard.html", {"form": form})


@login_required(login_url="users:login")
def post_detail(request, id):
    post = Post.objects.get(id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect("users:post_detail", id=id)
    return render(request, "users/post_detail.html", {"post": post, "form": form})
