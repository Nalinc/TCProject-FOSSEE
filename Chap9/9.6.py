#9.6.py
#Illustrating Arrays of Structures

#Import sys Library
import sys

#Class Declaration
class time:
        def __init__(self,h,m,s):
                #Variable Declarations
                self.hour=h
                self.minutes=m
                self.seconds=s
        def timeUpdate(self,now):
                #Calculation
                now.seconds+=1
                if ( now.seconds == 60):             #next minute
                        now.seconds = 0
                        now.minutes+=1   
                        if ( now.minutes == 60 ):            #next hour
                                now.minutes = 0
                                now.hour+=1;
                                if ( now.hour == 24 ):                 #  midnight
                                        now.hour = 0
        

                return now

#Main()
def main():
        #Creating instances
        testTimes = []
        testTimes.append(time(11,59,59))
        testTimes.append(time(12,0,0))
        testTimes.append(time(1,29,59))
        testTimes.append(time(23,59,59))
        testTimes.append(time(19,12,27))

        #Result
        for i in range(0,5):
               
                sys.stdout.write("Time is {0:2}:{1:2}:{2:2}  ".format(testTimes[i].hour,testTimes[i].minutes,testTimes[i].seconds))

                nextTime =testTimes[i].timeUpdate(testTimes[i])
        
        
                sys.stdout.write("...one second later it's {0:2}:{1:2}:{2:2}\n".format(testTimes[i].hour,testTimes[i].minutes,testTimes[i].seconds))



#Setting top level conditional script
if __name__=='__main__':
        main()



