#8.10.py
#Revising the Function to Find the Minimum Value in an Array

#Function to return minimum value
def minimum(values,numberOfElements):        
        minValue=values[0]                                    #Variable Declaration
        for i in range(1,numberOfElements):                   #Iteration/Calculations
                if(values[i]<minValue):
                        minValue=values[i]
        
        return minValue

#Main()
def main():
        #List/Variable Delcaration
        array1 = [ 157, -28, -37, 26, 10 ]                       
        array2 = [ 12, 45, 1, 10, 5, 3, 22 ]
        
        #Result
        print("array1 minimum: {0}".format(minimum (array1, 5)));
        print("array2 minimum: {0}".format(minimum (array2, 7)));

#Setting top level conditional script 
if __name__=='__main__':
        main()      
