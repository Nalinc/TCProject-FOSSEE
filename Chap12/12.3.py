#12.3.py
#Implementing a Shift Function

#Function to perform bitwise shift
def shift(value,n):
        if(n>0):
                value <<=n              #Left shift
        else:
                value >>=-n             #Right Shift

        return value

#Main()
def main():
        #Variable Declaration
        w1=177777
        w2=444

        #Result
        print("{0:7}   {1:7}".format(shift(w1,5),w1<<5))
        print("{0:7}   {1:7}".format(shift(w1,-6),w1>>6))
        print("{0:7}   {1:7}".format(shift(w2,0),w2>>0))
        print("{0:7} ".format(shift(shift(w1,-3),3)))

#Setting top level conditional script
if __name__=='__main__':
        main()
