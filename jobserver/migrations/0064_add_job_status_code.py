# Generated by Django 3.1.2 on 2021-01-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobserver", "0063_add_workspace_will_notify"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="status_code",
            field=models.TextField(blank=True, default=""),
        ),
    ]
