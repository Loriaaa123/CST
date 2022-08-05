from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="post", on_delete=models.CASCADE)
    body = models.TextField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (
            f"{self.user}"
            f"  -created: {self.created_at:%Y-%m-%d %H:%M}"
            f"  -body: {self.body[:30]}"
        )

    class Meta:
        ordering = ("created_at",)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE, null=True
    )
    body = models.TextField(max_length=350, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (
            f"{self.post.user}"
            f"  -created: {self.created_at:%Y-%m-%d %H:%M}"
            f"  -body: {self.body[:30]}"
        )
