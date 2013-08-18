#10.9.py
#Using the Dictionary Lookup Program

#Class Declaration
class entry:
        def __init__(self,w,d):
                self.word=w
                self.definition=d


#Function to check equality of two strings
def equalStrings(str1,str2):
        if(str1==str2):
                return True
        else:
                return False

#Lookup function to return dictionary entry
def lookup(dictionary,search,entries):
        for i in range(0,entries):
                if ( equalStrings(search, dictionary[i].word) ):
                        return i;
        return -1;

#Main()
def main():

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


