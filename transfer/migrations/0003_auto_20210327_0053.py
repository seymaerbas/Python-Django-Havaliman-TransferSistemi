# Generated by Django 3.1.7 on 2021-03-26 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0002_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]