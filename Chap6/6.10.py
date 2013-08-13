#6.10.py
#Generating a Table of Prime Numbers

#Variable declarations
p=2

#Calculations
while(p<=50):          #Outer loop
   isPrime=1           #Variable declaration
   d=2                 
   while(d<p):         #Inner loop
       if(p%d==0):
         isPrime=0
       d=d+1           #End of inner loop
      
   if( isPrime!=0):
#Print Result
      print " ",p    
   p=p+1               #End of outer loop

