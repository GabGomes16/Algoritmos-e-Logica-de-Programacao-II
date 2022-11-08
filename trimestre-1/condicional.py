n=int(input("Digite um número de 1 a 9: \n"))
if n > 0 and n < 4:
    n **= 2
    print (n)
elif n == 4 or n == 9:
    n *= 2
    print(n)
elif n >= 6 and n < 9:
    n = n/9
    print (n)
else:
    print (n)