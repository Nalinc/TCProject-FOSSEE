#4.5.py
#Converting Between Integers and Floats

#Variable Declarations
f1=123.125
f2=1.0
i1=1
i2=-150
c='a'


i1=f1                                                              #floating to integer conversion
print("{0} assigned to an int produces {1:.0f}".format(f1,i1))

f1=i2                                                              #integer to floating conversion
print("{0} assigned to a float produces {1}".format(i2,f1))

f1=i2/100                                                          #integer divided by integer
print("{0} divided by 100 produces {1}".format(i2,f1))

f2=i2/100.0                                                        #integer divided by a float
print("{0} divided by 100.0 produces {1}".format(i2,f2))

f2=float(i2/100)                                                   #type cast operator
print("{0} divided by 100 produces {1}".format(i2,f2))



