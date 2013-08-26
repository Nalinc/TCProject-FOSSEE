#18.1.py
#Adding Debug statements in program

#Program logs will be saved in file- 18.1_logFile.txt

#Import library
import logging

#Function to return sum of 3 numbers
def process(i,j,k):
        return i+j+k

#Main()
def main():

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        fh = logging.FileHandler('18.1_logFile.txt')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        arr=[]
        arr=map(int,"1 2 3".split())
        #arr=map(int,raw_input().split())
        logger.debug("Number of integers read= {0}".format(len(arr)))               #Debug statement
        logger.debug("i = {0}, j = {1}, k = {2}\n".format(arr[0],arr[1],arr[2]))    #Debug statement

        print("sum= %i\n"%process(arr[0],arr[1],arr[2]))


#Setting top level conditional script
if __name__=='__main__':
        main()


