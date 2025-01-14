# num=12
# print("ingresa un numero para adivinar")
# usu=int(input())
# while usu != num:
#     print("Error numero incorrecto")
#     usu=int(input("Ingresa un numero nuevamente"))
    
   
# print("Perfecto adivinaste")
from os import system 
opc=0
total=0
while True:
    print("1_arroz","2-atun")
    opc=int(input("ingresa una opcion"))
    if opc == 1:
        usu=int(input(("cuanto arroz desea llevar ")))
        total=total+usu
        exit=input("desea seguir comprando?SI/NO     ").lower()
        system("cls")
        if exit == "no":
            break
        else:
            print("ingresaste algo mal")
        
    else:
        if opc == 2:
            usu=int(input("Cuanto atun desea llevar"))
            total=total+usu
print("el total es de ",total)
            

