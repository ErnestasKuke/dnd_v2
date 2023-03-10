from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.forms import User
from django.db.models import Q
import json
from .extra import calculate_bonus, monster_list_manipulation, paginate_lists, search_mlist
from .models import Character, Race, Subrace, Monster


# Create your views here.


##################################################
# ________________Race related views
##################################################
def race_list(request):
    races = Race.objects.all
    context = {
        "races": races
    }
    return render(request, 'race/race_list.html', context=context)


def race_detail(request, race_id):
    race = get_object_or_404(Race, pk=race_id)
    context = {
        "race": race
    }
    return render(request, 'race/race_detail.html', context=context)


##################################################
# ________________Character related views
##################################################
def character_list(request):
    char_list = Character.objects.filter(player=request.user)
    context = {
        'char_list': char_list,
    }
    return render(request, 'character/character_list.html', context=context)


def character_detail(request, character_id):
    single_character = get_object_or_404(Character, pk=character_id)
    return render(request, "character/character_detail.html", {"character": single_character})


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
                character_abilityscores[score]["value"] = character_abilityscores[score]["value"] + race.ability_scores[
                    score]
            except KeyError:
                pass
        for score in character_abilityscores.keys():
            try:
                character_abilityscores[score]["value"] = character_abilityscores[score]["value"] + \
                                                          subrace.ability_scores[score]
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
    return render(request, 'character/character_creator.html', context=context)


##################################################
# ________________Monster related views
##################################################
@csrf_protect
def monster_list(request):
    search_url = "monster-list-search"
    monsters_list = Monster.objects.all()
    # Ability to add or remove from my monster list
    monster_list_manipulation(request, Monster)
    return render(request, 'monster/monster_list.html', context=paginate_lists(request, monsters_list, search_url))


def monster_list_search(request):
    search_url = "monster-list-search"
    starting_list = Monster.objects.all()
    monsters_list = search_mlist(request, starting_list)
    # Ability to add or remove from my monster list
    monster_list_manipulation(request, Monster)
    return render(request, 'monster/monster_list.html', context=paginate_lists(request, monsters_list, search_url))


def monster_detail(request, monster_id):
    single_monster = get_object_or_404(Monster, pk=monster_id)
    return render(request, "monster/monster_detail.html", {"monster": single_monster})


@csrf_protect
def user_monster_list(request):
    search_url = "user-monster-list-search"
    monsters_list = Monster.objects.filter(player=request.user)
    # Ability to add or remove from my monster list
    monster_list_manipulation(request, Monster)
    return render(request, 'monster/monster_list.html', context=paginate_lists(request, monsters_list, search_url))


def user_monster_list_search(request):
    search_url = "user-monster-list-search"
    starting_list = Monster.objects.filter(player=request.user)
    monsters_list = search_mlist(request, starting_list)
    # Ability to add or remove from my monster list
    monster_list_manipulation(request, Monster)
    return render(request, 'monster/monster_list.html', context=paginate_lists(request, monsters_list, search_url))


##################################################
# ________________System views
##################################################
def home(request):
    return render(request, 'home.html')


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reik??mes i?? registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slapta??od??iai
        if password == password2:
            # tikriname, ar neu??imtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} u??imtas!')
                return redirect('register')
            else:
                # tikriname, ar n??ra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. pa??tu {email} jau u??registruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame nauj?? vartotoj??
                    User.objects.create_user(username=username, email=email,
                                             password=password)
                    return redirect('login')
        else:
            messages.error(request, 'Slapta??od??iai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')
