# Generated by Django 3.1.13 on 2021-08-28 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0079_stream_description_nl"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partner",
            name="new_tags",
            field=models.JSONField(
                blank=True,
                default=None,
                help_text="Tag must be a valid JSON schema. Tag should be in the form of TagName_tag.",
                null=True,
            ),
        ),
    ]
