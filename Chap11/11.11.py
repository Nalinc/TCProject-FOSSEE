#11.11.py
#Working with Pointers to Arrays/Lists

#Function to evaluate sum of array elements
def arraySum (array,n):

        #Variable Declaration
        sum = 0 
        arrayEnd = n
        #Calculation
        for i in range(0,arrayEnd):
                 sum += array[i]
        return sum

#Main()
def main():

        #List Declaration
        values = [ 3, 7, -9, 3, 6, -1, 7, 9, 1, -5 ]
        #Result
        print("The sum is {0}\n".format(arraySum (values, 10)))

#Setting top level conditional script
if __name__=='__main__':
        main()


