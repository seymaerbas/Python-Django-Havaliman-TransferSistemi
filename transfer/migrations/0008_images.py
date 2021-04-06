# Generated by Django 3.1.7 on 2021-03-30 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0007_delete_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.transfer')),
            ],
        ),
    ]