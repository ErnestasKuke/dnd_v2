from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.forms import User
import json
from .extra import calculate_bonus
from .models import Character, Race, Subrace


# Create your views here.
def home(request):
    return render(request, 'home.html')


# Create your views here.

def character_list(request):
    char_list = Character.objects.filter(player=request.user)
    context = {
        'char_list': char_list,
    }
    return render(request, 'character_list.html', context=context)


def character_detail(request, character_id):
    single_character = get_object_or_404(Character, pk=character_id)
    subraces = Subrace.objects.filter(name__icontains=single_character.race.name)
    return render(request, "character_detail.html", {"character": single_character, "subraces": subraces})


@csrf_protect
def character_creation(request):
    race_choice = Race.objects.all
    race_subrace = {}
    for race in Race.objects.all():
        race_subrace[str(race.name)] = []
        for subrace in race.subrace.all():
            race_subrace[str(race.name)].append(subrace.name)
    race_subrace = json.dumps(race_subrace)

    if request.method == "POST":
        name = request.POST['name']
        last_name = request.POST['last-name']
        personality = request.POST['personality']
        appearance = request.POST['appearance']
        backstory = request.POST['backstory']
        race = Race.objects.get(name=request.POST['race'])
        subrace = Subrace.objects.get(name=request.POST['subrace'])

        # Character ability scores
        character_strength = int(request.POST['character-strength'])
        character_dexterity = int(request.POST['character-dexterity'])
        character_constitution = int(request.POST['character-constitution'])
        character_intelligence = int(request.POST['character-intelligence'])
        character_wisdom = int(request.POST['character-wisdom'])
        character_charisma = int(request.POST['character-charisma'])
        character_abilityscores = {
            "strength": {
                "value": character_strength,
            },
            "dexterity": {
                "value": character_dexterity,
            },
            "constitution": {
                "value": character_constitution,
            },
            "intelligence": {
                "value": character_intelligence,
            },
            "wisdom": {
                "value": character_wisdom,
            },
            "charisma": {
                "value": character_charisma,
            }
        }
        for score in character_abilityscores.keys():
            try:
                character_abilityscores[score]["value"] = character_abilityscores[score]["value"] + race.ability_scores[score]
            except KeyError:
                pass
        for score in character_abilityscores.keys():
            try:
                character_abilityscores[score]["value"] = character_abilityscores[score]["value"] + subrace.ability_scores[score]
            except KeyError:
                pass
        for score in character_abilityscores.keys():
            character_abilityscores[score]["bonus"] = calculate_bonus(character_abilityscores[score]["value"])

        Character.objects.create(
            player=request.user,
            name=name,
            last_name=last_name,
            personality=personality,
            appearance=appearance,
            backstory=backstory,
            race=race,
            subrace=subrace,
            ability_scores=character_abilityscores,
        )

        return redirect('character-list')

    context = {
        'race_choice': race_choice,
        'race_subrace': race_subrace
    }
    return render(request, 'character_creator.html', context=context)


def monster_list(request):
    return render(request, 'monster_list.html')


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email,
                                             password=password)
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')
