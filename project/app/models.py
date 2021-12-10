from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_paragraph = models.TextField()

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

