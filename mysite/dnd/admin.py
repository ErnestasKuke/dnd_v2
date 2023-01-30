from django.contrib import admin
from .models import Character, Race, Subrace, Languages, RaceTraits, Monster
from django.db import models
from django_json_widget.widgets import JSONEditorWidget


# Register your models here.

class MonsterAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


class CharacterAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


class RaceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


class SubraceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


admin.site.register(Character, CharacterAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(Subrace, SubraceAdmin)
admin.site.register(Monster, MonsterAdmin)
admin.site.register(Languages)
admin.site.register(RaceTraits)
