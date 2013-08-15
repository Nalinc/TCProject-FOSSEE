#8.5.py
#Revising the Program to Find the Greatest Common Divisor

#Import Library 
import sys                                                 

def gcd(u,v):                                                   #Function to calculate gcd
        sys.stdout.write("gcd of {0} and {1} is: ".format(u,v))
        while(v!=0):
            temp=u%v
            u=v
            v=temp
        sys.stdout.write("{0}\n".format(u))



def main():                                                     #Main() function
   gcd(150,35)                                                  
   gcd(1026,405)
   gcd(83,240)

if __name__=='__main__':                                        #Setting Top level conditional script 
   main()


