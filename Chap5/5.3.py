#5.3.py
#Generating a Table of Triangular Numbers

print("TABLE OF TRIANGULAR NUMBERS\n\n")
print(" n          Sum from 1 to n\n")
print("---        -----------------\n")

#Variable Declarations
triangularNumber=0

#Calculation/Result
for i in range (1,11):
    triangularNumber=triangularNumber+i
    print(" {0}                  {1}\n".format(i,triangularNumber))    






