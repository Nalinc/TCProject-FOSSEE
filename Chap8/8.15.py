#8.15.py
#Illustrating Static and Automatic Variables


#Function to display variables
def auto_static():
        global staticVar               #Global reference
        autoVar=1                      #variable Declaration
        print("automatic = {0}, static = {1}\n".format(autoVar,staticVar)); #Result
     
        #Calculation       
        autoVar+=1
        staticVar+=1

#Main()
def main():
        global staticVar
        staticVar=1                    #Variable Declaration
        for i in range(0,5):
                auto_static()

#Setting top level conditional script
if __name__=='__main__':
        main()


