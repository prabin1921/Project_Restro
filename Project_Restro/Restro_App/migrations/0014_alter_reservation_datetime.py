# Generated by Django 5.0.2 on 2024-03-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restro_App', '0013_table_remove_tableprice_table_no_reservation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]