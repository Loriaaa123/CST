from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Post anything you want ...",
                "class": "textarea is-success is-medium",
            },
        ),
        label="",
    )

    class Meta:
        model = Post
        exclude = ("user",)


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Add a comment ...",
                "class": "input is-medium",
            },
        ),
        label="",
    )

    class Meta:
        model = Comment
        exclude = ("user", "post")
