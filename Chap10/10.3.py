#10.3.py
#Concatenating Character Strings


#Function to concatinate strings
def concat(result,str1,str2):                            #Calculations
        
        #copy str1 to result
        for i in str1:
                result.append(i)
        
        #copy str2 to result        
        for j in str2:
                result.append(j)
                

#Main()
def main():

        #String Declaration
        s1 = "Test "
        s2 = "works."
        s3=[]

        concat(s3,s1,s2)                                 #Fucntion call
        print(''.join(s3))                               #Result


#Setting top level conditional script
if __name__=='__main__':
        main()

