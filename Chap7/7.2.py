#7.2.py
#Demonstrating an Array of Counters

#variable/List Declaration
ratingCounters=[0]*11

#Loop-1
for i in range(1,11):
        ratingCounters[i]=0

print("Enter your Responses:")

#Loop-2
#Clculation
for i in range (1,21):
        response=input()

        if(response<1 or response>10):
             print("Bad response: {0}".format(response))
        else:
           ratingCounters[response]+=1

#Result
print("\n\n Rating |  Number of Responses\n")
print(" -----   -------------------")

#Loop-3
for i in range(1,11):
        print("  {0}              {1}".format(i,ratingCounters[i]))




