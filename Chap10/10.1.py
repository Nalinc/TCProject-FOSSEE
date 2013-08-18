#10.1.py
#Concatenating Character Arrays

#Import system library
import sys

#Function to concatinate strings
def concat(result,str1,n1,str2,n2):                 #Calculations
        
        #copy str1 to result
        for i in range(0,n1):
                result[i]=str1[i]
        
        #copy str2 to result        
        for j in range(0,n2):
                result[n1+j]=str2[j]


#Main()
def main():

        #List Declaration
        s1 = [ 'T', 'e', 's', 't', ' ']
        s2 = [ 'w', 'o', 'r', 'k', 's', '.' ]
        s3=[0]*11

        concat(s3,s1,5,s2,6)                        #Fucntion call

        for i in range(0,11):                       #Result
                sys.stdout.write("{0}".format(s3[i]))

        sys.stdout.write("\n")


#Setting top level conditional script
if __name__=='__main__':
        main()

