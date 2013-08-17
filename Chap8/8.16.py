#8.16.py
#Calculating Factorials Recursively

#Function to calculate factorial
def factorial(n):
        if( n == 0 ):                            #Calculation
                result = 1
        else:
                result = n * factorial (n - 1)
        return result;

#Main()
def main():
        for j in range (0,11):
                print("{0:3}! = {1}\n".format(j,factorial (j)))


#Setting top level conditional script
if __name__=='__main__':
        main()

