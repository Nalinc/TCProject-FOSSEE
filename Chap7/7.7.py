#7.7.py
#Converting a Positive Integer to Another Base

#import Library
import sys                                    #for sys.stdout.write()

#Variable Declarations
baseDigits=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
convertedNumber=[0]*10
index=0

numberToConvert=input("Number to be converted?: ")
base=input("Base?: ")

#Calculations
while True:
     convertedNumber[index]=numberToConvert%base
     index+=1
     numberToConvert=numberToConvert/base
     if(numberToConvert==0):
        break

#Result
print("Converted Number= ")
index-=1
while(index>=0):
        nextDigit=convertedNumber[index]
        sys.stdout.write("{0} ".format(baseDigits[nextDigit]))
        index-=1

print("\n")



