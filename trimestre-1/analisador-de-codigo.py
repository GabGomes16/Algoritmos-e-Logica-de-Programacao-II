print("**********SUPERMERCADO**********\n")
cod = 1
prod = ""

def classif(cod):
    if cod == 1:
        prod = "Alimento não perecível"
    elif cod > 1 and cod < 5:
        prod = "Alimento perecível"
    elif cod >=5 and cod < 7:
        prod = "Vestuário"
    elif cod == 7:
        prod = "Higiene pessoal"
    elif cod > 7 and cod < 16:
        prod = "Limpeza e utensílios domésticos"
    else:
        prod = "CÓDIGO INVALIDO"
    return prod


while cod != 0:
    print("APERTE *0* PARA ENCERRAR\n")
    cod = int(input("DIGITE O CÓDIGO DE SEU PRODUTO: "))
    if cod > 0:
        print(f"O produto é: {classif(cod)}\n\n")
print("TENHA UM BOM DIA!   :]")
