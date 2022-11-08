def mdc(maior):
    if x % maior == 0 and y % maior == 0:
        result = maior
        return result
    else:
        return mdc(maior-1)
    
x = int(input("Digite o primeiro número para o cálculo: "))
y = int(input("Digite o segundo número para o cálculo: "))
maior = max(x, y)
print(mdc(maior))