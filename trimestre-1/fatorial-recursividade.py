def fat(n):
    if (n > 1):
        return n * fat(n-1)
    else:
        return 1
n = int(input("CÁLCULO DE FATORIAL\nDigite um número: "))
print (fat(n))