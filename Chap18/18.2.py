#18.2.py
#Compiling in Debug 

#Program logs will be saved in file- 18.2_logFile.txt

#Import Libraries
import logging,sys

#Function to return product of two numbers
def process(i1,i2):

        global logger 
        logger.debug("process (%i, %i)\n"%(i1, i2))
        val=i1*i2
        logger.debug("return %i\n"%(val))
        return val


#Main()
def main():

        global logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        fh = logging.FileHandler('18.2_logFile.txt')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)


        arg1=0
        arg2=0
        if(len(sys.argv)>1):
                arg1=int(sys.argv[1])
        if(len(sys.argv)==3):
                arg2=int(sys.argv[2])

        a=['3','5']
        logger.debug("processed %i arguments\n"%(len(a)))
        #logger.debug("processed %i arguments\n"%(len(sys.argv)))

        logger.debug("arg1 = %i, arg2 = %i\n"%(int(a[0]), int(a[1])))
        print("product = %i\n" %( process (int(a[0]),int( a[1]))))

        #logger.debug("arg1 = %i, arg2 = %i\n"%(arg1, arg2))
        #print("product = %i\n" %( process (arg1, arg2)))


#Setting top level conditional script
if __name__=='__main__':
        main()


