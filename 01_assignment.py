Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> print(x)
5
>>> x + 5
10
>>> x = 10
>>> x = 5
>>> y = x +5
>>> print(y)
10
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> input("What is your name? ")
What is your name? J Money
'J Money'

>>> name= input("What is your name?"
	    k
	    
SyntaxError: invalid syntax
>>> name= input("What is your name?")
What is your name?Bob
>>> print(name)
Bob
>>>
#Justin Holweck
#Assignment Examples

#You can assign "Values" to "Variables"
# by using and equals (right side into left side)
x = 5

#When Python reads a variable name, replaces i
# with the variable' stored value
y  = x + 5

# There are 4 diffrent perimitive data types
# Integers: any whole number positive or neagitive
age = 15
#Float any number with a decimal, positive or neagitive.
grade= 100.1
#string: a string of human readable characters
name = "Justin"
# numbers in a string are not numbers, they are letters
favoriteNumber = "17"
#Boolean: True or False
# True is any value that is not false or empty
isSmart = True

#You can output into the console using print
print(age)
print(grade)
print(name)
print(favoriteNumber)
print(isSmart)

#You concatenate values togethers
print("My name is "+ name)
#You can use functions to convert data types
print("and my age is" + str( age))
#Don't forget! If you want to convert a value permant;y
#you must assign the converted value to a variable
#you can convert back and forth wiht int(), str(), bool(), float()
print(int(age))
print(float(age))
print(bool(age))
