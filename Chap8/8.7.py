#8.7.py
#Calculating the Absolute Value

#yourstory.in

#Calculations
def absoluteValue(x):                              #Function to calculate & return absolute values
        if(x<0):
           x=-x
        return x

def main():                                         #Main() Function
    
        f1=-15.5
        f2=20.0
        f3=-5.0
        il=-716
#Result    
        result=absoluteValue(f1)
        print("result= {0:.2f}".format(result))
        print("f1={0:.2f}".format(f1))

        result=absoluteValue(f2)+absoluteValue(f3)
        print("result= {0:.2f}".format(result))

        result=absoluteValue(float(il))
        print("result= {0:.2f}".format(result))
                
        result=absoluteValue(il)
        print("resut= {0:.2f}".format(result))

        print("{0:.2f}".format(absoluteValue((-6.0)/4)))


#End of Main()
 
if __name__=='__main__':                                    #Setting Top level conditional script
    main()

