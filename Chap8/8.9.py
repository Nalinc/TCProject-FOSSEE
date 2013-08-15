#8.9.py
#Finding the Minimum Value in an Array

#Function to return minimum value
def minimum(values):
        minValue=values[0]                                   #Variable Declaration
        for i in range (1,10):                               #Calculation
                if(values[i]<minValue):
                        minValue=values[i]

        return minValue
                   
#Main()
def main():
        scores=[]                                            #Variable Declaration
        print("Enter 10 scores:")
        for i in range (0,10):
            scores.append(input())              

        minScore=minimum(scores)                             #Function call & assignment
        print("\nMinimum score is {0}\n".format(minScore))   #Result

#Setting top level conditional script
if __name__=='__main__':
        main()
       

