# Generated by Django 5.0 on 2024-05-13 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="status",
            field=models.CharField(
                choices=[
                    ("#00FF00", "#00FF00"),
                    ("#FFFF00", "#FFFF00"),
                    ("#FF0000", "#FF0000"),
                    ("#A52A2A", "#A52A2A"),
                    ("#000000", "#000000"),
                ],
                default="#00FF00",
                max_length=10,
            ),
        ),
    ]
