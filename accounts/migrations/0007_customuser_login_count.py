# Generated by Django 3.1.3 on 2020-11-15 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='login_count',
            field=models.IntegerField(default=0, verbose_name='ログイン回数'),
        ),
    ]
