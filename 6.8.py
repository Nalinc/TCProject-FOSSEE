#6.8.py
#evaluate simple expressions of the form
#<number operator number>


try:
#Variable declaration/User input
  value1, operator, value2=raw_input("Type in your expression(with spaces inbetween): ").split()
except:
  print("err.. follow the syntax <value operator value>") 
  print("with spaces inbetween\n")

#Parsing
value1,value2=[float(value1),float(value2)]

#Calculation/Result
if(operator=='+'):
     print("answer: {0:.2f}".format(value1+value2))
elif(operator=='-'):
     print("answer: {0:.2f}".format(value1-value2))
elif(operator=='*'):
     print("answer: {0:.2f}".format(value1*value2))
else:
     print("answer: {0:.2f}".format(value1/value2))





