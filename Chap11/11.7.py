#11.7.py
#Traversing a linked list

#Main()
def main():
        class entry:
                def __init__(self):                    #Class constructor
                        self.value=0
                        self.nxt=0

        #Creating class instances
        n1=entry()
        n2=entry()
        n3=entry()
        list_pointer=n1

        #Variable Declaration
        n1.value=100
        n2.value=200
        n3.value=300
        n1.nxt=n2
        n2.nxt=n3
        n3.nxt=0

        while(list_pointer!=0):                         #Calculation
                print("{0}\n".format(list_pointer.value))
                list_pointer = list_pointer.nxt;


#Setting top level conditional script
if __name__=='__main__':
        main()


