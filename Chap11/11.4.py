#11.4.py
#Using Pointers to classes

#Main()
def main():
        class date:
                def __init__(self):             #Class constructor
                        self.month=0
                        self.day=0
                        self.year=0

        #Creating instances
        today=date()
        datePtr=today

        datePtr.month=9
        datePtr.day=25
        datePtr.year=2004

        #Result
        print("Today's date is {0}/{1}/{2}".format(datePtr.month, datePtr.day, datePtr.year))

#Setting top level conditional script
if __name__=='__main__':
        main()


