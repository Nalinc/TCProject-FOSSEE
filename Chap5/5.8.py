#5.8.py
#Reversing the Digits of a Number

#Import Library
import sys

#Variable declaration/User Input
number=input("Enter your number.\n")

#Calculation/Result
while(number!=0):
        right_digit=number%10
        sys.stdout.write("{0}".format(right_digit))
        number=number/10

print("\n")

