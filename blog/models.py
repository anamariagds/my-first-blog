from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)#def texto cm limite de caracteres
    text = models.TextField()#texto sem limite
    created_date = models.DateTimeField(default=timezone.now)#data e hora
    published_date = models.DateTimeField(blank=True, null=True)#link para outro modelo

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
