#8.4.py
#Calculating the nth Triangular Number


def calculateTriangularNumber(n):                 #Function to calculate triangular number
        triangularNumber=0                        #Variable Dclaration
                          
        for i in range (1,n+1):                   #Calculation/Iteration
             triangularNumber+=i
     
        print("Triangular Number {0} is {1}".format(n,triangularNumber))


def main():
        calculateTriangularNumber(10)              #Function call-1
        calculateTriangularNumber(20)              #Function call-2
        calculateTriangularNumber(50)              #Function call-3
 

if __name__=='__main__':                            #Setting top level conditional script
      main()


