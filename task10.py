# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".


M = 1
m = 10**12
def f(x):
    if(x == 1):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True

c = int(input())
for i in range(1, c+1):
    n = int(input())

    if f(n)==True:
        if n>M:
            M=n
        if n<m:
            m=n


if m == 10**12 and M == 1:
    print("нет")
else:
    print (m, M)