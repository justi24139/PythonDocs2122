#Justin Holweck
#Practice using expresion and conditional statement

#An experession is a problem that must be solved
# 5  + 5 is an "arithmetic" expression
x = 5 + 5

#Functions/methods must be resolved as expressions as well
answer = input("What is your name?")

#Comparison expression resolve as True/False
print( 7 > 7 )
print( 7 <= 7 )
print( x == 10)
print( x > 10 or x < 10)

#A conditional statements runs if it's condition is not False
if answer == "BROB":
    print("Hello, BROB! Welcome back")
    print("This line also prints if your name is BROB")
elif answer == "Vadim":
    print("Hey! You still owe me money!")
else:
    print("Sorry, I only talk to Bobs")
print("This inside of the if statement , and print regardless")
    
# ^ If checks a condition
# ^ Elif checks a conidition if the previous conditions were not True
# ^ Ypu can have as many elif's as you wants
# ^ Elseruns if no prior condditions were true
age = input('What is your age?')
age = int(age)
if age >= 10:
    print("Ok, here is your lisense")
elif age == 9:
    print("You have one more year to go.")
    
else:
    print("You are just to young")

