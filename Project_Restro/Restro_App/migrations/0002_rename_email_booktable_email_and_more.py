# Generated by Django 4.2.7 on 2024-02-19 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Restro_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booktable',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='booktable',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='booktable',
            old_name='number',
            new_name='No_Pople',
        ),
        migrations.RenameField(
            model_name='booktable',
            old_name='specialRequest',
            new_name='SpecialRequest',
        ),
        migrations.RemoveField(
            model_name='booktable',
            name='dateTime',
        ),
        migrations.RemoveField(
            model_name='booktable',
            name='people',
        ),
        migrations.AddField(
            model_name='booktable',
            name='Ph_Number',
            field=models.CharField(default=django.utils.timezone.now, max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booktable',
            name='DateTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
