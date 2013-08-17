#9.1.py
#Illustrating a Structure/Class in python

#Main()
def main():

        #Class Declaration
        class date:
                'python classes are equivalent to C structures'
                def __init__(self):                     #Class Constructor
                        #Set default values
                        self.month=0
                        self.day=0
                        self.year=0


        #Creating instance
        today=date()     
 
        #Modifying values
        today.month=9       
        today.day=25
        today.year=2004

        #Result
        print("Today's date is {0}/{1}/{2}".format(today.month,today.day,today.year%100));


#Setting top level conditional script
if __name__=='__main__':
        main()

