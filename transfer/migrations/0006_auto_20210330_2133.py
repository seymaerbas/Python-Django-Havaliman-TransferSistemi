# Generated by Django 3.1.7 on 2021-03-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0005_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]
