## List: is a collection which is ordered and changeable(modifiable).
# Allows duplicate members.
## Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable).
# Allows duplicate members.
## Set: is a collection which is unordered, un-indexed and unmodifiable,
# but we can add new items to the set. Duplicate members are not allowed.
## Dictionary: is a collection which is unordered,
# changeable(modifiable) and indexed. No duplicate members.

##EXERCICE5

##N1
empty_list = []
print(empty_list)

##N2
my_list = [1,2,3,4,5,6,7]
print(my_list)
##N3
print(len(my_list))

##N4
first = my_list[0]
middle = my_list[len(my_list)//2]
last = my_list[-1]
print(first, middle, last)

##N5

mixed_data_types = ["Josué", 19, 1.75, "Célibataire", "Lomé, Togo"]
print(mixed_data_types)

##N6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


##N7
print(it_companies)

##N8
print(len(it_companies)) #affiche la longueur de la liste

##N9
print(it_companies[0])
print(
    (len(it_companies)//2))
print(it_companies[-1])

##N10
it_companies[0] = "Meta"
print(it_companies)

##N11
it_companies.append("Tesla") #ajoute un élément à la fin de la liste
print(it_companies)

##N12
it_companies.insert(len(it_companies)//2, "Intel") #ajoute un élément au milieu de la liste
print(it_companies)

##N13
it_companies[1] = it_companies[1].upper() #permet de mettre en majuscule le deuxième élément de la liste
print(it_companies)

##N14
print(" #; ".join(it_companies)) #permet d'afficher les éléments de la liste séparés par un point virgule

##N15
print("Google" in it_companies)

##N16
it_companies.sort() #permet de trier la liste par ordre alphabétique
print(it_companies)

##N17
it_companies.reverse() #permet d'inverser l'ordre de la liste
print(it_companies)

##N18
print(it_companies[:3]) #permet de découper les 3 premiers entreprises

##N19 
print(it_companies[-3:]) #permet de découper les 3 dernières entreprises

##N20 découpe l'entreprise du milieu
mid = len(it_companies)//2
if len(it_companies)%2==0:
    print(it_companies[mid-1:mid+1])
else:
    print(it_companies[mid])

##N21
it_companies.pop(0) #permet de supprimer le premier élément de la liste
print(it_companies)

##N22
mid = len(it_companies)//2
it_companies.pop(mid) #permet de supprimer l'élément du milieu de la liste
print(it_companies)

##N23
it_companies.pop() #permet de supprimer le dernier élément de la liste car on n'a pas précisé l'indice
print(it_companies)

##N24
it_companies.clear() #permet de vider la liste
print(it_companies)

##N25
del it_companies #permet de supprimer la liste

##N26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end #permet de concaténer les deux listes
print(full_stack)

##N27
full_stack = front_end + back_end
full_stack.insert(full_stack.index("Redux")+1, "Python") #insère "Python" après "Redux"
full_stack.insert(full_stack.index("Python")+1, "SQL") #insère "SQL" après "Python"
print(full_stack)



##EXERCIES: NIVEAU 2

##N1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Trier la liste ages
ages.sort(reverse=False)
print("Ages triées: ", ages)

##N2 : Min et Max

print("Min: ", min(ages))
print("Max: ", max(ages))

##N3: ajouter min et max
ages.extend([min(ages), max(ages)])
print("Après avoir ajouté min et max: ", ages)

##N4: Médiane

n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print("Médiane:", median)

# Moyenne
avg = sum(ages) / len(ages)
print("Moyenne:", avg)

# Étendue (Range)
print("Étendue:", max(ages) - min(ages))

# Comparaison min-avg et max-avg
print("abs(min-avg):", abs(min(ages)-avg))
print("abs(max-avg):", abs(max(ages)-avg))

##1)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
##find the middle of the liste country
middle=len(countries)//2
if len(countries)%2==0:
    print(countries[middle-1:middle+1])
else:
    print(countries[middle])
    
n = len(countries)
print(n)

##calcul du milieu
mid = n // 2
if n % 2 == 0:
    first_half = countries[:mid]
    second_half = countries[mid:]
else:
    first_half = countries[:mid+1]
    second_half = countries[mid+1:] 
    
print("Première moitié:", first_half)
print("Deuxième moitié:", second_half)


##3)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Danemark']
first, second, third, *scandic_countries = countries

print("First country: ",first)
print("Second country: ",second)
print("Third country: ",third)
print("Scandic countries: ",scandic_countries)