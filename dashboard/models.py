from django.db import models
from kworb.models import Song


class TopFiveRadio(models.Model):
    id = models.IntegerField(null=False, unique=True)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)

    class Meta:
        unique_together = ["id"]

    def __unicode__(self):
        return self.id + ": " + Song.title


class TopFiveSpotify(models.Model):
    id = models.IntegerField(null=False, unique=True)
    artist = models.TextField(max_length=200, default='null', null=True, blank=True)
    title = models.TextField(max_length=200, default='null', null=True, blank=True)
    plays = models.IntegerField(null=False)

    class Meta:
        unique_together = ["id"]

    def __unicode__(self):
        return self.title


class TopFiveSpins(models.Model):
    id = models.IntegerField(null=False, unique=True)
    song = models.ManyToManyField('Song')

    class Meta:
        unique_together = ["id"]

    def __unicode__(self):
        return self.id


class NewOnRadio(models.Model):
    id = models.IntegerField(null=False, unique=True)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)

    class Meta:
        unique_together = ["id"]

    def __unicode__(self):
        return self.id + ": " + Song.title


class FastestRisingOnRadio(models.Model):
    id = models.IntegerField(null=False, unique=True)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)

    class Meta:
        unique_together = ["id"]

    def __unicode__(self):
        return self.id + ": " + Song.title
