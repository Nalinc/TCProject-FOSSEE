#8.11.py
#Changing Array Elements in Functions

#Import System Library
import sys

#Function to multiply elements by 2
def multiplyBy2(array,n):
        for i in range (0,n):                                     #Iteration/Calculation
                array[i]*=2

#Main()
def main():

        #List/Variable Declaration
        floatVals=[1.2, -3.7, 6.2, 8.55]      
        multiplyBy2(floatVals,4)

        for i in range (0,4):
                sys.stdout.write("{0:.2f} ".format(floatVals[i]))  #Result
        print("\n")

#Setting top level conditional script
if __name__=='__main__':
        main()


