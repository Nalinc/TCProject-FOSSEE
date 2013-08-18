#10.2.py
#Counting the Characters in a String


#FUnction to count number of characters ina  string
def stringLength(string):
        count = 0
        while(string[count]!='\0'):                  #Calculation
                count+=1
        return count

#Main()
def main():

        #List Declaration
        word1 = [ 'a', 's', 't', 'e', 'r', '\0' ]
        word2 = [ 'a', 't', '\0' ]
        word3 = [ 'a', 'w', 'e', '\0' ]

        #Result
        print("{0}  {1}  {2}\n".format(stringLength (word1),stringLength (word2),stringLength (word3)))


#Setting top level conditional script
if __name__=='__main__':
        main()


