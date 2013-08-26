#18.4.py
#A simple program for use with pdb(gdb like python debugger)

#Main()
def main():
        
        #Variable Declaration
        sum=0
        data = [1, 2, 3, 4, 5]

        #Calculation
        for i in range (0,5):
                sum += data[i]
        
        #Result
        print("sum = %i\n"%(sum))
        

#Setting top level conditional script
if __name__=='__main__':
        main()


