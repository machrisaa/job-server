# Generated by Django 3.1.2 on 2020-12-07 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobserver", "0049_rename_jobrequest_backend_to_backend_old"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobrequest",
            name="backend",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="job_requests",
                to="jobserver.backend",
            ),
        ),
    ]
