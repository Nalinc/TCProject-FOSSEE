#8.3.py
#More on Calling Functions


def printMessage():                                #Function to Print Message
        print("Programming is Fun.\n")             #Print Statement


def main():               
     for i in range (1,6):                         #Main() function
        printMessage()


if  __name__ =='__main__':                         #Setting Top-level script environment
     main()


