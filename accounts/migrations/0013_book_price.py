# Generated by Django 3.1.3 on 2020-11-22 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='値段'),
        ),
    ]
