import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh'))

#import functions from a module

from mymodule import generate_full_name, sum_two_nums, person
print(generate_full_name('AMEGADJIN', 'josue'))
print(sum_two_nums(1, 9))
print(person['firstname'])

from statistics import *
ages = [20, 20, 4, 24, 25,22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

import math
print(math.pi)
print(pow(2,3))