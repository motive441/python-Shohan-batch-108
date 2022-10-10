
# def shop_total_sale(*args):
#         print(type(args))
#         sum = 0
#         for amount in args:
#             sum = sum + amount
#             return sum 

# total_amount = shop_total_sale(54,67,23,46,78,90,11,34,56,34)

# print('Total Sale Amount : ', total_amount)


def add(**kwargs):
    print(type(kwargs))
    sum = 0
    for key in kwargs:
        sum = sum + kwargs[key]
    return sum

total = add(a=54,b=67,c=23,d=46)
print(total)