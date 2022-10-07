from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    polls = models.ManyToManyField('Poll', through='Participant', blank=True)


class Poll(models.Model):
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
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='choices')


class Vote(models.Model):
    is_pos = models.fields.BooleanField()
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='votes')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='votes')
