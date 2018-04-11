# Generated by Django 2.0.2 on 2018-03-24 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0002_presentation'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='ساعت پایان'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='ساعت شروع'),
        ),
    ]
