from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    friends = models.ManyToManyField("self", symmetrical=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    private_profile = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username