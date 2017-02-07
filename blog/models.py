from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    text = models.TextField()
    cdate = models.DateTimeField(default=timezone.now)
    pdate = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.pdate = timezone.now()
        self.save()

        def __str__(self):
            return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    cdate = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
