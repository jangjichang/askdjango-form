from django.db import models
from django.core.validators import MinLengthValidator
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.pk])

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    ip = models.CharField(max_length=15)

    def __str__(self):
        return "{}: {}".format(self.author, self.message)

class GameUser(models.Model):
    server = models.CharField(max_length=10)
    username = models.CharField(max_length=20, validators=[MinLengthValidator(3)])

    class Meata:
        unique_together = [
            ('server', 'username'),
        ]
