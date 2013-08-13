#6.6.py
#Implementing the Sign Function

#Variable declaration/User input
number=int(raw_input("Please type in a number: "))

#Calculations
try:
   if(number<0):         #Negative Number
     sign=-1
   elif(number==0):      #No sign
     sign=0
   else:                 #Positive Number
     sign=1
except:                  #Value error
   print("invalid input")

#Result
print("Sign= {0}".format(sign))



