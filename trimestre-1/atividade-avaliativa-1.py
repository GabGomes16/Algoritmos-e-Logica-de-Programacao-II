continuar=1
while continuar == 1:
    quest=1


    def fim(continuar):
        cond = str(input("**********DESEJA CONTINUAR?**********\n(S) para sim\n(N) para não\n\n"))
        if cond == "n":
            continuar-=1
        return continuar


    def q1():
        print("\33[1;31mEscreva um algoritmo que imprima todos os números pares no intervalo aberto ]1..20[, ou seja, a saída é: 2, 4, 6, ..., 18.\nÉ obrigatório o uso de repetição.")
        
        print("\033[1;97mNúmeros pares até 20")
        n=0
        for n in range(1,20):
            if n % 2 == 0 :
                print(n, end='\n') 
        fim(continuar)


    def q2():
        print("\033[31mEscreva um programa que receba uma palavra e uma letra do teclado.\nTal função deve contar quantas vezes a letra aparece na palavra e retornar o valor. Obs: Não podem utilizar função count. Utilize o FOR.")
        
        print("\033[1;97mCONTADOR DE LETRAS\n") 
        word= str(input("Digite uma palavra: \n"))
        letter = str(input("Digite qual letra quer saber a quantidade: "))
        quant = 0
        for l in word:
            if (l == letter):
                quant = quant + 1
        print(quant) 
        fim(continuar)


    def q3():
        print("\033[31mImplemente um programa que leia 3 nomes e imprima a palavra formada pelas duas primeiras letras de cada um dos nomes.\nOs nomes devem ser armazenados em uma lista. Obs: A ordem dos fatores altera o produto")
        
        print("\033[1;97mJUNTA NOMES")
        nomes=[]
        novo=""
        for i in range(3):
            nome=input("Digite o nome %d: "%(i+1))
            nomes.append (nome)
        print (nomes)
        for nome in nomes:
            novo=novo+nome [0] +nome [1]
        print (novo) 
        fim(continuar)


    def q4():
        print("\033[31mUm professor possui 2 turmas, e cada turma possui 10 alunos.\nConstrua um algoritmo que leia a nota dos alunos de cada uma das turmas e exiba a media das notas por turma.")

        print("\033[1;97mMEDIA DAS NOTAS")
        notas=[]
        for turma in range(2):
            notas.append([0]*10)
        for turma in range(2):
            print("Prcencha as notas da turma ", turma+1)
            for aluno in range(10):
                print("nota do aluno ", aluno+1, end=": ")
                notas [turma] [aluno] = float(input())
        for turma in range(2):
            soma=0
            for aluno in range(10):
                soma = soma + notas [turma] [aluno]
            print("Média da turma ",turma+1,": ",soma/len(notas [turma])) 
        fim(continuar)


    def q5():
        print("\033[31mExplique como funciona a função range.")

        print("\033[1;97mA função range() permite gerar sequencias de valores em progressão aritmética e nos permite especificar o início da sequência, o passo, e o valor final.\nO único parâmetro obrigatório é o que define quem será o último elemento da sequência.")
        fim(continuar)


    def q6():
        print("\033[31mDiferencie o WHILE do FOR e exemplifique o uso de cada um dels com um código.\n")

        print("\033[1;97mO for é usado quando se quer iterar sobre um bloco de código um número determinado de vezes.\nO while é usando quado queremos que o bloco de código seja repetido até que uma condição seja satisfeita.\n****************EXEMPLOS NO CODIGO****************")
        # ***************************************************************
        # quant=int(input("quantidade: "))
        # for i in range(quant):
        #     print(i)
        
        # t=5
        # while t != 0:
        #     print(t)
        #     t-=1
        # ***************************************************************
        fim(continuar)


    def q7():
        print("\033[31mQual a diferença entre usaar list e numpy para definir vetores em python?")

        print ("\033[1;97mNumpy é uma biblioteca para computação cientifica em Python, para utilizá-la é necessário importá-la. Essa biblioteca \n fornece alto desempenho e ferramentas para manipulação de arrays multidiminesionais. Um array Numpy deve ser composto \n por elementos do mesmo tipo. Já uma lista (list) é nativa do Python, ou seja, não é necessário que uma biblioteca seja \n importada para ela ser utilizada. Além disso, uma lista em Python é equivalente a um array, mas é redimensionável \n e pode conter elementos de diferentes tipos. Vejam o exemplo abaixo para somar duas matrizes.\n")
        print ("- Programa para somar duas matrizes utilizando listas")

        x = [[12,7,3],
            [4,5,6],
            [7,8,9]]
        y = [[5,8,1],
            [6,7,3],
            [4,5,9]]
        result =    [[0,0,0],
                    [0,0,0],
                    [0,0,0]]
        
        for i in range (len(x)):
            print (x[i])
            
            for j in range (len(x[i])):
                result [i][j] = x[i][j] + y [i][j]
        for r in  result:
            print (r)

        print ("- Programa para somar duas matrizes utilizando Numpy")
        import numpy as np
        A = np.array ([[2,4], [5,-6]])
        B = np.array ([[9,-3],[3,6]])
        print ("A: ", A)
        print ("B: ", B)
        C = A + B
        print ("C: ", C)
        fim(continuar)


    def q8():
        print("\033[31mQual a diferença conceitual entre vetores e matrizes? Exemplifique o uso de cada um deles com um código em python.")

        print ("\033[1;97mVetores e matrizes são coleções de variáveis continuas na memória e acessadas por meio de um número de índice. A diferença entre vetores e matrizes é que vetores são de uma única dimensão, enquanto matrizes podem conter várias dimensões. \n")
        print ("- Programa com vetor\n")

        #Numeros ímpares com Numpy em um array de única dimensão
        import numpy as np

        arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
        arr[arr % 2 == 1]

        print ("- Programa com matrizes\n")

        #Importando Numpy para operações de matrizes 
        import numpy

        #Inicialização de matrizes de duas dimensões
        x = numpy.array([[1, 2], [4, 5]])
        y = numpy.array([[7, 8], [9, 10]])

        #Uso do add() para adicionar
        print ("Adição de cada elemento da matriz: ") 
        print (numpy.add(x,y))

        #Uso do subtract() para subtrair
        print ("Subtração de cada elemento da matriz: ") 
        print (numpy.subtract(x,y))

        #Uso do divide() para dividir
        print ("Divisão de cada elemento da matriz: ")
        print (numpy.divide(x,y))

        #Uso do multiply() para multiplicar cada elemento 
        print ("Multiplicação de cada elemento da matriz: ") 
        print (numpy.multiply(x,y))
        fim(continuar)


    quest=int(input('\033[1;33mQUAL QUESTÃO DESEJA EXECUTAR?\n\033[1;97mDigite um número de 1-8 para acessar a questão: '))
    if quest == 1:
        q1()
    elif quest == 2:
        q2()
    elif quest == 3:
        q3()
    elif quest == 4:
        q4()
    elif quest == 5:
        q5()
    elif quest == 6:
        q6()
    elif quest == 7:
        q7()
    elif quest == 8:
        q8()
    else:
        print("\033[31mERRO")
            
