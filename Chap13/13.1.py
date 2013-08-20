#13.1.py
#defining constants

#Variable Decarations
global YES
global NO
YES=1
NO=0


#Function to check if a number is even or odd
def isEven(number):
        global YES
        global NO

        if(number%2==0):
                answer=YES
        else:
                answer=NO

        return answer

#Main()
def main():
        global YES
        global NO

        #Calculation/Result
        if(isEven(17)==YES):
                print("YES")
        else:
                print("NO")

        
        if(isEven(20)==YES):
                print("YES")
        else:
                print("NO")


#Setting top level conditional script
if __name__=='__main__':
        main()


