from django.db import models

# Create your models here.

from django.db import models
from django.db import migrations
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from .extra import get_first_img


# Create your models here.
class Skills(models.Model):
    name = models.CharField('Name', max_length=200)
    desc = models.TextField('Description', max_length=1000)

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class AbilityScores(models.Model):
    name = models.CharField('Name', max_length=200)
    full_name = models.CharField('Full Name', max_length=200)
    desc = models.TextField('Description', max_length=2000)
    skills = models.ManyToManyField(Skills, help_text='Choose the skills that need this ability score')

    def __str__(self): return self.full_name

    class Meta:
        verbose_name = 'Ability Score'
        verbose_name_plural = 'Ability Scores'


class Alignments(models.Model):
    name = models.CharField('Name', max_length=200)
    abbreviation = models.CharField('Abbreviation', max_length=200)
    desc = models.TextField('Description', max_length=2000)

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'Alignment'
        verbose_name_plural = 'Alignments'


# Link with races
class Languages(models.Model):
    name = models.CharField('Name', max_length=200)
    type = models.CharField('Type', max_length=200)
    script = models.CharField('Script', max_length=200)
    desc = models.TextField('Description', max_length=2000, null=True, blank=True)

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class RaceTraits(models.Model):
    name = models.CharField('Name', max_length=200, help_text='Trait name', null=True, blank=True)
    description = models.TextField('Trait Description', max_length=2000, null=True, blank=True)
    level = models.IntegerField('level', default=0, null=True, blank=True)

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'RaceTrait'
        verbose_name_plural = 'RaceTraits'


class Subrace(models.Model):
    name = models.CharField('Name', max_length=200, help_text='Subrace name', null=False)
    description = HTMLField('Subrace description', max_length=3000, help_text='Subrace description', null=True,
                            blank=True)
    ability_scores = models.JSONField(blank=True, null=True)
    other_traits = models.ManyToManyField(RaceTraits)

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'Subrace'
        verbose_name_plural = 'Subraces'


class Race(models.Model):
    name = models.CharField('Name', max_length=200, help_text='Race name', null=False)
    description = HTMLField('Race description', max_length=10000, help_text='Race description', null=True)
    speed = models.IntegerField('Base speed')
    size = models.CharField('Size', max_length=200, help_text='Usual size of the race')
    languages = models.ManyToManyField(Languages, help_text='Languages that this race knows')
    subrace = models.ManyToManyField(Subrace, blank=True)
    ability_scores = models.JSONField(blank=True, null=True, default=dict)
    other_traits = models.ManyToManyField(RaceTraits)

    @property
    def img_url(self):
        url = get_first_img(self.name)
        return url

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'Race'
        verbose_name_plural = 'Races'


class Character(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('Name', max_length=200, help_text='Characters name', null=True)
    last_name = models.CharField('Last Name', max_length=200, help_text='Characters last name', null=True)
    personality = models.TextField('Personality', max_length=3000, help_text='Characters personality', null=True)
    appearance = models.TextField('Appearance', max_length=3000, help_text='Characters appearance', null=True)
    backstory = models.TextField('Backstory', max_length=3000, help_text='Characters backstory', null=True)

    # Needs to be added as a choice
    alignment = models.ForeignKey('Alignments', on_delete=models.SET_NULL, null=True, blank=True)

    race = models.ForeignKey('Race', on_delete=models.SET_NULL, null=True)
    subrace = models.ForeignKey('Subrace', on_delete=models.SET_NULL, null=True, )
    ability_scores = models.JSONField(blank=True, null=True, default=dict)

    # # char_class = models.ForeignKey('')

    def __str__(self): return f'{self.name} {self.last_name}'

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'


class Monster(models.Model):
    player = models.ManyToManyField(User)
    name = models.CharField('Name', max_length=200, help_text='Monsters name', null=True, blank=True)
    size = models.CharField('Size', max_length=200, help_text='Monsters size', null=True, blank=True)
    type = models.CharField('Type', max_length=200, help_text='Monsters type', null=True, blank=True)
    alignment = models.CharField('Alignment', max_length=200, help_text='Monsters type', null=True, blank=True)
    armor_class = models.IntegerField('Armor Class', help_text='Monsters Armor Class', null=True,
                                      blank=True)
    hit_points = models.IntegerField('Hit Points', help_text='Monsters Hit points', null=True,
                                     blank=True)
    speed = models.JSONField('Speed', null=True, blank=True)
    ability_scores = models.JSONField('Ability Scores', null=True, blank=True)
    skills = models.JSONField('Skills', null=True, blank=True)
    senses = models.CharField('Senses', max_length=200, help_text='Monsters senses', null=True, blank=True)
    languages = models.CharField('Languages', max_length=200, help_text='Monsters language', null=True, blank=True)
    challenge_rating = models.CharField('Challenge Rating', max_length=200, help_text='Monsters Challenge rating',
                                        null=True, blank=True)
    actions = models.JSONField('Actions', null=True, blank=True)
    reactions = models.JSONField('Reactions', null=True, blank=True)
    legendary_desc = models.TextField('Legendary Description', max_length=1000,
                                      help_text='Monsters Legendary Action Description', null=True, blank=True)
    legendary_actions = models.JSONField('Legendary Actions', null=True, blank=True)
    special_abilities = models.JSONField('Special Abilities', null=True, blank=True)
    book_source = models.CharField('Book Source', max_length=200, help_text='What book is this monster from', null=True,
                                   blank=True)

    @property
    def img_url(self):
        url = get_first_img(self.name)
        return url

    @property
    def get_usernames(self):
        usernames = []
        for user in self.player.all():
            usernames.append(user.username)
        return usernames

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'Monster'
        verbose_name_plural = 'Monsters'


class CharClass(models.Model):
    name = models.CharField('Name', max_length=200, help_text='Class name', null=False)
    description = HTMLField('Class description', max_length=3000, help_text='Class description', null=True)

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'


class Subclass(models.Model):
    name = models.CharField('Name', max_length=200, help_text='Class name', null=False)
    description = HTMLField('Class description', max_length=3000, help_text='Class description', null=True)

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'Subclass'
        verbose_name_plural = 'Subclasses'
