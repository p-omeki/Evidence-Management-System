# Generated by Django 5.0.2 on 2024-02-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_management_app', '0006_alter_case_case_outcome_alter_case_case_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reporter',
            options={'verbose_name': 'Reporter', 'verbose_name_plural': 'Reporters'},
        ),
        migrations.RenameField(
            model_name='evidence',
            old_name='is_analyzed',
            new_name='is_analysed',
        ),
        migrations.AlterField(
            model_name='evidence',
            name='is_collected',
            field=models.BooleanField(default=True),
        ),
    ]