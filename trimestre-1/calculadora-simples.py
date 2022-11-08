def opera(x,y,oper):
    if oper == "+":
        z = x+y
    elif oper == "-":
        z = x-y 
    elif oper == "*":
        z = x*y 
    elif oper == "/":
        if y != 0:
            z = x/y
        else:
            z = None
    else:
        z = None
    return z

x = int(input("Digite o primero número: "))
y = int(input("Digite o segundo número: "))
oper = str(input("Escolha a operação:\n(+) para SOMA\n(-) para SUBTRAÇÃO\n(*) para MULTIPLICAÇÃO\n(/) para DIVISÃO\n          "))
if (opera(x,y,oper)) == None:
    print("ERRO")
else:
    print(opera(x,y,oper))