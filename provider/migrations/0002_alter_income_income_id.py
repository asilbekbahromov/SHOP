# Generated by Django 4.2.1 on 2023-05-11 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("provider", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="income",
            name="income_id",
            field=models.CharField(
                default="#71d6f06f-5a92-4b9a-9fa9-ce12694ff245",
                max_length=255,
                verbose_name="Maxsulot id raqami",
            ),
        ),
    ]