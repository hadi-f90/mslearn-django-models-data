from django.db import models


class Product(models.Model):
    name = models.TextField()
    price = models.DecimalField()
    creation_date = models.DateField()


class Category(models.Model):
    name = models.TextField()
