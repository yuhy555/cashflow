# Generated by Django 2.0.2 on 2018-09-06 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentmethod', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
