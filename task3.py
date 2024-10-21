# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.


def f(x):
    if(x == 1):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True
a=0
b=0
x=int(input())
while (x!=0):
    if f(x)==True:
        a+=1
    else:
        b+=1
    x=int(input())


print (a,b)