# Generated by Django 2.2.7 on 2019-12-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='adv1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='places',
            name='adv2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='places',
            name='adv3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='places',
            name='adv4',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='places',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='places',
            name='per',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='places',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]