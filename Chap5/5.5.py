#5.5.py
#Using Nested for Loops

#Calculations
for counter in range(1,6):                     #Outer Loop
        number=input("what triangular number do you want? ")

        triangularNumber=0                     #Variable Decaration

        for n in range (1,(number+1)):         #Inner Loop
           triangularNumber+=n
        
        #Result
        print("Triangular Number {0} is {1}".format(number,triangularNumber))

