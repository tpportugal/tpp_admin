from django.db import models

from api.apps.gtfs.agencies.models import Agency


def timetable_file_path(instance, filename):
    return 'maps/{0}/{1}'.format(instance.agency.slug, filename)


class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    map_name = models.CharField(max_length=200)
    map_data = models.FileField(upload_to=timetable_file_path, verbose_name="Ficheiro")
    # Training Data
    agency = models.ForeignKey(Agency, models.DO_NOTHING)
