#9.7.py
#Illustrating Structures and Arrays


#Main()
def main():
        #Class Declaration
        class month:
                def __init__(self,n,na):                 #Class Constructor
                        self.numberOfDays=n
                        self.name=na

        #List Declaration
        months=[]
        months.append(month(31,['j','a','n']))
        months.append(month(28,['f','e','b']))
        months.append(month(31,['m','a','r']))
        months.append(month(30,['a','p','r']))
        months.append(month(31,['m','a','y']))
        months.append(month(30,['j','u','n']))
        months.append(month(31,['j','u','l']))
        months.append(month(31,['a','u','g']))
        months.append(month(30,['s','e','p']))
        months.append(month(31,['o','c','t']))
        months.append(month(30,['n','o','v']))
        months.append(month(31,['d','e','c']))
        
        
        #Result
        print("Month     NumberOfDays")
        print("-----     ------------")
        for i in range (0,12):
                 print("{0}{1}{2}           {3}\n".format(months[i].name[0],months[i].name[1],months[i].name[2], months[i].numberOfDays))


#Setting top level conditional script
if __name__=='__main__':
        main()


