from django.db import models
from inst.models import Installation


class Log(models.Model):
    LogContent = models.CharField(max_length=254, null=False)
    LogDate = models.DateField(null=False, auto_now=True)
    Installation = models.ForeignKey(
        Installation, to_field='id', null=False, on_delete=models.DO_NOTHING)
