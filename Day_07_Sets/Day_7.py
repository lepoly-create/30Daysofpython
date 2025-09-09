##Les sets

##EXERCICE1 : Niveau 1
##N1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("\nlength:", len(it_companies)) ## len() retourne le nombre d'éléments uniques

##N2
it_companies.add("Twitter") ##add() insère un seul élément
print("\nAfter adding Twitter :",it_companies)

##N3
it_companies.update(['Samsung', 'Intel', 'HP'])
print("\nAfter adding multiple companies:", it_companies) ##update() insère plusieurs éléments

##N4
it_companies.remove('Google')
print("\nAfter removing Google:", it_companies) ##remove() supprime l'élément, lève une erreur si l'élément n'existe pas

##N5 : différence entre remove et discard 

# remove -> erreur si l'élement n'existe pas
# discard -> ne provoque pas d'erreur si l'élement est absent
it_companies.discard('NotExist')

##EXERCICE2 : Niveau 2
##Données

A= {19,22, 24, 20, 25, 26}
B= {19,22, 20, 25, 26, 24, 28, 27}

##N1: Union de A et B
print("\nUnion:", A.union(B))

##N2: Intersection de A et B

print("\nIntersection:", A.intersection(B))

##N3: Est-ce que A est un sous-ensemble de B ?
print("\nIs A subset of B ?", A.issubset(B))

##N4: Est-ce que A et B sont disjoints ?
print("\nAre A and B disjoint?", A.isdisjoint(B))

##N5: Union dans les deux sens ?
## l'union est commutative , donc les résultats sont identiques
print("\nA Union B:", A.union(B))
print("B Union A:", B.union(A))

##N6:  différence symétrique
print("\nSymmetric Difference:", A.symmetric_difference(B))
## éléments présents dans l'un OU l'autre mais pas dans les deux

##N7: Supprimer complétement les ensembles
del A
del B


##NIVEAU 3

##N1: Convertir age en set et comparer la longueur avec la liste

age = [22, 19, 24, 25, 26, 24, 25, 24]

age_set = set(age)
print("\nLength of list:", len(age))
print("Length of set:", len(age_set))

##N2: différence entre string, list, tuple,set

## String
print("""\n
- Type de données immuable
- Utilisé pour stocker des séquences de caractères
- Déclaré avec des guillemets simples ou doubles

## List
- Type de données mutable
- Utilisé pour stocker des séquences d'éléments
- Déclaré avec des crochets []

## Tuple
- Type de données immuable
- Utilisé pour stocker des séquences d'éléments
- Déclaré avec des parenthèses ()

## Set
- Type de données mutable
- Utilisé pour stocker des éléments uniques
- Déclaré avec des accolades {}
""")

##N3: combien de mots uniques dans la phrase ?

sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print("\nUnique words:", unique_words)
print("Number of unique words:", len(unique_words))
