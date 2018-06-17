from django.db import models


class Song(models.Model):
    date_created = models.DateField(default="00000000")
    position = models.IntegerField(default='0', null=True, blank=True)
    position_change = models.IntegerField(default='0', null=True, blank=True)
    artist = models.TextField(max_length=200, default='null', null=True, blank=True)
    title = models.TextField(max_length=200, default='null', null=True, blank=True)
    spins = models.IntegerField(default='0', null=True, blank=True)
    spins_change = models.IntegerField(default='0', null=True, blank=True)
    bullet = models.IntegerField(default='0', null=True, blank=True)
    bullet_change = models.IntegerField(default='0', null=True, blank=True)
    audience = models.DecimalField(max_digits=10, decimal_places=3, default='0', null=True, blank=True)
    audience_change = models.DecimalField(max_digits=10, decimal_places=3, default='0', null=True, blank=True)
    days = models.IntegerField(default='0', null=True, blank=True)
    peak = models.IntegerField(default='0', null=True, blank=True)

    class Meta:
        unique_together = ["date_created", "title"]

    def __unicode__(self):
        return self.title
