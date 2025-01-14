from os import system
system("cls")
def suma():
    n1=int(input("Ingrese un numero"))
    n2=int(input("Ingrese otro numero"))
    print(n1+n2)



def resta():
    n1=int(input("Ingrese un numero "))
    n2=int(input("Ingrese otro numero "))
    print(n1-n2)

def multi():
    n1=int(input("Ingrese un numero "))
    n2=int(input("Ingrese otro numero "))
    print(n1*n2)

def divi():
    n1=int(input("Ingrese un numero "))
    n2=int(input("Ingrese otro numero "))
    print(n1/n2)

while True:
    print("1-suma\n2-resta\n3-multiplicacion\n4-division")
    Op=int(input("ingrese una opcion  "))
    match Op:
        case 1:
            suma()
            usu=input("Quiere seguir haciendo operaciones? SI/NO")
            if usu == "si":
                system("cls")
            else:
                break
        case 2 :
            resta()
            usu=input("Quiere seguir haciendo operaciones? SI/NO")
            if usu == "si":
                system("cls")
            else:
                break
        case 3 :
            multi()
            usu=input("Quiere seguir haciendo operaciones? SI/NO")
            if usu == "si":
                system("cls")
            else:
                break
        case 4 :
            divi()
            usu=input("Quiere seguir haciendo operaciones? SI/NO")
            if usu == "si":
                system("cls")
            else:
                break
        case _:
            system("cls")
            print("Seleccione una opcion valida")
            
print("adios")
