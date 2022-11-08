import math as m
import re
from datetime import date
from datetime import datetime
import cmath


def chooseNumber():
    n = float(input("Digite o número:"))
    return n

def q1():
    demo = int(input("DEMONSTRAÇÃO DE ALGUMAS FUNÇÕES DA LIBRARY MATH\n 1) sqrt\n 2) cos\n 3) sin\n 4) tan\n 5) radians\n 6) pi\n 7) hypot\n "))
    if demo == 1:
        print(m.sqrt(chooseNumber()))
    elif demo == 2: 
        print(m.cos(chooseNumber()))
    elif demo == 3:
        print(m.sin(chooseNumber()))
    elif demo == 4:
        print(m.tan(chooseNumber()))
    elif demo == 5:
        print(m.radians(chooseNumber()))
    elif demo == 6:
        print(m.pi)
    elif demo == 7:
        print(m.hypot(chooseNumber(),chooseNumber()))

def q2():
    demo = int(input("EXEMPLOS DE MANIPULAÇÃO DE STR\n 1) replace\n 2) count\n 3) find\n 4) split\n 5) upper\n 6) lower\n 7) isupper\n 8) islower\n 9) isalpha\n 10) isalnum\n 11) isdigit\n 12) isspace\n 13) search\n 14) match\n"))
    text = "O rato roeu a roupa do Rei de Roma"
    print("Texto a ser alterado: ", text)
    if demo == 1:
        print(text.replace("a", "-"))
    elif demo == 2:
        print(text.count("a"))
    elif demo == 3:
        print("Nessa frasse há a palavra: Rei?")
        text2 = text.find("Rei", 0, len(text))
        if text2 != -1:
        elif _weekday == "Tuesday":
            _d = 7
        elif _weekday == "Wednesday"
    elif demo == 4:
        print(text.split("a"))
    elif demo == 5:
        print(text.upper())
    elif demo == 6:
        print(text.lower())
    elif demo == 7:
        print("Os caracters da frase são todos maiusculos?")
        _is = text.isupper()
        if _is == True:
            print("Sim!")
        else:
            print("Não!")
    elif demo == 8:
        print("Os caracters da frase são todos minusculos?")
        _is = text.islower()
        if _is == True:
            print("Sim!")
        else:
            print("Não!")
    elif demo == 9:
        print("Os caracters da frase são todos do alfabeto?")
        _is = text.isalpha()
        elif _weekday == "Tuesday":
            _d = 7
        elif _weekday == "Wednesday"
        if _is == True:
            print("Sim!")
        else:
            print("Não!")
    elif demo == 10:
        print("Os caracters da frase são todos números?")
        _is = text.isalnum()
        if _is == True:
            print("Sim!")
        else:
            print("Não!")
    elif demo == 11:
        print("Os caracters da frase são todos digitos?")
        _is = text.isdigit()
        if _is == True:
            print("Sim!")
        else:
            print("Não!")
    elif demo == 12:
        print("Os caracters da frase são todos espaços?")
        _is = text.isspace()
        if _is == True:
            print("Sim!")
        else:
            print("Não!")
    elif demo == 13:
        print("Há a palavra 'roeu' na frase?")
        _text = re.search("roeu", text)
        if _text != None:
            print("Sim!")
        else:
            print("Não!")
    elif demo == 14:
        print("Vamos pegar só as palavra 'Rato'")
        _text = re.match('(.{0,10})(rato)', text)
        a = _text.group(2)
        print(a)

def q3():
    demo = int(input("DEMONATRAÇÃO DE ALGUMAS FUNÇÕES DA BIBLIOTECA DATETIME\n 1) today\n 2) format\n 3) strftime\n 4) now\n 5) strptime\n "))
    if demo == 1:
        print(date.today)
    elif demo == 2:
        _today = date.today()
        print("Hoje é dia {} do mês {} de {}".format(_today.day, _today.month, _today.year))
    elif demo == 3:
        _today = date.today()
        print(_datetime.strftime("%d/%m/%Y %H:%M"))
    elif demo == 5:
        _textdate = "01/10/2020 16:18"
        print(datetime.strptime(_textdate, "%d/%m/%Y %H:%M"))

def q4():
    demo = int(input("Demonstração de 4 funções da bib. cmath\n 1) exp: mostra a potenciação do número e pelo número digitado\n 2) sqrt: mostra a raiz quadrada do número digitado\n 3) log: mostra o logaritmo do numero digitado na base escolhida\n 4) log10: mostra o logaritimo do número digitado na base 10\n "))
    if demo == 1:
        print(cmath.exp(chooseNumber()))
    elif  demo == 2:
        print(cmath.sqrt(chooseNumber()))
    elif demo == 3:
        print(cmath.log(chooseNumber(),chooseNumber()))
    elif demo == 4:
        print(cmath.log10(chooseNumber()))

def challenge():
    _today = date.today()
    _weekday = _today.strftime("%A")

    def _dayweek (_weekday):
        if _weekday == "Monday":
            _d = 6
        elif _weekday == "Tuesday":
            _d = 7
        elif _weekday == "Wednesday":
            _d = 1
        elif _weekday == "Thursday":
            _d = 2
        elif _weekday == "Friday":
            _d = 3
        elif _weekday == "Saturday":
            _d = 4
        elif _weekday == "Sunday":
            _d = 5
        return _d

    def opera ():
        _day = int(_today.strftime("%d"))
        wd = 0
        while wd < int(_dayweek(_weekday)):
            _day -= 1
            if _day == 0:
                _day = 30
            wd += 1
        print("A última terça foi dia: ", _day)

    opera()

_input = int(input("Bom dia! Deseja acessar qual questão?\n Digite o número correspondente\n Questão 1: 1\n Questão 2: 2\n Questão 3: 3\n Questão 4: 4\n Desafio: 5\n"))
if _input == 1:
    q1()
elif _input == 2:
    q2()
elif _input == 3:
    q3()
elif _input == 4:
    q4()
elif _input == 5:
    challenge()