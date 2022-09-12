from django.db import models


class User(models.Model):
    name = models.fields.CharField(max_length=100)


class Poll(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.TextField(null=True)
    participants = models.ManyToManyField(User, through='Participant')


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    pseudo = models.fields.CharField(max_length=100, null=True)


class Choice(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.TextField(null=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)


class Vote(models.Model):
    is_pos = models.fields.BooleanField()
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
