#5.4.py
#Asking the User for Input

#Variable Declaration/User Input
triangularNumber=0
number=input("What triangular number do you want?")

#Calculations
for n in range (1,(number+1)):
        triangularNumber+=n

#Result
print("triangular number {0} is {1}".format(number,triangularNumber))

