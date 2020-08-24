from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Places(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    per = models.CharField(max_length=100)
    adv1 = models.CharField(max_length=100)
    adv2 = models.CharField(max_length=100)
    adv3 = models.CharField(max_length=100)
    adv4 = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})

class Book(models.Model):
    billno = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=200)
    phno = models.CharField(max_length=12)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    place = models.ForeignKey(Places, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('users-auth', kwargs={'pk' : self.pk})
