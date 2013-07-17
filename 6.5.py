#6.5.py
#Determining if a Year Is a Leap Year

#Variable declaration/User input
year=int(raw_input("Enter the year to be tested: "))

#Calculations
rem_4=year%4
rem_100=year%100
rem_400=year%400

#Result
if((rem_4==0 and rem_100!=0)or rem_400==0):
    print("Woah! Its a leap year.")
else:
    print("Whoops! Its not a leap year.\n")
