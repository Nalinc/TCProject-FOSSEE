#9.2.py
#Determining Tomorrows Date

#Main()
def main():
        #Class Declaration
        class date:
                def __init__(self):   #Class Constructor
                        #Default values
                        month=0
                        day=0
                        year=0
        #creating instances
        today=date()
        tomorrow=date()

        #List Declaration
        daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        
        today.month,today.day,today.year=map(int,raw_input("Enter today's date (mm/dd/yyyy):").split('/'))

        #Calculations
        if( today.day != daysPerMonth[today.month - 1] ):
                tomorrow.day = today.day + 1;
                tomorrow.month = today.month;
                tomorrow.year = today.year;
        elif( today.month == 12 ):
                tomorrow.day = 1;
                tomorrow.month = 1;
                tomorrow.year = today.year + 1;
        else:
                tomorrow.day = 1;
                tomorrow.month = today.month + 1;
                tomorrow.year = today.year;

        #Result
        print("Tomorrow's date is {0}/{1}/{2}\n".format(tomorrow.month,tomorrow.day,tomorrow.year));


#Setting top level conditional script
if __name__=='__main__':
        main()



