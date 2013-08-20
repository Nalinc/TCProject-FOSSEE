#12.2.py
#Illustrate Bitwise Opertors

#Main()
def main():

        #variable Declarations
        w1=525
        w2=707
        w3=122
        
        print("{0:5}  {1:5}  {2:5}".format(w1&w2,w1|w2,w1^w2))
        print("{0:5}  {1:5}  {2:5}".format(~w1,~w2,~w3))
        print("{0:5}  {1:5}  {2:5}".format(w1^w1,w1&~w2,w1|w2|w3))
        print("{0:5}  {1:5}".format(w2&w3,w1|w2&~w3))
        print("{0:5}  {1:5}".format(~(~w1&~w2),~(~w1|~w2)))

        #Exchange variables
        w1^=w2
        w2^=w1
        w1^=w2
        print("w1={0:3}  w2={1:3}".format(w1,w2))


#Setting top level conditional script
if __name__=='__main__':
        main()

