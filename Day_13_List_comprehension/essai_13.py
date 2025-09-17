language = 'AMEGADJIN'
lst = [i for i in language]
print(lst)

squares = [(i,i*i) for i in range(2, 9,2)]
print(squares)

#lambda function
def add_three_nums(a,b,c):
    return a+b+c
print(add_three_nums(2,3,5))
add_three_nums = lambda a,b,c : a+b+c
print(add_three_nums(-1, -2,9))

(lambda  a,b,c: a+b+c)(2,-1,-9)
print()