#8.14.py
#Converting a Positive Integer to Another Base

#Import system Libraries
import sys

#Function to get Number & Base
def getNumberAndBase():
        
        #Global Reference
        global digit
        global numberToConvert
        global base
       
        #Variable Declaration
        digit=0
        numberToConvert=input("Number to be converted ?")
        base=input("Base?")
        if(base<2 or base>16):
                print("Bad base - must be between 2 and 16\n");
                base = 10;

#Conversion Function
def convertNumber():
        
        #Global Reference
        global numberToConvert
        global base
        global convertedNumber
        global digit
        convertedNumber=[0]*64                                      #List declaration
        
        while(numberToConvert!=0):
                convertedNumber[digit]=numberToConvert%base         #Calculations
                digit=digit+1
                numberToConvert/=base


#Function to display
def displayConvertedNumber():

        #Global reference 
        global baseDigits
        global digit 

        #List/Variable Declaration
        baseDigits=[ '0', '1', '2', '3', '4', '5', '6', '7',\
                          '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' ]
        sys.stdout.write("Converted number = ")
       
        digit=digit-1

        for i in range(digit,-1,-1):
                nextDigit = convertedNumber[i];
                sys.stdout.write("{0}".format(baseDigits[nextDigit]));  #Result

        sys.stdout.write("\n")



#Main()
def main():
        getNumberAndBase()                               #Function call-1
        convertNumber()                                  #Function call-2
        displayConvertedNumber()                         #Function call-3


#Setting top level conditional script
if __name__=='__main__':
        main()

