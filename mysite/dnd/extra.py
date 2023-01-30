import requests
from bs4 import BeautifulSoup
import os


# Turns ability scores in to the bonuses that they add
def calculate_bonus(number):
    bonus = 0
    if number == 1:
        bonus = -5
    elif number == 2 or number == 3:
        bonus = -4
    elif number == 4 or number == 5:
        bonus = -3
    elif number == 6 or number == 7:
        bonus = -2
    elif number == 8 or number == 9:
        bonus = -1
    elif number == 10 or number == 11:
        bonus = 0
    elif number == 12 or number == 13:
        bonus = 1
    elif number == 14 or number == 15:
        bonus = 2
    elif number == 16 or number == 17:
        bonus = 3
    elif number == 18 or number == 19:
        bonus = 4
    elif number == 20 or number == 21:
        bonus = 5
    elif number == 22 or number == 23:
        bonus = 6
    elif number == 24 or number == 25:
        bonus = 7
    elif number == 26 or number == 27:
        bonus = 8
    elif number == 28 or number == 29:
        bonus = 9
    elif number == 30:
        bonus = 10
    return bonus


# Gets the url of the first image on google img search
def get_first_img(name):
    search = 'dnd' + '+' + name
    url = "https://www.google.com/search?q=" + search + "&sxsrf=AJOqlzXgKKv_ete7_OUpdTStiq5cvWzyRw:1675077915766&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi_ro_Bl-_8AhWQuYsKHQqtDNsQ_AUoAXoECAEQAw&biw=1920&bih=929&dpr=1"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    image = images[1]['src']
    return image
