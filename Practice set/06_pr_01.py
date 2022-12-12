n1=int(input("Enter number1: "))
n2=int(input("Enter number2: "))
n3=int(input("Enter number3: "))
n4=int(input("Enter number4: "))

# if(n1>n2 and n1>n3 and n1>n4):
#     print("n1 is the greatest")

# elif(n2>n1 and n2>n3 and n2>n4):
#     print("n2 is the greatest")

# elif(n3>n1 and n3>n2 and n3>n4):
#     print("n3 is the greatest")

# else:
#      print("n4 is the greatest")


#Another Method

if(n1>n3):
 
    n='n1'
else:
    
    n='n3'

if(n2>n4):
    
    nn='n2'
else:
    
    nn='n4'
if(n>nn):
    print(str(n),"is the greatest")
else:
    print(str(nn),"is the greatest")

