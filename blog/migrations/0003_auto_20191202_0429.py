# Generated by Django 2.2.7 on 2019-12-02 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_places'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='places',
            name='random',
            field=models.TextField(default='40'),
        ),
        migrations.AddField(
            model_name='places',
            name='seats',
            field=models.IntegerField(default=30),
        ),
    ]
