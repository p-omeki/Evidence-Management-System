# Generated by Django 5.0.1 on 2024-02-14 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case_management_app', '0003_rename_officer_case_case_officer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='description',
            new_name='case_description',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='title',
            new_name='case_title',
        ),
    ]
