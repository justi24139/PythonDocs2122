#import the basics module to use its code
import basics

#make a new application abject from the basic module
app = basics.newProgram()

#use a method that belongs to our new application object
app.print('yo mama')

#print a property of our new application object
app.print( app.debugging )

#This line won't print if app.debugging is false
app.debug("Hello")

#We'll enable debugging for the application
app.debugging = True
app.debug('Now it Works!')

#Import a default Python module
import random

#use a method from the random module
randomNumber = random.randint(1, 10)
app.print(randomNumber)
