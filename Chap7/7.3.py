#7.3.py
#Generating Fibonacci Numbers

#Variable/List Declaration
Fibonacci=[0]*15

Fibonacci[0]=0
Fibonacci[1]=1

#Loop-1
for i in range(2,15):
        Fibonacci[i]=Fibonacci[i-2]+Fibonacci[i-1]  #Calculation

#Loop-2
for i in range(15):
        print("{0}".format(Fibonacci[i]))           #Print Result

