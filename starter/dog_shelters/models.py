from unicodedata import category
from django.db import models


# DEFAULT_AUTO_FIELD = models.BigAutoField()
class Shelter(models.Model):
    Shelter_id = models.AutoField(auto_created=True,
                                  primary_key=True,
                                  db_column='Shelter_id')
    shelter_name = models.CharField(max_length=200,
                                    primary_key=models.AutoField)
    location = models.CharField(max_length=200)
    default_auto_field = models.BigAutoField

    def __str__(self):
        return self.name


class Dog(models.Model):
    shelter = models.ForeignKey(Shelter,
                                db_column='Shelter_id',
                                to_field='shelter_name',
                                on_delete=models.PROTECT,
                                primary_key=models.BigAutoField)

    name = models.CharField(max_length=200)
    description = models.TextField()
    intake_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


"""
class Product(models.Model):
    name = models.TextField(max_length=50,
                            unique=True
                            # primary_key=DEFAULT_AUTO_FIELD
                            )

    price = models.DecimalField(max_digits=6,
                                decimal_places=3)
    creation_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey('Category',  # name the model
                                 on_delete=models.PROTECT)


class Category(models.Model):
    name = models.TextField(max_length=50,
                            unique=True
                            # primary_key=DEFAULT_AUTO_FIELD
                            ) """
