# Generated by Django 3.1.3 on 2020-11-15 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_customuser_name_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name_test',
        ),
    ]
