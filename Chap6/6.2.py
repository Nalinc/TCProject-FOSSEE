#6.2.py
#Calculating average & counting the number
#of failures from a set of grades

#Variable Declarations
gradeTotal=0
failureCount=0
i=1

#User Input
numberOfGrades=int(raw_input("How many grades will you be entering? "))

#Calculation
while(i<=numberOfGrades):
     grade=float(raw_input("enter grade {0}: ".format(i)))
     gradeTotal=gradeTotal+grade
     if(grade<65):
         failureCount=failureCount+1;
     i=i+1

average=float(gradeTotal/numberOfGrades)
      
#Result
print("Grade average= {0:.2f}".format(average))
print("Number of failures= {0}".format(failureCount))










