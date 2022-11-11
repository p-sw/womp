from django.db import models

# Create your models here.


class WompCounter(models.Model):
    womp_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.womp_count)
