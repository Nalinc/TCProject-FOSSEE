#19.1.py
#Working with fractions in python

#Class declaration
class Fraction:
        def __init__(self):                     #Class constructor
                self.numerator=0
                self.denominator=0

#Main()
def main():

        #Creating instance
        myFract=Fraction()
        myFract.numerator=1
        myFract.denominator=3

        print("The Fraction is {0}/{1}".format(myFract.numerator,myFract.denominator))

#Setting top level conditional script
if __name__=='__main__':
        main()


