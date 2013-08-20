#11.13.py
#Version of copyString

#Function to copy string from source to destinaton
def copyString(to, frm):
        global string2
        to=frm
        string2=to

#Main()
def main():
       
        global string2
        #String declaration
        string1="A string to be copied"
        string2=""
        copyString(string2,string1)                          #Functon call

        print("{0}\n".format(string2))
        copyString (string2, "So is this.")                  #Function call
        print("{0}\n".format(string2))

#Setting top level conditional script
if __name__=='__main__':
        main()


