fn = 0

def fibo(n):
    if n > 2:
        fn = fibo(n-1) + fibo(n-2)
    else:
        return 1
    return fn

def fat(n):
    f = 1
    print("{}! = ".format(n), end="")
    for i in range(n, 0, -1):
        print(i, " X " if i != 1 else " = ", end="")
        f *= i
    return f