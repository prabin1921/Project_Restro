# Generated by Django 5.0.2 on 2024-03-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restro_App', '0004_category_foodmenu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='items',
            new_name='items_category',
        ),
        migrations.AddField(
            model_name='foodmenu',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodmenu',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='foodmenu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]