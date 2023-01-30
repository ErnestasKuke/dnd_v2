# Generated by Django 4.1.5 on 2023-01-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0004_racetraits_remove_race_other_traits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racetraits',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Trait Description'),
        ),
        migrations.AlterField(
            model_name='racetraits',
            name='level',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='level'),
        ),
        migrations.AlterField(
            model_name='racetraits',
            name='name',
            field=models.CharField(blank=True, help_text='Trait name', max_length=200, null=True, verbose_name='Name'),
        ),
    ]