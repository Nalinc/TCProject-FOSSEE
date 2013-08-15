#8.6.py
#Finding the Greatest Common Divisor and Returning the Results

#Import Library 
import sys                                                 

def gcd(u,v):                                                   #Function to calculate gcd

        while(v!=0):
            temp=u%v
            u=v
            v=temp
        return u

def main():                                                     #Main() function
   result= gcd(150,35)                                                  
   print("the gcd of 150 and 35 is: {0}".format(result))
   result=gcd(1026,405)
   print("the gcd of 1026 and 405 is: {0}".format(result))  
   result= gcd(83,240)
   print("the gcd of 83 and 240 is: {0}".format(result))

if __name__=='__main__':                                        #Top level conditional script 
   main()


