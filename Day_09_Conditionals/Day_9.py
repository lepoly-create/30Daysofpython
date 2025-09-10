##Exercice - JOUR 9: Condition
#Level 1

##N1: Get user input using input("Enter your age:")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive")
else:
    years_left = 18-age
    print(f"You need {years_left} more years to learn to drive")

##N2: compare my_age and your_age
my_age = 19
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print(f"You are {diff} year older than me.")
    else:
        print(f"You are {diff} years older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    if diff == 1:
        print(f"I am {diff} year older than you.")
    else:
        print(f"I am {diff} years older than you.")
else:
    print("We are the same age.")

##N3: demande deux nombre à l_user et comparons ensuite
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


##Level2
##N1:
score = int(input("Enter your score: "))

if 80 <= score <= 100:
    grade = "A"
elif 70 <= score <= 79:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
elif 0 <= score <= 49:
    grade = "F"
else:
    grade = "Invalid score"

print("\nYour grade is:", grade)


##N2: Demandonc un mois et ffichons la saison correspondent
month = input("Enter the month: ").capitalize()

if month in ["September", "October", "November"]:
    print("The season is Autumn")
elif month in ["December", "January", "February"]:
    print("The season is Winter")
elif month in ["March", "April", "May"]:
    print("The season is Spring")
elif month in ["June", "July", "August"]:
    print("The season is Summer")
else:
    print("\nInvalid month")

##N3: vérifions si un fruit existe et sinon ajoutons le
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print("\nModified list:", fruits)


##Level3

##concerne aussi les dictionnaires de donnée

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

##N1: vérifions si le dict contient la clé 'skills'

if 'skills' in person:
    print("Skills:", person['skills'])
else:
    print("\nNo 'skills' key found")

##N2: Vérifions si 'python' est présent dans la liste des compétences

if 'Python' in person['skills']:
    print("The person has Python skill")
else:
    print("\nThe person does not have Python skill")


##N3: Trouvons et affichons la compétence du milieu dans la listes des compétences

skills = person['skills']
middle_index = len(skills) // 2   # division entière
print("\nMiddle skill:", skills[middle_index])

##N4: verifions si la liste des compétences est axactement ..
if person['skills'] == ['JavaScript', 'React']:
    print("The person has only JavaScript and React")
else:
    print("\nThe person has more or different skills")

##N5:
if person['skills'] == ['JavaScript', 'React']:
    print("\nThe person has only JavaScript and React")
else:
    print("\nThe person has more or different skills")

##N6:
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
