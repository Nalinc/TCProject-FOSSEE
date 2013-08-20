#11.9.py
#Using Pointers to Exchange Values

#Function to exchange & return values
def exchange(pint1,pint2):
         temp=pint1
         pint1=pint2
         pint2=temp
         return pint1,pint2


#Main()
def main():

        #Variable Declaration
        i1=-5
        i2=66
        p1=i1
        p2=i2

        print("i1 ={0}, i2 ={1}\n".format(i1, i2))
        
        i1,i2=exchange(p1,p2)                     #Fucntion call-1

        print("i1 ={0}, i2 ={1}\n".format(i1, i2))

        i1,i2=exchange(i1,i2)                     #Fucntion call-2

        print("i1 ={0}, i2 ={1}\n".format(i1, i2))


#Setting top level conditional script
if __name__=='__main__':
        main()



