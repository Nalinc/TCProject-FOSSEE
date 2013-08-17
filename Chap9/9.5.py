#9.5.py
#Updating the Time by One Second

#Class Declaration
class time:
        def __init__(self):
                hour=0
                minutes=0
                seconds=0
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
        currentTime=time()
        nextTime=time()
        #User Input
        currentTime.hour,currentTime.minutes,currentTime.seconds=map(int,raw_input("Enter the time (hh:mm:ss):").split(':'))
        
        nextTime =currentTime.timeUpdate (currentTime);
        
        #Result
        print("Updated time is {0}:{1}:{2}\n".format(nextTime.hour,nextTime.minutes,nextTime.seconds))



#Setting top level conditional script
if __name__=='__main__':
        main()



