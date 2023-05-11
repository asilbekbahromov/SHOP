# Generated by Django 4.2.1 on 2023-05-11 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0002_alter_category_parent_alter_product_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Income",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "income_id",
                    models.CharField(
                        default="#604df1f9-1794-4b0e-a696-6e223300acfe",
                        max_length=255,
                        verbose_name="Maxsulot id raqami",
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2, max_digits=17, verbose_name="Summa"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Provider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Yetkazib beruvchi"),
                ),
                (
                    "phone",
                    models.CharField(max_length=13, verbose_name="Telefon raqami"),
                ),
                (
                    "balance",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=17,
                        verbose_name="Yetkazib beruvchi balansi",
                    ),
                ),
                (
                    "info",
                    models.TextField(verbose_name="Yetkazib beruvchi haqida ma'lumot"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IncomeItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.SmallIntegerField(verbose_name="Soni")),
                (
                    "income",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="provider.income",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="product.product",
                        verbose_name="Maxsulot",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="income",
            name="provider",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="provider.provider",
                verbose_name="Yetkazib beruvchi",
            ),
        ),
    ]
