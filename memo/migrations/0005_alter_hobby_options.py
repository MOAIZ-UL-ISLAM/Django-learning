# Generated by Django 4.2.4 on 2023-09-02 08:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("memo", "0004_profile_sect"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="hobby",
            options={"verbose_name_plural": "Hobbies"},
        ),
    ]
