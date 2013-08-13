#6.4.py
#Program to determine if a number is even or odd (Ver. 2)

#Variable declaration/User input
number_to_test=int(raw_input("Enter your Number to be tested: "))

#Calculation
remainder=number_to_test%2

#Result
if(remainder==0):
    print("The number is even.\n")
else:                      #using 'else' instead of second 'if'
    print("The number is odd.\n")





