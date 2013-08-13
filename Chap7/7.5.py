#7.5.py
#Initializing Arrays

#Variable/List Declarations
array_values=[0]*10
array_values[0:4]=[0,1,4,9,16]

#Calculations
for i in range(5,10):
        array_values[i]=i*i

#Results
for i in range(10):
        print("array values[{0}] = {1}".format(i,array_values[i]))

