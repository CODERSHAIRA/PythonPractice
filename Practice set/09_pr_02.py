class Calculator:
    
    def __init__(self,num):
       self.number=num
                
    def square(self):
       print(f"The value of {self.number} square is {self.number **2}")

    def cube(self):
       print(f"The value of {self.number} square is {self.number **3}")

    def squareRoot(self):
       print(f"The value of {self.number} square is {self.number **(1/2)}")
    
    @staticmethod
    def greet():
        print("Hello user!")


c= Calculator(25)
c.square()
c.cube()
c.squareRoot()
c.greet()


    