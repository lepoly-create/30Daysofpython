# language = 'Python'
# lst =[i for i in language]

# print(lst)

# numbers = [(i, i*i) for i in range(11)]
# print(numbers)
# print("\n")
# even_numbers = [ i for i in range(21) if i % 2  ==0]
# print(even_numbers)
# print("\n")

# list_of_listes = [[1,2,3] , [4,5,6] ,[7,8,9] ]
# flattened_list = [numbers for row in list_of_listes for numbers in row]
# print(flattened_list)
# print("\n")
# def add_to_nums(a, b):
#     return a+b
# print(add_to_nums(2, 3))
# print("\n")
# add_to_nums = lambda a,b : a+b
# print(add_to_nums(2, 3))
# print("\n")

# multiple_value = lambda  a,b,c : a**2 -3*b +4*c
# print(multiple_value(5,3,2))
# def power(x):
#     return lambda n : x ** n
# cube = power(2)(3)
# two_power_of_five = power(2)(5)
# print(two_power_of_five)


##Exercice: Day_13
##N1:
numbers = [-4,-3,-2,-1,0,2,4,6]
negative_and_zero = [i for i in numbers if i <= 0]
print(negative_and_zero)

##N2:
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dimensional = [num for sublist in list_of_lists for inner in sublist for num in inner]
print(one_dimensional)

##N3:
listes_tuples = [(x,1,x, x**2, x**3, x**4, x**5) for x in range(11)]
print(listes_tuples)

##n4:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
formatted = [[country.upper(), country[:3].upper(), city.upper()] for [(country, city)] in countries]
print(formatted)

##N5:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list = [{'country': country.upper(), 'city': city.upper()} for [(country, city)] in countries]
print(dict_list)

##N6:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for [(first, last)] in names]
print(full_names)

##N7:
# pente
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# ordonnée à l’origine
intercept = lambda x, y, m: y - m * x

print("Slope:", slope(2, 3, 6, 7))       # (7-3)/(6-2) = 1.0
print("Intercept:", intercept(2, 3, 1))  # b = y - mx = 3 - (1*2) = 1









