# Generated by Django 4.2.4 on 2023-08-30 19:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("receipts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="receipt",
            old_name="catagory",
            new_name="category",
        ),
    ]
