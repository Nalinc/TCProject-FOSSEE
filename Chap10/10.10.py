#10.10.py
#Modifying the Dictionary Lookup Using Binary Search

#Class Declaration
class entry:
        def __init__(self,w,d):                 #Class constructor
                self.word=w
                self.definition=d


#Function to compare two strings
def compareStrings(s1,s2):

        #Calculations
        if( s1 < s2 ):
                answer = -1;
        elif( s1 == s2 ):
                answer = 0;
        else:
                answer=1

        return answer



#Lookup function to return dictionary entry
def lookup(dictionary,search,entries):
        
        #Variable Declaration
        low=0
        high=entries-1

        #Calculations
        while(low<=high):
                mid=(low+high)/2
                result=compareStrings(dictionary[mid].word,search)

                if(result==-1):
                        low=mid+1
                elif(result==1):
                        high=mid-1
                else:
                        return mid

        return -1


#Main()
def main():

        #Variable Declaration
        entries=10
        global entry
        dictionary=[]
        
        dictionary.append(entry("aardvark","a burrowing African mammal"))
        dictionary.append(entry("abyss","a bottomless pit"))
        dictionary.append(entry("acumen","mentally sharp keen"))
        dictionary.append(entry("addle","to become confused"))
        dictionary.append(entry("aerie","a high nest"))
        dictionary.append(entry("affix","to append; attach"))
        dictionary.append(entry("agar","a jelly made from seaweed"))
        dictionary.append(entry("ahoy","nautical call of greeting"))
        dictionary.append(entry("aigrette","an ornamental cluster of feathers"))
        dictionary.append(entry("ajar","partially opened"))

        print("Enter word:")
        word=raw_input()
        entry=lookup(dictionary,word,entries)

        #Result
        if(entry!=-1):
                print("{0}".format(dictionary[entry].definition))
        else:
                print("Sorry, the word {0} is not in my dictionary.\n".format(word))


#Setting top level conditional script
if __name__=='__main__':
        main()


