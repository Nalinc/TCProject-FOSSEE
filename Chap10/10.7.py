#10.7.py
#Counting Words

#Function to determine if a character is alphabetic
def alphabetic(c):
        if ( (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') ):
                return True
        else:
                return False


#Function to count the number of words in a string
def countWords(string):
        
        #Variable Declaration
        wordCount=0
        lookingForWord=True
        
        #Calculations
        for i in string:
                if(alphabetic(i)):
                        if(lookingForWord):
                                wordCount+=1
                                lookingForWord=False
                else:
                        lookingForWord=True
        return wordCount


#Main()
def main():

        #String Declaration
        text1 = "Well, here goes."
        text2 = "And here we go... again."
        
        #Result
        print("{0} - words = {1}\n".format(text1,countWords(text1)))
        print("{0} - words = {1}\n".format(text2,countWords(text2)))


#Setting top level conditional script
if __name__=='__main__':
        main()


