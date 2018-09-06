# Generated by Django 2.0.2 on 2018-09-06 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('street', models.CharField(blank=True, default='', max_length=200)),
                ('city', models.CharField(blank=True, default='', max_length=200)),
                ('province', models.CharField(blank=True, default='', max_length=200)),
                ('country', models.CharField(blank=True, default='', max_length=200)),
                ('postal_code', models.CharField(blank=True, default='', max_length=10)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
