#7.8.py
#Generating Fibonacci Numbers Using Variable-Length Arrays

#import Libraries
import sys                               #For sys.exit()     
 
#User Input        
numFibs=input("How many Fibonacci numbers do you want (between 1 and 75)? ")

if(numFibs<1 or numFibs>75):
        print("bad number,sorry!")
        sys.exit()

#Variable Declarations        
Fibonacci=[0]*numFibs
Fibonacci[0]=0
Fibonacci[1]=1

#Calculation
for i in range(2,numFibs):
    Fibonacci[i]=Fibonacci[i-2]+Fibonacci[i-1] 
            
#Result
for i in range(numFibs):
    print("{0}".format(Fibonacci[i]))     

