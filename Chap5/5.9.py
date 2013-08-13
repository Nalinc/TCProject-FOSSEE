#5.9.py
#Implementing a Revised Program to Reverse the Digits of a Number
#(do-while equivalent code)

#Import Library
import sys

#Variable Declaration/User Input
number=input("Enter your number:\n")

#Calculation/Result
while True:                                     #Enter loop instantly for the first time
    right_digit=number%10
    sys.stdout.write("{0}".format(right_digit))
    number=number/10
    if(number == 0):                            #Check for exit condition
        break

print("\n")


