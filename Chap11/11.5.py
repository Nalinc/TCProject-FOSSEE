#11.5.py
#Using classes Containing pointer variables

#Main()
def main():
        class intPtrs:
                def __init__(self):             #Class constructor
                        self.p1=0
                        self.p2=0

        #Variable Declarations & Instance creation
        i1=100
        pointers=intPtrs()
        pointers.p1=i1
        i2=-97
        pointers.p2=i2

        #Result
        print("i1 = {0}, pointers.p1 = {1}\n".format(i1, pointers.p1))
        print("i2 = {0}, pointers.p2 = {1}\n".format(i2, pointers.p2))


#Setting top level conditional script
if __name__=='__main__':
        main()


