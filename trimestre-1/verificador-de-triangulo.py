def formaTriang(a,b,c):
    if sub1 < a < b+c or sub2 < b < a+c or sub3 < c < a+b:
        return True
    else:
        return False

def qualTriang(triang):
        if a == b and b == c:
            print("Esse é um TRIÂNGULO EQUILATERO")
        elif a != b and b != c and a!= c:
            print("Esse é um TRIÂNGULO ESCALENO")
            print(f"O maior lado mede: {max(a,b,c)}")
        elif a == b and b != c or b == c and c != a or a == c and c != b:
            print("Esse é um TRIÂNGULO ISÓRCELES")
            print(f"O maior lado mede: {max(a,b,c)}")

a = int(input("Digite o tamanho do primeiro lado: "))
b = int(input("Digite o tamanho do segundo lado: "))
c = int(input("Digite o tamanho do terceiro lado: "))
sub1 = a-b
sub2 = a-c
sub3 = b-c
triang = formaTriang(a,b,c)
if triang == True:
    print(qualTriang(formaTriang))
else:
    print("Não é triangulo  :[")