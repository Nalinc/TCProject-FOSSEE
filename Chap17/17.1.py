#17.1.py
#File Copy Program Using Command-Line Arguments

#Import Libraries
import sys,string,os

def main():
        
        if(len(sys.argv)!=3):
                print("need two file names!")
                sys.exit()
       
#Read Command Line Arguments
        inName=str(sys.argv[1])
        outName=str(sys.argv[2])

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


        print("File has been copied.\n");


#Setting top level conditional script
if  __name__=='__main__':
        main()


