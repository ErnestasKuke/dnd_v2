# Generated by Django 4.1.5 on 2023-01-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0006_remove_subrace_other_traits_subrace_other_traits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subrace',
            name='ability_scores',
            field=models.JSONField(blank=True, null=True),
        ),
    ]