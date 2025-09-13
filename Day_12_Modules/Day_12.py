##Day12: MODULES

##LEVEL 1
#Exercice1: random_user_id
#fonction qui génère un id user aléatoire de 6 caractères

import random
import string
def random_user_id():
    chars  = string.ascii_letters + string.digits #lettres maj/min" + chiffres
    return ''.join(random.choice(chars) for _ in range(6)) #choisir aléatoirement 6 caractères

print(random_user_id())

##Exercice2: ecrivons une fonction qui demande deux entrée à l'user: longueur et nombre des 
#id à générer


def user_id_gen_by_user():
    length = int(input("Entrez la longueur de l'ID : "))
    count = int(input("Entrez le nombre d'IDs à générer : "))
    chars = string.ascii_letters + string.digits
    ids = []
    for _ in range(count):
        new_id = ''.join(random.choice(chars) for _ in range(length))
        ids.append(new_id)
    return ids

##Exercice3: fonction qui génére une couleurRGB au hasard

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

##LEVEL 2

##Exercice1: fonction retournant une liste de couleurs hexadécimales

def list_of_hexa_colors(n):
    hex_colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        hex_colors.append(color)
    return hex_colors

print(list_of_hexa_colors(3))  

##Exercice2: fonction retournant une liste de couleurs rgb
def list_of_rgb_colors(n):
    rgb_colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f"rgb({r},{g},{b})")
    return rgb_colors

print(list_of_rgb_colors(3))

##Exercice3: fonction qui génére soit color rgb ou hexadécimal

def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Type invalide. Choisissez 'hexa' ou 'rgb'."

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))

##LEVEL 3

##Exercice1: fonction qui mélange aléatoirement une liste

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

print(shuffle_list([1,2,3,4,5]))


##Exercice2: unique_random_numbers

def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())  # Exemple : [3, 7, 1, 9, 0, 4, 6]
