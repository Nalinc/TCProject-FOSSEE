#8.13.py
#Using Multidimensional Arrays and Functions

#Import system Library
import sys

#Main()
def main():

        #List/Variable Declaration
        sampleMatrix =[ [ 7, 16, 55, 13, 12 ],
                        [ 12, 10, 52, 0, 7 ],
                        [ -2, 1, 2, 4, 9 ]   ]


        print("Original matrix:\n")
        displayMatrix(sampleMatrix)                     #Function call-1

        scalarMultiply(sampleMatrix, 2)                 #Function Call-2
        print("\nMultiplied by 2:\n")
        
        displayMatrix(sampleMatrix);                    #Function call-3
        scalarMultiply(sampleMatrix, -1)                #Function call-4
        
        print("\nThen multiplied by -1:\n")
        displayMatrix(sampleMatrix)                     #Function call-5


#Function to multiply matrix by a scalar quantity        
def scalarMultiply(matrix,scalar):
        for row in range(0,3):                                 #Calculation
                for column in range(0,5):
                        matrix[row][column]*=scalar          


#Function to display the matrix
def displayMatrix(matrix):
        for row in range(0,3):                                 #Result
                for column in range(0,5):
                        sys.stdout.write("{0:7}".format(matrix[row][column]))
                sys.stdout.write("\n")


#Setting top level conditional script
if __name__=='__main__':
        main()



