#7.4.py
#Revising the Program to Generate Prime Numbers,Version 2

#Variable Declaration
primeIndex=2
primes=[0]*50

primes[0]=2
primes[1]=3
p=5

#Calculations
while(p<=50):                                        #Outer Loop-1
        isPrime=True
        
        i=1
        while(isPrime and p/primes[i]>=primes[i]):   #Inner Loop
            if(p%primes[i]==0):
               isPrime=False
            i+=1
         

        if(isPrime==True):
           primes[primeIndex]=p
           primeIndex+=1
        p=p+2

#Results
for i in range (primeIndex):                         #Outer Loop-2
        print("{0}".format(primes[i]))



