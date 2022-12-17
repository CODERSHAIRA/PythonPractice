class Number:
    def __init__(self, num):
        self.num=num

    def __add__(self,num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self,num2):
        print("Lets multiply")
        return self.num * num2.num
n1=Number(2)
n2=Number(4)
s=n1+n2
print(s)
m=n1*n2
print(m)