#10.4.py
#Testing Strings for Equality

#Function to compare 2 strings
def equalStrings(s1,s2):
        
        #Calculation
        if(s1==s2):
                areEqual=True
        else:
                areEqual=False
        return areEqual



def main():

        #String Declaration
        stra = "string compare test";
        strb = "string";

        #Result
        print("{0}".format(equalStrings (stra, strb)))
        print("{0}".format(equalStrings (stra, stra)))
        print("{0}".format(equalStrings (strb, "string")))


#Setting top level confditional script
if __name__=='__main__':
        main()



