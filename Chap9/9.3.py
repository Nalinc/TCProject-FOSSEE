#9.3.py
#Revising the Program to Determine Tomorrow's Date

#Class Declaration
class date:
        def __init__(self):   #Class Constructor
                #Default values
                month=0
                day=0
                year=0
 

#Main()
def main():
       #creating instances
        today=date()
        tomorrow=date()

       
        today.month,today.day,today.year=map(int,raw_input("Enter today's date (mm/dd/yyyy):").split('/'))

        #Calculations
        if( today.day != numberOfDays(today) ):
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


#Function to find the number of days in a month        
def numberOfDays(d):
        
        #List Declaration
        daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        if(isLeapYear(d)==True and d.month==2):
                days=29
        else:
                days = daysPerMonth[d.month - 1];

        return days


#Function to determine if it's a leap year
def isLeapYear(d):
        if ( (d.year % 4 == 0 and d.year % 100 != 0) or  d.year % 400 == 0 ):
                leapYearFlag = True        # Its a leap year
        else:
                leapYearFlag = False       # Not a leap year
        
        return leapYearFlag;



#Setting top level conditional script
if __name__=='__main__':
        main()



