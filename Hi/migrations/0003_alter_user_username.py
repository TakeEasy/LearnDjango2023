# Generated by Django 4.2.5 on 2023-09-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hi', '0002_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, verbose_name='用户名'),
        ),
    ]
