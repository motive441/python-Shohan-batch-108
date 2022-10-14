# class Firstclass:
#     f_name= 'Idris'
#     m_name= 'Ali'
#     l_name= 'pk'
# shohan1 = Firstclass()
# shohan2 = Firstclass()
# shohan3 = Firstclass()
   
# print(shohan1.f_name,shohan2.m_name,shohan3.l_name)

# class Firstclass:
#     a=5
#     b=80
# stu1=Firstclass()
# stu2=Firstclass()

# print(stu1.a,stu1.b)
# print(stu2.a,stu2.b)

# class cal:
#     def add(self,a,b):
#         return a + b
# cal1 = cal()
# print(cal1.add(5,6))

# class Cal:
#     def add(self,num1,num2):
#         return num1+num2
# cl=Cal()
# a=cl.add(12,20)
# print(a)

# class cal:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mult(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
# shohan = cal()
# print(shohan.add(8,5),shohan.sub(8,5),shohan.mult(8,5),shohan.div(8,5))

# class MyCal:
#     def add(self,a,b):
#         return a+b

#     def sub(self,a,b):
#         return a-b

#     def multiplication(self,a,b):
#         return a*b

#     def division(self,a,b):
#         return a/b

# x=int(input("Enter a value for x : "))
# y=int(input("Enter a value for y : "))
# z=input("+,-,*,/or x for exit:")

# Calc1=MyCal()
# if z=='+':
#  print (Calc1.add(x,y))
# elif z=='-':
#  print (Calc1.sub(x,y))
# elif z=='*':
#  print (Calc1.multiplication(x,y))
# elif z=='/':
#  print (Calc1.division(x,y))
# elif z=='x':
#  exit()


class xty:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
object=xty(20,10)
print(object.add())
print(object.sub())
print(object.mul())




