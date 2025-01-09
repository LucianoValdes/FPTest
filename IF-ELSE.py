# print("Ingrese un numero")
# num1=int(input())
# if num1 >= 18:
#     print("Es mayor de edad")
# else:
#     print("Es menor de edad")

# print("ingrese un numero")
# num1=int(input())
# num2=int(input())
# num3=int(input())
# promedio=(num1+num2+num3)//3

# print("su promedio es", promedio)


#EJERCICIO ENTRADAS
# Total=int(input("cuantas entradas desea"))
# valor=0
# for i in range(Total):

#     print("Ingrese su edad")
#     edad=int(input())
#     if edad < 12 :
#         print("El precio de la entrada es de 500$")
#         valor=valor+500
#     else:
#         if edad >= 13 or edad <=18:
#             print("el costo de su entrada es de $1000")
#             valor=valor+1000
#         else:
#             if edad >= 19 or edad <= 64:
#                 print("el precio de su entrada es de $2000")
#                 valor=valor+2000

#             else:
#                 print("El precio de su entrada es de 700")
#                 valor=valor+700
        
# print(f"El valor total es de {valor}")

direc=input("¿Pertenece a comuna la florida?/SI-NO")
monto=5000
if direc == "si":
    print("continue con la siguiente fase")
    carnet=input("Tiene carnet de socio?").lower()
    if carnet == "si":
        int(input("Ingrese su numero de carnet"))
        print("Perfecto pase a la siguiente fase")
        jub=input("Es jubilado?").lower()
        if jub == "si":
            print("Debe pagar el monto de $5000 , pero con un descuento del 25%")
            desc=monto*0.75
            print(f"Su monto a cancelar es de{desc}")

        else:
            print("Cancele el monto")
            print(f"El monto a cancelar es de {monto}")

    else:
        print("Debe crear su carnet")
        Nombre=input("Ingrese su nombre completo")
        Rut=int(input("ingrese su rut sin guion"))
        telf=int(input("Ingrese su numero de telefono"))
        print("Carnet creado correctamente")
        int(input("Ingrese su numero de carnet"))
        print("Perfecto pase a la siguiente fase")
        jub=input("Es jubilado?").lower()
        if jub == "si":
            print("Debe pagar el monto de $5000 , pero con un descuento del 25%")
            desc=monto*0.75
            print(f"Su monto a cancelar es de{desc}")

        else:
            print("Cancele el monto")
            print(f"El monto a cancelar es de {monto}")
else:
    print("Gracias por visitar")