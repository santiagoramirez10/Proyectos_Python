# Generated by Django 4.2.5 on 2023-09-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
