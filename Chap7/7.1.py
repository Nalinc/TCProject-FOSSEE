#7.1.py
#Working with an Array(or list in python)

#Variable/List declaration
values=[0]*10

#Initialisation/Calculation
values[0]=197
values[2]=-100
values[5]=350
values[3]=values[0]+values[5]
values[9]=values[5]/10
values[2]-=1
i=0

#Iteration/Result
for index in values:
   print("values[{0}] = {1}".format(i,index))
   i=i+1

