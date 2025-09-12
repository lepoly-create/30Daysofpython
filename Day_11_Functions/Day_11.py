# def find_even_numbers(n): 
#     evens = [] 
#     for i in range(n + 1):
#         if i % 2 == 0: 
#             evens.append(i) 
#     return evens 
# print(find_even_numbers(10))
# print("\n")
# def greetings (name = 'Peter'):
#     message = name + ', welcome to Python for Everyone!'
#     return message
# print(greetings())
# print(greetings('Asabeneh'))
# print("\n")

# def square_number (n): return n * n 
# def do_something(f, x): return f(x) 
# print(do_something(square_number, 3))


##DAY_11
#Level1

##N1: add_two_numbers

def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(3, 7))  # 10

##N2: area_of_circle
import math

def area_of_circle(r):
    return math.pi * r * r

print(area_of_circle(5))  

##N3: add_all_nums

def add_all_nums(*args):
    total = 0
    for i in args:
        if not isinstance(i, (int, float)):
            return "All arguments must be numbers"
        total += i
    return total

print(add_all_nums(2, 3, 5))     
print(add_all_nums(2, "a", 5))   

##N4: covert celcius to fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(convert_celsius_to_fahrenheit(0))
print(convert_celsius_to_fahrenheit(100))
print("\n")

##N5: check season

def check_season(month):
    month= month.lower()
    
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Invalid month'
print(check_season('April'))

##N6: calculate_slope/ retourn la pente d'une équation linéaire

def calculate_pente(x1, y1, x2, y2):
    if x2 - x1 ==0:
        return "Slope is undefined (vertical line)"
    return (y2 - y1) / (x2 - x1)
print(calculate_pente(2, 3, 4, 7))
print("\n")
##N7: solve_quadratic_eqn (ax² + bx + c = 0)
import math

def solve_quadratic_eqn(a, b, c):
    d = b**2 - 4*a*c  # discriminant
    if d < 0:
        return "No real solution"
    elif d == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return (x1, x2)

print(solve_quadratic_eqn(1, -3, 2))  

##N8: print_list / déclarer une fonction qui affiche tous les élements d'une liste

def print_list(lst):
    for item in lst:
        print(item)

print_list([1, 2, 3, 4, 5])

##N9: déclarons une fonction qui inverse une liste
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print(reverse_list([1, 2, 3, 4, 5]))
print("\n")

##N10: fonction qui met tous les élements d'une liste en majuscule

def capitalize_list_items(lst):
    return [str(item).capitalize() for item in lst]

print(capitalize_list_items(['apple', 'banana', 'cherry']))
print("\n")
##N11: ajoutons un élément à une liste

def add_item(lst, item):
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
print("\n")

##N12: remove_item
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

##N13: sum_of_numbers

def somme_de_nombre(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

print(somme_de_nombre(5))   
print(somme_de_nombre(10))  
##N14: somme detous les nombres imapirs jusqu'à n
def sum_of_odds(n):
    total = 0
    for i in range(n+1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(10))  # 25
print("\n")

##N15: des pairs alors

def sum_of_even(n):
    total = 0
    for i in range(n+1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(10))  # 30
print("\n")


##Level2
 
 ##Exercice1: la fonction prendra en paramêtre un positif et comptera combien de pair 
 #et d'impair de 0 à n pour n ce nombre positif
 
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 ==0 :
            evens += 1
        else:
            odds += 1
    return f'The number of evens are {evens}. The number of odds are {odds}.'
print(evens_and_odds(100))
print("\n")

##Exercice2: factoriel d'un nombre

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))   
print(factorial(0))   

 ##Exercice3: is_empty
 
def is_empty(param):
    if not param:
        return True
    return False

print(is_empty([]))      # True
print(is_empty(""))      # True
print(is_empty([1, 2]))  # False

##Exercice 4: Fonctons statiques

from collections import Counter
import math

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    data_sorted = sorted(data)
    n = len(data_sorted)
    mid = n // 2
    if n % 2 == 0:
        return (data_sorted[mid - 1] + data_sorted[mid]) / 2
    else:
        return data_sorted[mid]

def calculate_mode(data):
    count = Counter(data)
    max_freq = max(count.values())
    modes = [k for k, v in count.items() if v == max_freq]
    return modes

def calculate_range(data):
    return max(data) - min(data)

def calculate_variance(data):
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_std(data):
    return math.sqrt(calculate_variance(data))

# ✅ Exemple d’utilisation
dataset = [2, 4, 4, 4, 5, 5, 7, 9]

print("Mean:", calculate_mean(dataset))     
print("Median:", calculate_median(dataset))  
print("Mode:", calculate_mode(dataset))      
print("Range:", calculate_range(dataset))    
print("Variance:", calculate_variance(dataset))  
print("Std:", calculate_std(dataset))        


#Level3

#Exercice1: prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # tester jusqu'à racine carrée de n
        if n % i == 0:
            return False
    return True

print(is_prime(7))   
print(is_prime(10))  

##Exercice2: is_uniquz
def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1, 2, 3, 4]))   
print(all_unique([1, 2, 2, 3]))   

##Exercice3: 
def same_type(lst):
    return all(isinstance(x, type(lst[0])) for x in lst)

print(same_type([1, 2, 3]))          
print(same_type([1, "hello", 3]))    

#Exercice4: 
def is_valid_variable(var):
    import keyword
    return var.isidentifier() and not keyword.iskeyword(var)

print(is_valid_variable("age"))    
print(is_valid_variable("1age"))    
print(is_valid_variable("for"))     

#Exercice5: analyse de doonnées
countries_data = [
    {"country": "China", "population": 1402112000, "languages": ["Chinese"]},
    {"country": "India", "population": 1380004000, "languages": ["Hindi", "English"]},
    {"country": "USA", "population": 331000000, "languages": ["English"]},
    {"country": "Nigeria", "population": 206000000, "languages": ["English"]},
]

from collections import Counter

def most_spoken_languages(data, top_n=10):
    all_langs = []
    for country in data:
        all_langs.extend(country["languages"])  # ajoute toutes les langues
    lang_count = Counter(all_langs)  # compte la fréquence
    return lang_count.most_common(top_n)

print(most_spoken_languages(countries_data, 3))

def most_populated_countries(data, top_n=10):
    sorted_countries = sorted(data, key=lambda x: x["population"], reverse=True)
    return sorted_countries[:top_n]

print(most_populated_countries(countries_data, 3))


