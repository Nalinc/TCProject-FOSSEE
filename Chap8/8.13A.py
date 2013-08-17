#8.13A.py
#Multidimensional Variable-Length Arrays

#Import system Library
import sys

#Main()
def main():

        #List/Variable Declaration
        sampleMatrix =[ [ 7, 16, 55, 13, 12 ],
                        [ 12, 10, 52, 0, 7 ],
                        [ -2, 1, 2, 4, 9 ]   ]


        print("Original matrix:\n")
        displayMatrix(3,5,sampleMatrix)                     #Function call-1

        scalarMultiply(3,5,sampleMatrix, 2)                 #Function Call-2
        print("\nMultiplied by 2:\n")
        
        displayMatrix(3,5,sampleMatrix);                    #Function call-3
        scalarMultiply(3,5,sampleMatrix, -1)                #Function call-4
        
        print("\nThen multiplied by -1:\n")
        displayMatrix(3,5,sampleMatrix)                     #Function call-5


#Function to multiply matrix by a scalar quantity        
def scalarMultiply(nRows,nCols,matrix,scalar):
        for row in range(0,nRows):                                 #Calculation
                for column in range(0,nCols):
                        matrix[row][column]*=scalar          


#Function to display the matrix
def displayMatrix(nRows,nCols,matrix):
        for row in range(0,nRows):                                 #Result
                for column in range(0,nCols):
                        sys.stdout.write("{0:7}".format(matrix[row][column]))
                sys.stdout.write("\n")


#Setting top level conditional script
if __name__=='__main__':
        main()



