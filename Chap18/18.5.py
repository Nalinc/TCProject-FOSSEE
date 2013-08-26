#18.5.py
#Working more with pdb

#Class Declaration
class date:
        def __init__(self,m,d,y):               #Class constructor
                self.month=m
                self.day=d
                self.year=y

        def foo(x):
                x.day+=1
                return x

#Main()
def main():

        #Variable Declaration
        today=date(10,11,2004)
        array=[1,2,3,4,5]
        string="test string"
        i=3
        newdate=date(11,15,2004)
        today=date.foo(today)

        #Result
        print("today= %d/%d/%d"%(today.day,today.month,today.year))


#Setting top level conditional script
if __name__=='__main__':
        main()



