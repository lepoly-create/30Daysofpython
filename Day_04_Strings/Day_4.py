##NN1

print('Thirty '+'Days '+'Of '+'Python ' )
##NN2
print( "'Coding "+"For "+"All'")
##NN3
company = "Coding For All"
print(company)
len_company = len(company)
print(len_company)
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

##NN9
print(company[1:14])#découpe le premier motde la chaine
##N10: vérifions si la chaine contient le mot "Coding"

print("Coding" in company)
print(company.index('Coding'))
##N11
print(company.replace("Coding", "Python"))
##N12

sentence = "Python for Everyone"
print(sentence.replace("Everyone", "All"))
##N13
print(company.split())

##N14 : Séparation avec virgule

techs = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(techs.split(", "))

##N15
print(company[0])
##N16
print(len(company) -1)
##N17

print(company[10])
##N18: accronyme pour "Python For Everyone"

phrase = "Python For Everyone"
acronym = "".join([word[0]
                   for word in phrase.split()
                   ])
print(acronym)

##N19 pour "Coding For All" aussi
phrase2= "Coding For All"
acronym2 = "".join([word[0] for word in phrase2.split()])
print(acronym2)

##N20
print(company.index("C"))
##N21
print(company.index("F"))

##N22 : trouver l'indice de la dernière occurennce de l dans la chaine avec rfind
print(company.rfind("l"))
##N23: Trouvons la premier occurence de 'because' dans la phrase

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

##N24: On utilise rindex pour trouver la dernière occurence de ce dernier
print(sentence.rindex("because"))
##25 : extrons because qui s'est répété 3 fois dans la phrase
print(sentence[31:54])

##N26 et 27 same for beginning
##N28: Vérifions si réellement "Coding For All" commence par "Coding"

print(company.startswith("Coding"))
##N29
print(company.endswith("coding"))
##N30: suppression des espace au début et à la fin de la chaine
chaine = " Coding For All "
print(chaine.strip())

##N31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

##N32

libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" #".join(libs))
##N33
print("I am enjoying this challenge.\nI just wonder what is next.")

##N34

print("Name\t\tAge\t\tCountry\t\tCity")
print("Asabenh\t\t250\t\tFinlande\tHelsinki")
##N35
rayon = 10
area = 3.14*rayon**2
print(f"The area of a circle with rayon {rayon} is {area} meters square")
print("The area of a circle with radius {} is {} meters square.".format(rayon, int(area)))

##N36
a, b = 8, 6

# Utilisation de f-strings
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  # .2f = 2 chiffres après la virgule
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")








