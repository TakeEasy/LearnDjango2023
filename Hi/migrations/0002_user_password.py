# Generated by Django 4.2.5 on 2023-09-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.IntegerField(null=True),
        ),
    ]
