#6.7.py
#Implementing the Sign Function

#Variable declaration/User input
ch=raw_input("Enter a single character: ")

#Calculation/Result
if((ch>='a' and ch <='z') or (ch>='A' and ch<='Z')):
     print("It's an alphabetic character.")
elif(ch>='0'and ch<='9'):
     print("It's a digit.")
else:
     print("It's a special character")



