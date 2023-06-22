import datetime

from django.db import models


class Request(models.Model):
    endpoint = models.CharField(max_length=100, null=True)
    user = models.ForeignKey("authentication.User", on_delete=models.SET_NULL, null=True)
    response_date = models.DateTimeField(default=datetime.datetime.now())
    response_code = models.PositiveSmallIntegerField()
    method = models.CharField(max_length=10, null=True)
    remote_address = models.CharField(max_length=20, null=True)
    exec_time = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)
    body_response = models.TextField()
    body_request = models.TextField()
