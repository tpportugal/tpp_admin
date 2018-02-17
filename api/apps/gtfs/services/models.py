from django.db import models
from django.db.models import SmallIntegerField, DateField


class Service(models.Model):
    """
    Modelo para os serviços dos transportes públicos em Portugal

    Equivale ao services.txt num feed GTFS
    """

    monday = SmallIntegerField(default=0)
    tuesday = SmallIntegerField(default=0)
    wednesday = SmallIntegerField(default=0)
    thursday = SmallIntegerField(default=0)
    friday = SmallIntegerField(default=0)
    saturday = SmallIntegerField(default=0)
    sunday = SmallIntegerField(default=0)
    start_date = DateField()
    end_date = DateField()
