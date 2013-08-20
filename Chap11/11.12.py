#11.12.py
#Summing the Elements of an Array--version 2

#Function to evaluate sum of array elements
def arraySum (array,n):
        #Variable Declaration
        sum = 0 
        #Calculation
        for i in array:
                 sum += i
        return sum

#Main()
def main():

        #List Declaration
        values = [ 3, 7, -9, 3, 6, -1, 7, 9, 1, -5 ]
        #Result
        print("The sum is {0}\n".format(arraySum(values,10)))

#Setting top level conditional script
if __name__=='__main__':
        main()


