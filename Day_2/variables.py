#jour2: 30 days of python programming

# Variables in Python

first_name = 'Josue'
last_name = 'AMEGADJIN'
full_name= {
    'firstname':'josue', 
    'lastname':'AMEGADJIN', 
    }
country = 'TOGO'
city = 'Lomé'
age = 19
year= 2025
is_married = False
is_true = True
is_light_on = True

# Declaring multiple variables on one line

first_name, last_name, country, age, is_married = 'Josue', 'AMEGADJIN', 'TOGO', 19, False

#exercice: Level 2

#Check the data type of all your variables using type() built-in function
print(type(first_name))  
print(type(last_name))  
print(type(country))     
print(type(city))       
print(type(age))         
print(type(is_married)) 
print(type(year))       
print(type(is_true))     
print(type(is_light_on)) 
# Check the length of your variable names
print(len('first_name'))  
print(len('last_name'))   
print(len('country'))     
print(len('city'))        
print(len('age'))         
print(len('is_married'))  
print(len('year'))        
print(len('is_true'))     
print(len('is_light_on')) 

#compare the length of your first name and last name

print(len(first_name) == len(last_name))  

#declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4

# add num_one and num_two and assign the result to a variable total
total = num_one + num_two

# substract num_two from num_one and assign the result to a variable diff
diff = num_one - num_two

# multiply num_one and num_two and assign the result to a variable product
product = num_one * num_two

# divide num_one by num_two and assign the result to a variable division
division = num_one / num_two

#use modulus division to find num_one divided by num_two and assign the result to a variable remainder
remainder = num_one % num_two

#calculate num_one to the power of num_two and assign the result to a variable exponent
exponent = num_one ** num_two

#find floor division of num_one by num_two and assign the result to a variable floor_division
floor_division = num_one // num_two


#calculate the area of a circle and assign the value to a variable name of area_of_circle
import math
radius = 30
area_of_circle = math.pi * (radius ** 2)
#calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * radius
#take radius as user input and calculate the area
radius_input = float(input("Enter the radius of the circle: "))
area_of_circle_input = math.pi * (radius_input ** 2)

#use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variables names
first_name_input = input("Enter your first name: ")
last_name_input = input("Enter your last name: ")
country_input = input("Enter your country: ")
age_input = int(input("Enter your age: "))

#run help('keywords') in Python shell or in your file to check for the python reserved words or keywords

