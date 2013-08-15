#8.12.py
#

#Import system Library 
import sys

#Function to sort the array
def sort(a,n):

        for i in range (0,n-1):                          #Calculations
                for j in range (i+1,n):
                        if(a[i]>a[j]):                   #Conditional swapping
                                temp=a[i]
                                a[i]=a[j]
                                a[j]=temp

#Main()
def  main():

        #List/Variable Declaration 
        array= [ 34, -5, 6, 0, 12, 100, 56, 22,\
                      44, -3, -9, 12, 17, 22, 6, 11 ]
        
        print("The array before the sort:\n");
        for i in range (0,16):
                sys.stdout.write("{0} ".format(array[i]))
        
        sort (array, 16);                                #Function Call
        
        print("\n\n\nThe array after the sort:\n")
        for i in range (0,16):
                sys.stdout.write("{0} ".format(array[i]))
        print("\n")


#Setting top level conditional script        
if  __name__=='__main__':
        main()



