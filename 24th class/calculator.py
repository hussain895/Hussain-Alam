class cal:
    calcul = "---------------------------------------Calculator---------------------------------------------"

    def __init__(self , num1 , num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        num = self.num1+self.num2
        print("The Addition Of num1 and num2 is = ",num)
    def sub(self):
        num3 = self.num1-self.num2
        print("The Addition Of num1 and num2 is = ",num3)
    def multiply(self):
        num4 = self.num1*self.num2
        print("The Addition Of num1 and num2 is = ",num4)
    def divide(self):
        num5 = self.num1/self.num2
        print("The Addition Of num1 and num2 is = ",num5)


a = int(input("Enter The Value = "))
b = int(input("Enter The Value = "))

calculator = cal(a,b)

print(calculator.calcul)
print(calculator.num1)
print(calculator.num2)
calculator.add()
calculator.sub()
calculator.multiply()
calculator.divide() 
