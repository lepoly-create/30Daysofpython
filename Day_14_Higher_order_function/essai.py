

#functions as a parameter
def sum_numbers(nums):
    return sum(nums)
def higher_order_function(f, lst):
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1,2,3,4,5])
print(result)
#python closures

def add_ten():
    ten=10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))
#python decorators
#creating decorators
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g= uppercase_decorator(greeting)
print(g())

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper()
@uppercase_decorator
def greeting():
    return 'Welcome to comme back from Python'
print(greeting)

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters
@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format( first_name, last_name, country))
print_full_name("Asabeneh", "Yetayeh",'Finland')

#map function

numbers = [1,2,3,4,5]
def square(x):
    return x**2
numbers_squared = map(square, numbers)
print(list(numbers_squared))
#with a lambda function
numbers_squared= map(lambda x: x**2, numbers)
print(list(numbers_squared))

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham'] # iterable
def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased)) # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased)) # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

#exemple de la différnce de map, reduce, filter

from functools import reduce
nums = [1,2,3,4]
print(list(map(lambda x: x*2, nums)))
print(list(filter(lambda x: x%2==0,nums)))
print(reduce(lambda x,y: x*y, nums)) #lambda ne peut pas prendre 3 arguments??
#car j'ai essayé ici mais on me signale un messaged'error















