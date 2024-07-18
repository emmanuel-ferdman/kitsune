# Generated by Django 4.2.14 on 2024-07-18 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0012_auto_20240701_0307"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="topics",
                to="products.product",
            ),
        ),
    ]
