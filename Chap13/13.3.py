#13.3.py
#Defining global constants--advance

#Variable Declaration
global QUARTS_PER_LITER
QUARTS_PER_LITER=1.05687

#Main()
def main():
        global QUARTS_PER_LITER                         #Global Reference

        print("***Liters to galons***")
        print("Enter the number of Litres")
        liters=raw_input()

        gallons=float(liters)*QUARTS_PER_LITER/4.0      #calculation

        print("{0} Liters = {1} gallons".format(liters,gallons))

#Setting top level conditional script
if __name__=='__main__':
        main()

