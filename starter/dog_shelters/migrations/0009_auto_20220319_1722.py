# Generated by Django 3.2.12 on 2022-03-19 17:22

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0008_alter_dog_shelter_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shelter',
            name='id',
        ),
        migrations.AlterField(
            model_name='shelter',
            name='name',
            field=models.CharField(max_length=200, primary_key=django.db.models.fields.AutoField, serialize=False),
        ),
    ]
