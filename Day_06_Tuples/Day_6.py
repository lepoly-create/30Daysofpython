#"EXERCICES SUR LES TUPLES

##EXO1
##N1 : tupl vide 
empty_tuple = ()
print(empty_tuple)

##N2 : tuple contenant les noms de tes soeurs et frères 
sisters = ('Anna', 'Elsa')
brothers = ('John', 'Michael', 'David')
print("sisters: ", sisters)
print("brothers: ", brothers)

##N3 : combiner les tuples sisters et brothers et assigner à siblings
siblings = sisters + brothers
print("siblings: ", siblings)

##N4 : nombre de frères et sœurs
print("Nombre de frères et sœurs: ", len(siblings))

##N5: modifions le tuple siblings et ajoutons le nom de nos parents
family_members = siblings + ('Mary', 'Robert')
print("family_members: ", family_members)


##EXO2
##N1: décompréssé siblings et parents à partie de family_members
#supoosons que les 2 dernières entrées de family_members sont les parents
*siblings, mother, father = family_members
print("siblings: ", siblings)
print("mother: ", mother)
print("father: ", father)

##N2: créons 3 tuples nommés fruits, vegetables et animal_products

fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'yogurt')

food_stuff_tp = fruits + vegetables + animal_products
print("food_stuff_tp: ", food_stuff_tp)

##N3: transformons le tuple food_stuff_tp en une liste food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
print("food_stuff_lt: ", food_stuff_lt)

##N4: décupe l'élément ou les éléménts du milieu cdu tuple ou de la liste

n = len(food_stuff_tp)
if n%2 == 0:
    middle_elements_tp = food_stuff_tp[n//2 - 1:n//2 + 1]
else:
    middle_elements_tp = food_stuff_tp[n//2]
print("Middle element(s) of tuple: ", middle_elements_tp)

##N5: décupe les 3 premiers et les 3 derniers éléments du tuple ou de la liste
first_three_tp = food_stuff_tp[:3]
last_three_tp = food_stuff_tp[-3:]
print("First three elements of tuple: ", first_three_tp)
print("Last three elements of tuple: ", last_three_tp)

##N6: supprime le tuple food_stuff_tp
del food_stuff_tp

##N7: vérifie si un element existe dans un tuple

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("Is Estonia a nordic country?", "Estonia" in nordic_countries)
print("Is Finland a nordic country?", "Finland" in nordic_countries)