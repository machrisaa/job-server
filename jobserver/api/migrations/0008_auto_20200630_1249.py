# Generated by Django 3.0.7 on 2020-06-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_job_status_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='callback_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
