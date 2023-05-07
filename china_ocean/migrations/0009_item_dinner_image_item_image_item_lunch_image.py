# Generated by Django 4.1.3 on 2023-05-07 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("china_ocean", "0008_item_combo_lunch_number_item_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="dinner_image",
            field=models.ImageField(blank=True, null=True, upload_to="dinner-special/"),
        ),
        migrations.AddField(
            model_name="item",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="item",
            name="lunch_image",
            field=models.ImageField(blank=True, null=True, upload_to="lunch/"),
        ),
    ]