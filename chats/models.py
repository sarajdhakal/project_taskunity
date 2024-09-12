from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    user1 = models.CharField(max_length=100, default='', blank=True)
    user2 = models.CharField(max_length=100, default='', blank=True)
    friends = models.ManyToManyField(User, related_name='team_members', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

