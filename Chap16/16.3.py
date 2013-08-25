#16.3.py
#Program to copy one file to another

#Main()
def main():

        print("Enter name of the file to be copied: ")
        inName=raw_input()
        print("Enter name of the output file: ")
        outName=raw_input()

#Try to open a file for reading
        try:
            inn=open(inName,"r")         
        except:# Exception:
                print("cant open {0} for reading".format(inName))
                sys.exit()

#try to open a file for writing
        try:
               out=open(outName,"w") 
        except:# Exception:
                print("cant open {0} for writing".format(outName))
                sys.exit()

        string=inn.read()               #Read content from File-1
        out.write(string)               #Write content to File-2

#Close Files
        inn.close()
        out.close()


#Setting top level conditional script
if __name__=='__main__':
        main()


