# Generated by Django 3.1.2 on 2020-12-07 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobserver", "0041_remove_job_started"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="needed_by",
        ),
    ]
