from django.db import models


class Msg(models.Model):
    sender = models.CharField(max_length=250, default='')
    text = models.TextField(default='')
    date = models.DateTimeField(auto_now=True)
