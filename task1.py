#с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено положительных
# и сколько отрицательных чисел.
x = int(input())
a = 0
b = 0
while (x!=0):
    if x > 0:
        a = a+1
    else:
        b = b+1
    x = int(input())
print (a, b)
