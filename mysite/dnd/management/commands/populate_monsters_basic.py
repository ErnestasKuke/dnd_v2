from django.core.management.base import BaseCommand
from dnd.models import Monster
from dnd.extra import calculate_bonus
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

            # Gather speed data
            speed = {}
            for key in monster["speed"].keys():
                speed[key] = monster["speed"][key]

            # Gather ability scores and add ability bonus
            ability_scores = {
                "strength": {
                    "value": monster['strength'],
                    "bonus": 5
                },
                "dexterity": {
                    "value": monster['dexterity'],
                    "bonus": 5
                },
                "constitution": {
                    "value": monster['constitution'],
                    "bonus": 5
                },
                "intelligence": {
                    "value": monster['intelligence'],
                    "bonus": 5
                },
                "wisdom": {
                    "value": monster['wisdom'],
                    "bonus": 5
                },
                "charisma": {
                    "value": monster['charisma'],
                    "bonus": 5
                },
            }
            for score in ability_scores.keys():
                ability_scores[score]["bonus"] = calculate_bonus(ability_scores[score]["value"])

            # Gather skill data
            skills = {}
            for key in monster["skills"].keys():
                skills[key] = monster["skills"][key]

            senses = monster['senses']
            languages = monster['languages']
            challenge_rating = monster['challenge_rating']

            # Gather actions and transform them to fit the JSON format
            actions = {}
            for action in monster["actions"]:
                actions[action["name"]] = {}
                for key in action.keys():
                    if key != "name":
                        actions[action["name"]][key] = action[key]

            legendary_desc = monster['legendary_desc']

            # Gather legendary actions and transform them to fit JSON format
            legendary_action = {}
            for action in monster["legendary_actions"]:
                legendary_action[action["name"]] = action["desc"]

            # Gather special abilities and transform them to fit JSON format
            special_abilities = {}
            for ability in monster["special_abilities"]:
                special_abilities[ability["name"]] = ability["desc"]

            monster = Monster(
                name=name,
                size=size,
                type=monster_type,
                alignment=alignment,
                armor_class=armor_class,
                hit_points=hit_points,
                speed=speed,
                ability_scores=ability_scores,
                skills=skills,
                senses=senses,
                languages=languages,
                challenge_rating=challenge_rating,
                actions=actions,
                legendary_desc=legendary_desc,
                legendary_actions=legendary_action,
                special_abilities=special_abilities,
                book_source="Basic rules"
            )
            monster.save()

    def handle(self, *args, **options):
        self._create_monsters()
