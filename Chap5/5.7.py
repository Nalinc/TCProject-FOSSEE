#5.7.py
#Finding the Greatest Common Divisor

print("Please type in two nonnegative integers.")
#Variable Declaration/User Input
u=input()
v=input()

#Calculation
while(v!=0):
        temp=u%v
        u=v
        v=temp

#Result
print("Their greatest common divisor is {0}\n".format(u))



