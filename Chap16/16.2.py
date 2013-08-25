#16.2.py
#Copying Characters from Standard Input to Standard Output

#Import system library
import sys

#Main()
def main():
        
        while (True):
                c=raw_input()     #User Input
                print(c);         #Display Result
                if(c=="EOF"):     #Check Exit condition
                   sys.exit()
        

#Setting top level conditional script
if __name__=='__main__':
        main()


