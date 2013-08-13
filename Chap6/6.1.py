#6.1.py
#Calculating the Absolute Value of an Integer

#Variable Declaration/User input
number=int(raw_input("Type in your number: "))

#Calculation
try:
    if( number < 0 ):
      number=-number     #change sign,if number is negative
except: 
    print "not a number" #Invalid input/value error
 
#Result
print ("The absolute Value is {0}".format(number))

