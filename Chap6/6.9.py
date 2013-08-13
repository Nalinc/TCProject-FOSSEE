#6.9.py
#evaluate simple expressions of the form
#<number operator number>  (Version 2)


try:
#Variable declaration/User input
   value1, operator, value2=raw_input("Type in your expression(with spaces inbetween): ").split()
except:
  print("err.. follow the syntax <value operator value>") 
  print("with spaces inbetween\n")

#parsing
value1,value2=[float(value1), float(value2)]

#Calculation/Result
if(operator=='+'):
   print("Answer= {0:.2f}".format(value1+value2))
elif(operator=='-'):
   print("Answer= {0:.2f}".format(value1-value2))
elif(operator=='*'):
   print("Answer= {0:.2f}".format(value1*value2))
elif(operator=='/'):
   if(value2==0):
      print("Whoops! divide by 0 issue")
   else:
      print("Answer= {0:.2f}".format(value1/value2))
else:
   print("err.. Invalid operator")




