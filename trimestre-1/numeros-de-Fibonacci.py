def fibo(n):
    if n > 2:
        fn = fibo(n-1) + fibo(n-2)
    else:
        return 1
    return fn

n = int(input("Digite quantos números da sequência você quer: "))
fn = 0
print(fibo(n))