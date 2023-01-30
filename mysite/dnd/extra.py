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