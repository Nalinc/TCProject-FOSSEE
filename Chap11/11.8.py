#11.8.py
#Using Pointers and Functions

#Function to change incoming varible
def test(int_pointer):
        int_pointer=100
        return int_pointer

#Main()
def main():

        #Variable declaration
        i=50
        p=i
        print("Before the call to test i = {0}".format(p))
       
        p=test(i)                                           #Function call

        print("After the call to test i = {0}".format(p))


#Setting top level conditional script
if __name__=='__main__':
        main()


