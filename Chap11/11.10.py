#11.10.py
#Returning a Pointer from a Function

#Class Declaration
class entry:
        def __init__(self):                     #Class constructor
                self.value=0
                selfnxt=0

        def FindEntry(listPtr,match):           #Function to traverse list

                #Calculation
                while(listPtr!=0):
                        if(int(listPtr.value)==int(match)):
                                return listPtr
                        else:
                                listPtr=listPtr.nxt

                return 0

#Main()
def main():

        #Creating instance
        n1=entry()
        n2=entry()
        n3=entry()
        listPtr=entry()

        #Variable declaration
        n1.value=100
        n2.value=200
        n3.value=300

        n1.nxt=n2
        n2.nxt=n3
        n3.nxt=0
        listStart=n1
        
        print("Enter value to locate: ")
        search=raw_input()
        listPtr = entry.FindEntry (listStart, search)    #Function call

        #Result
        if ( listPtr != 0 ):
                print("Found {0}.\n".format(listPtr.value))
        else:
                print("Not found.\n")


#Setting top level conditional script
if __name__=='__main__':
        main()


