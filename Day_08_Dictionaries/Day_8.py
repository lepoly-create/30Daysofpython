# person = {'first_name': 'Asabeneh', 'last_name': 'Yetayeh', 'age': 250, 'country': 'Finland', 'is_marred': True,
#           'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }, 'job_title': 'Instructor'}
# person['skills'].append('HTML')
# print(person)

##EXERCICE9/DICTIOONAIRES

##N1 créons un dictionnaire vide appélé dog
dog = {}
print(dog)

##N2 : ajoutons name,color,breed, legs,age au dictionnaire dog
dog['name']='Josue'
dog['color']='yellow'
dog['breed']='yorkshire'
dog['legs']=4
dog['age']=19
print(dog)

##N3: créeons un dictionnaire student avec plusieurs clés
student = {
  'firstname': 'josue',
  'lastname': 'komlan',
  'gender': 'male',
  'age': '19',
  'marital status': 'single',
  'skills': ['HTML', 'CSS', 'JavaScript', 'Python'],
  'country': 'Togo',
  'city': 'Lome',
  'address': {
    'street': 'dakoté',
    'zipcode': '210'
  }
}
print("\nstudent:", student)

##N4: obtenons la longueur du dictionnaire
print("\nla longueur du dictionnaire student est:", len(student))
print("\n")
##N5: obtenons la valeur de skills et vérifions sont type
skills = student['skills']  #skills contient une liste
print("Skills:", skills)
print("Type of skills:", type(skills))
print("\n")
##N6 : modifions skills en ajoutant 1 ou 2 compétences
student['skills'].append('CSS')
student['skills'].append('JavaScript') #append ajoute un nouvel élément à une liste

print(student["skills"])
print("\n")
##N7: obtenons les clés du dictionnaire sous forme de liste
print(list(student.keys()))
print("\n")
##N8: obtenons les valeurs du dictionnaire sous forme de liste
print(list(student.values()))
print("\n")
##N9: convertis le dictionnaire en liste de tuples grâce à items()
print(list(student.items())) #chaque élément devient un tuple(clé, valeur)
print("\n")
##N10: supprimons un élément du dictionnaire
student.pop("address")
print("\n")
print(student)


##N11: supprimons complétement  un dictionnaire
del dog
