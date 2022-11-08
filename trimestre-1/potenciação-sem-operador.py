def pot(x, y):
    if y == 0:
        return 1
    else:
        return x * pot(x, y-1)
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
print(pot(x, y))