# Generated by Django 4.1.5 on 2023-01-31 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0009_alter_monster_legendary_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='challenge_rating',
            field=models.CharField(blank=True, help_text='Monsters Challenge rating', max_length=200, null=True, verbose_name='Challenge Rating'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='legendary_desc',
            field=models.TextField(blank=True, help_text='Monsters Legendary Action Description', max_length=1000, null=True, verbose_name='Legendary Description'),
        ),
    ]
