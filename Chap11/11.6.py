#11.6.py
#Using Linked Lists


#Main()
def main():
        class entry:
                def __init(self):                       #Class constructor
                        self.value=0
                        self.nxt=0

        #Variable declarations & instance creation
        n1=entry()
        n1.value=100
        n2=entry()
        n2.value=200
        n3=entry()
        n3.value=300

        n1.nxt=n2
        n2.nxt=n3

        i=n1.nxt.value

        #Result
        print("{0}".format(i))
        print("{0}".format(n2.nxt.value))



#setting top level conditional script
if __name__=='__main__':
        main()


