#10.8.py
#Counting Words in a Piece of Text


#Function to read a piece of text
def readLine(line):
        
        line.pop()
        line.append(raw_input()+" ")


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



def main():
        #Variable Declaration
        totalWords=0
        endOfText=False
        text=['sample']

        print("Type in your text.\n")
        print("When you are done, press 'RETURN'.\n\n")
       
        readLine (text)
        
        #Increment Counter
        totalWords += countWords(''.join(text))
        
        #Result
        print("\nThere are {0} words in the above text.\n".format(totalWords))


#Top level conditional script
if __name__=='__main__':
        main()


