
# def my_sale(*args):
#     sale=0
#     for i in args:
#         sale=sale+i
#     return sale

# print ('Total sale : ', my_sale(10,5,5,50))   
# print ('Total sale : ', my_sale(10,5,15))   
# print ('Total sale : ', my_sale(15,2,3,25,14,1))

# def add(**kwargs):
#     sum=0
#     for key in kwargs:
#         sum=sum+kwargs[key]
#     return sum

# total=add(a=45,b=48,c=23)
# print(total)



# def shop_total_sale(*args):
#         print(type(args))
#         sum = 0
#         for amount in args:
#             sum = sum + amount
#             return sum 

# total_amount = shop_total_sale(54,67,23,46,78,90,11,34,56,34)

# print('Total Sale Amount : ', total_amount)


# def add(**kwargs):
#     print(type(kwargs))
#     sum = 0
#     for key in kwargs:
#         sum = sum + kwargs[key]
#     return sum

# total = add(a=54,b=67,c=23,d=46)
# print(total)

x=input("Enter a value for x : ")
y=input("Enter a value for y : ")

z=input("Options are (+-*/ or x for exit) : ")
while (z!=0):
  if (z=='+'):
    print(int(x)+int(y))
  elif(z=='-'):
    print(int(x)-int(y))
  elif(z=='*'):
    print(int(x)*int(y))
  elif(z=='/'):
    print(int(x)/int(y))
  elif (z=='x'):
    exit()
  z=input("Options are (+-*/ or x for exit) : ")
