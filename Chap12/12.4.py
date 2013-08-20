#12.4.py
#Implementing a Rotate Function

#Function to perform rotation
def rotate(value,n):

        #Calculation
        if(n>0):
                n=n%32
        else:
                n=-(-n%32)

        if(n==0):
                result=value
        elif(n>0):
                bits=value>>(32-n)
                result=value<<n|bits
        else:
                n=-n
                bits=value<<(32-n)
                result=value>>n|bits

        return result


#Main()
def main():
#Variable Declaration
        w1=0xabcdef00
        w2=0xffff1122

        print("%x"%rotate(w1,8))
        print("%x"%rotate(w1,-16))
        print("%x"%rotate(w2,4))
        print("%x"%rotate(w2,-2))
        print("%x"%rotate(w1,0))
        print("%x"%rotate(w1,44))
        

#Setting top level conditional script
if __name__=='__main__':
        main()


