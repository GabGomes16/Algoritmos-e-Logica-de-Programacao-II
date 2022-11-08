n = int(input("CÁLCULO DE FATORIAL\nDigite um número: "))
f = 1
print("{}! = ".format(n), end="")
for i in range(n, 0, -1):
    print(i, " X " if i != 1 else " = ", end="")
    f *= i
print(f)