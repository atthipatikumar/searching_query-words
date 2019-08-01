from django.db import models


class Details(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    state_id = models.IntegerField()

    class Meta:
      verbose_name_plural = "application"

    def __str__(self):
        return self.name