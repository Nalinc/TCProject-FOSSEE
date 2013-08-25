#16.1.py
#Illustrating print function

#Main()
def main():

        #Variable Declaration
        c='X'
        s="abcdefghijklmnopqrstuvwxyz"
        i=425
        j=17
        u=0xf179
        l=75000
        L=0x1234567812345678
        f=12.978
        d=-97.4583
        cp=c
        ip=i
        

        #Print Integers
        print("Integers:\n")
        print("%i %o %x %u" %(i,i,i,i))
        print("%x %X %#x %#X" %(i,i,i,i))
        print("%+i % i %07i %.7i" %(i,i,i, i))
        print("%i %o %x %u" %(j,j,j,j))
        print("%i %o %x %u" %(u,u,u,u))
        print("%ld %lo %lx %lu" %(l,l,l,l))
        print("%li %lo %lx %lu" %(L,L,L, L))

        #Print Floats & Doubles
        print("\nFloats and Doubles:")
        print("%f %e %g"%( f, f, f))
        print("%.2f %.2e"%( f, f))
        print("%.0f %.0e"%( f, f))
        print("%7.2f %7.2e"%( f, f))
        print("%f %e %g"%( d, d, d))
        print("%.*f"%( 3, d))
        print("%*.*f" %(8, 2, d))

        #Print Characters
        print("\nCharacters:")
        print("%c"%(c))
        print("%3c%3c"%( c, c))
        print("{0:x} ".format(ord(c))) 

        #Print Strings
        print("\nStrings:")
        print("%s"%(s))
        print("%.5s"%(s))
        print("%30s"%(s))
        print("%20.5s"%(s))
        print("%-20.5s"%(s))

        #Print variables pointers
        print("\nPointers:")
        print("{0:x} {1:x}\n".format(int(ip),ord(cp)))

        print("This%n is fun.")
        print("c1 = %i, c2 = %i\n"%(4, 12))


#Setting top level conditional script
if __name__=='__main__':
        main()


