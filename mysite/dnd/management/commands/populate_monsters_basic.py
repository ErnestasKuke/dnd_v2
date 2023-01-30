from django.core.management.base import BaseCommand
from dnd.models import Monster
import json
import requests


class Command(BaseCommand):
    help = 'Command to create dnd base monsters'

    def _create_monsters(self):
        url = "https://api.open5e.com/monsters/?challenge_rating=&armor_class=&type=&name=&document=&document__slug=wotc-srd"
        r = requests.get(url)
        monsters = json.loads(r.text)
        monsters = monsters['results']
        for monster in monsters:
            name = monster['name']
            size = monster['size']
            monster_type = monster['type']
            alignment = monster['alignment']
            armor_class = monster['armor_class']
            hit_points = monster['hit_points']
            speed = json.dumps(monster['speed'])
            ability_scores = {
                "strength": monster['strength'],
                "dexterity": monster['dexterity'],
                "constitution": monster['constitution'],
                "intelligence": monster['intelligence'],
                "wisdom": monster['wisdom'],
                "charisma": monster['charisma']
            }
            x = 'filler'
            monster = Monster(
                name=name,
                size=size,
                type=monster_type,
                alignment=alignment,
                armor_class=armor_class,
                hit_points=hit_points,
                speed=speed,
                ability_scores=ability_scores,
                skills=x,
                senses=x,
                languages=x,
                challenge_rating=x,
                actions=x,
                reactions=x,
                legendary_desc=x,
                legendary_actions=x,
                special_abilities=x
            )
            monster.save()

    def handle(self, *args, **options):
        self._create_monsters()
