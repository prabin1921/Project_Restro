# Generated by Django 4.2.7 on 2024-02-19 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restro_App', '0002_rename_email_booktable_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booktable',
            old_name='No_Pople',
            new_name='No_People',
        ),
    ]
