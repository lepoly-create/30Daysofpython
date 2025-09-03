# Day 1 - 30DaysOfPython Challenge 
print(3 + 4)             # addition(+) 
print(3 - 4)             # subtraction(-) 
print(3 * 4)             # multiplication(*) 
print(3 / 4)             # division(/) 
print(3 ** 4)            # exponential(**) 
print(3 % 4)             # modulus(%) 
print(3 // 4)            # Floor division operator(//) 

#exo2 number3
print('josue')
print('AMEGADJIN')
print('TOGO')
print("je profite de 30 jours de python")

#  Exo 2 number 4 - Checking data types
print(type(10))          # Int 
print(type(3.14))        # Float 
print(type(4 - 4j))      # Complex number print(type('Asabeneh'))  # String 
print(type(['Asabeneh', 'Python', 'Finland']))   # List print(type({'name':'Asabeneh'})) # Dictionary 
print(type({'my name':'josue' ,'my family name':'AMEGADJIN' , 'my country':'TOGO'}))

#Exercice 3 
#number 1

print(type(19))#this is int number
print(type(3.145))#this is float
print(type(3-2j))#this is a complex
print(type('my name'))#this is string
print(type([9, 11, 15]))#this is a list
print(type({'my friend':'Bossro'}))#this is the dictionary
print(type({6.66, 8.9, 10}))#this is set
print(type((6.66, 8.9, 10)))#this is tuple

#Exo 3 number 2
#distance euclidienne entre les points de coordonnées (2, 3) et (10, 8)
import math
point1 = (2, 3)
point2 = (10, 8)
distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
print("La distance euclidienne entre les points", point1, "et", point2, "est", distance)

