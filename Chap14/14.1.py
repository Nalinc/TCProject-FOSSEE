#14.1.py
#Using Enumerated Data Type

#Main()
def main():

        #Declaring an Enumerator 
        def enum(**enums):
                return type('Enum',(),enums)

        #Defining an Enumerator
        month=enum(january=1,february=2,march=3,april=4,may=5,june=6,july=7,\
                   august=8,september=9,october=10,november=11,december=12)
        days=0

        print("Enter month number:")
        aMonth=raw_input()

        #Calculations
        if(int(aMonth)==month.january or int(aMonth)==month.march or \
           int(aMonth)==month.may or int(aMonth)==month.july or \
           int(aMonth)==month.august or int(aMonth)==month.october or int(aMonth)==month.december):
                days=31

        elif(int(aMonth)==month.april or int(aMonth)==month.june or \
             int(aMonth)==month.september or int(aMonth)==month.november):
                days=30
        elif(int(aMonth)==month.february):
                days=28
        else:
                print("bad month number")
                days=0

        #Result
        if(days!=0):
                print("Number of days is {0}".format(days))
        if(int(aMonth)==month.february):
                print("...or 29 if it's a leap year")


#Top level conditional script
if __name__=='__main__':
        main()


