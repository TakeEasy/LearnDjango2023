# Generated by Django 4.2.5 on 2023-09-21 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hi', '0009_book_publish_date_publish_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='kucun',
            field=models.IntegerField(default=10000),
        ),
        migrations.AddField(
            model_name='book',
            name='maichu',
            field=models.IntegerField(default=0),
        ),
    ]
