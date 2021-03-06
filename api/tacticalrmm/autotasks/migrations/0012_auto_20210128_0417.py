# Generated by Django 3.1.4 on 2021-01-28 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autotasks', '0011_automatedtask_alert_severity'),
    ]

    operations = [
        migrations.AddField(
            model_name='automatedtask',
            name='email_alert',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='automatedtask',
            name='email_sent',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='automatedtask',
            name='text_alert',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='automatedtask',
            name='text_sent',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
