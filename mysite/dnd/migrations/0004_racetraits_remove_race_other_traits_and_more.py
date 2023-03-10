# Generated by Django 4.1.5 on 2023-01-29 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0003_charclass_description_race_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaceTraits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Trait name', max_length=200, verbose_name='Name')),
                ('description', models.CharField(max_length=2000, verbose_name='Trait Description')),
                ('level', models.IntegerField(verbose_name='level')),
            ],
            options={
                'verbose_name': 'RaceTrait',
                'verbose_name_plural': 'RaceTraits',
            },
        ),
        migrations.RemoveField(
            model_name='race',
            name='other_traits',
        ),
        migrations.AddField(
            model_name='race',
            name='other_traits',
            field=models.ManyToManyField(to='dnd.racetraits'),
        ),
    ]
