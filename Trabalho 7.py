def func1(a):
    return sum(a), sum(a)/len(a)

def func2(a, b, c):
    for indice in range(len(a)):
        if a[indice] == b:
            a[indice] = c
            return a

def func3(num_linhas):
    for i in range (1, num_linhas + 1):
        print('*' * i)
