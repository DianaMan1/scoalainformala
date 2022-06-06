from django.db import models


class FavCountry(models.Model):
    user_id = models.IntegerField()
    country_code = models.CharField(max_length=3)


class FavRegion(models.Model):
    user_id = models.IntegerField()
    country_code = models.CharField(max_length=3)
    iso_code = models.CharField(max_length=3)


class FavCity(models.Model):
    user_id = models.IntegerField()
    country_code = models.CharField(max_length=3)
    city_id = models.CharField(max_length=3)
