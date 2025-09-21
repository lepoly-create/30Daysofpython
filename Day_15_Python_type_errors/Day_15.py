
PS C:\Users\amega> python
Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<python-input-0>", line 1
    print 'hello world'
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> exit
PS C:\Users\amega> Start-Transcript -Path .\day15_session.txt
Transcription démarrée, le fichier de sortie est .\day15_session.txt
PS C:\Users\amega> python
Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    print(age)
          ^^^
NameError: name 'age' is not defined
>>> age = 19
>>> print(age)
19
>>> print("Index Error")
Index Error
>>> numbers = [1,2,3,4,5]
>>> numbers[5]
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    numbers[5]
    ~~~~~~~^^^
IndexError: list index out of range
>>> print("ModuleNotFoundError")
ModuleNotFoundError
>>> import maths
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    import maths
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> print("AttributeError")
AttributeError
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<python-input-11>", line 1, in <module>
    math.PI
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>> math.pi
3.141592653589793
>>> print("KeyError")
KeyError
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['Asab']
Traceback (most recent call last):
  File "<python-input-15>", line 1, in <module>
    users['Asab']
    ~~~~~^^^^^^^^
KeyError: 'Asab'
>>> users['name']
'Asab'
>>> users['country']
'Finland'
>>> users['county']
Traceback (most recent call last):
  File "<python-input-18>", line 1, in <module>
    users['county']
    ~~~~~^^^^^^^^^^
KeyError: 'county'
>>> print("TypeError")
TypeError
>>> 4+ '3'
Traceback (most recent call last):
  File "<python-input-20>", line 1, in <module>
    4+ '3'
    ~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> print("importError")
importError
>>> from math import power
Traceback (most recent call last):
  File "<python-input-23>", line 1, in <module>
    from math import power
ImportError: cannot import name 'power' from 'math' (unknown location)
>>> from math import pow
>>> pow(2,3)
8.0
>>> pow(2.3)
Traceback (most recent call last):
  File "<python-input-26>", line 1, in <module>
    pow(2.3)
    ~~~^^^^^
TypeError: pow expected 2 arguments, got 1
>>> print("ValueError")
ValueError
>>> int('12a')
Traceback (most recent call last):
  File "<python-input-28>", line 1, in <module>
    int('12a')
    ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: '12a'
>>> str('12a')
'12a'
>>> print("ZeroDivisionError")
ZeroDivisionError
>>> 1/0
Traceback (most recent call last):
  File "<python-input-31>", line 1, in <module>
    1/0
    ~^~
ZeroDivisionError: division by zero
>>> print("We cannot divide a number by zero")
We cannot divide a number by zero
>>> exit
