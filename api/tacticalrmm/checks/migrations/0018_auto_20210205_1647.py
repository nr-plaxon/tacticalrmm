# Generated by Django 3.1.4 on 2021-02-05 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0017_check_dashboard_alert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='alert_severity',
            field=models.CharField(blank=True, choices=[('info', 'Informational'), ('warning', 'Warning'), ('error', 'Error')], default='warning', max_length=15, null=True),
        ),
    ]
