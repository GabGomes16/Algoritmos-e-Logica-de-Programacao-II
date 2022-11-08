def somaLista(lista, posicao):
    tamanho = len(lista)
    resultado = 0
    if tamanho > posicao:
        resultado = lista[posicao] + somaLista(lista, posicao+1)
    else:
        return 0
    
    return resultado

lista = []
for i in range(5):
    lis = int(input("Digite o {}* número: ".format(i+1)))
    lista.append(lis)                                                                                                                                                                                                                                                                                                                                                                                                                                                             
print(somaLista(lista, 0))