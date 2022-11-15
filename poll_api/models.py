import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from poll_api.authentication.custom_user_manager import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    polls = models.ManyToManyField('Poll', through='Participant', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Poll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.fields.CharField(max_length=100)
    description = models.fields.TextField(null=True)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, through='Participant', blank=True)


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    pseudo = models.fields.CharField(max_length=100, null=True)


class Choice(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.TextField(null=True)
    link = models.URLField(max_length=250, null=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='choices')


class Vote(models.Model):
    is_pos = models.fields.BooleanField()
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='votes')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='votes')
