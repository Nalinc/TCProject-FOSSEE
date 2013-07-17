#6.3.py
#Determining if a Number Is Even or Odd

#Variable declaration
number_to_test=int(raw_input("Enter your number to be tested: "))

#Calculation
remainder=number_to_test%2

#Result
if(remainder==0):
   print("Number is even")
if(remainder!=0):
   print("Number is odd")



