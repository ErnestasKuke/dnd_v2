# Generated by Django 4.1.5 on 2023-01-31 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0012_monster_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monster',
            old_name='user',
            new_name='player',
        ),
    ]