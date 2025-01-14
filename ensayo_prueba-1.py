
# valor=0


# print("Ingrese su edad")
# edad=int(input())
# if edad >10 :
#     print("El precio de la entrada es de 1000$")
# else:
#     if edad > 18 and edad < 65:
#         print("el costo de su entrada es de $2000")
#     else:
#         if edad > 65:
#             print("el precio de su entrada es de $1500")
#         else:
#             print("El costo de su Ticket es GRATIS")


#EJERCICIO 2 
# Valor1=int(input("Ingrese un numero"))
# Valor2=int(input("Ingrese otro numero"))
# if Valor1 > Valor2:
#     print("El numero mayor es ", Valor1)
# else:
#     print("El valor mayor es ", Valor2)

#EJERCICIO 3
# Tabla=int(input("Ingrese la tabla que desea saber"))
# for i in range(10):
#     print(Tabla,"x",i+1,"=",(Tabla)*(i+1))
                

#EJERCICIO 4
from os import system 
opc=0
total=0
nombre=input("Ingrese su nombre  ")
while True:
    print("1_arroz a la francesa \n 2-Arroz marinero \n 3-sopa marinera")
    opc=int(input("ingresa una opcion"))
    if opc == 1:
        usu=int(input(("El valor del arroz a la francesa es de $4500, cuantos desea llevar? ")))
        Total=total+usu*4500
        exit=input("desea seguir comprando?SI/NO     ").lower()
        system("cls")
        if exit == "no":
            break
        else:
            print("ingresaste algo mal")
        
    else:
        if opc == 2:
            usu=int(input(("El valor del arroz marinero es de $5200,cuantos desea llevar? ")))
            Total=total + usu*5200
            
            exit=input("desea seguir comprando?SI/NO     ").lower()
            system("cls")
            if exit == "no":
                break
            else:
                print("ingresaste algo mal")
        else:
            if opc == 3:
                usu=int(input(("El valor de la sopa marinera es de $9700, cuantos desea llevar? ")))
                Total=total + usu*9700
                
                exit=input("desea seguir comprando?SI/NO     ").lower()
                system("cls")
                if exit == "no":
                    break
                else:
                    print("ingresaste algo mal")
print("Gracias",nombre,"por venir al restorant Panuchis el total es de",Total)
            

