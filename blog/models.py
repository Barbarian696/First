from django.db import models
from django.utils import timezone


class Post(models.Model):
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length=100)
    text=models.TextField()
    cdate=models.DateTimeField(default=timezone.now)
    pdate=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.pdate=timezone.now()
        self.save()

        def __str__(self):
            return self.title
