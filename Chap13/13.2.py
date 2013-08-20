#13.2.py
#Working more with constants

global PI
PI= 3.141592654


#Function to calculate area
def area(r):
        global PI
        return (PI*r*r)

#Function to calculate circumference
def circumference(r):
        global PI
        return (2*PI*r)

#Function to calculate volume
def volume(r):
        global PI
        return (1.33 * PI*r*r*r)
        

#Main()
def main():
        print("radius=1   {0:5}   {1:5}   {2:5}".format(area(1),circumference(1),volume(1)))
        print("radius=4.98   {0:5}   {1:5}   {2:5}".format(area(4.98),circumference(4.98),volume(4.98)))


#Setting top level conditional script
if __name__=='__main__':
        main()


