# Generated by Django 3.2.12 on 2022-03-19 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='dog',
            name='adoption_date',
        ),
        migrations.AlterField(
            model_name='dog',
            name='description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.TextField(max_length=50, primary_key=models.BigAutoField(primary_key=True), serialize=False, unique=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dog_shelters.category')),
            ],
        ),
    ]
