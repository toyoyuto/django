# Generated by Django 3.1.3 on 2020-11-15 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201115_0218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='custom_user',
        ),
    ]
