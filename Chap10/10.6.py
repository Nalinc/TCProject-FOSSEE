#10.6.py
#Reading Lines of Data

#Main()
def main():

        #List declaration
        line=['sample text']
        for i in range(0,3):
                readLine(line)                         #Function call
                print("{0}\n".format(''.join(line)))   #Result


#Function to read user input
def readLine(line):
        
        line.pop()
        line.append(raw_input()+" ")


#Setting top level conditional script
if __name__=='__main__':
        main()



