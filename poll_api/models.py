from django.utils import timezone

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from poll_api.authentication.custom_user_manager import CustomUserManager


class User(AbstractUser):
    """
    User model (extends Django user)
    """
    email = models.EmailField(max_length=255, unique=True)
    polls = models.ManyToManyField('Poll', through='Participant', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Poll(models.Model):
    """
    Poll model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.fields.CharField(max_length=100)
    description = models.fields.TextField(null=True)

    start_date = models.fields.DateField(null=True)
    end_date = models.fields.DateField(null=True)
    closing_time = models.fields.DateTimeField(null=True)

    created_by = models.ForeignKey(
        User, related_name='created_by', on_delete=models.CASCADE)
    participants = models.ManyToManyField(
        User, through='Participant', blank=True)


class Participant(models.Model):
    """
    Participant model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    pseudo = models.fields.CharField(max_length=100, null=True)


class Choice(models.Model):
    """
    Choice model
    """
    class Currency(models.TextChoices):
        EU = 'eu'
        USD = 'usd'

    name = models.fields.CharField(max_length=100)
    description = models.fields.TextField(null=True)
    link = models.URLField(max_length=250, null=True)
    price = models.fields.FloatField(default=0)
    currency = models.CharField(
        choices=Currency.choices, default=Currency.EU, max_length=3)
    creation_time = models.fields.DateTimeField(default=timezone.now)
    participant = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name='choices')


class Vote(models.Model):
    """
    Vote model
    """
    is_pos = models.fields.BooleanField()
    participant = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name='votes')
    choice = models.ForeignKey(
        Choice, on_delete=models.CASCADE, related_name='votes')
