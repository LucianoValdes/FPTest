#TRY , EXCEPT
from os import system
system("cls")
deuda=100000
while True:
    print("1-Pago de Tarjeta de credito\n2-Simulacion de compras\n3-Salir")
    opc=int(input("Ingrese una opcion  "))
    match  opc:
        case 1:
            print("Usted posee una deuda de",deuda)
            usu=int(input("ingrese un monto para pagar la deuda "))
            Total=deuda-usu
            if usu >= 1 and usu <=100000:
                system("cls")
                print("Valor ingresado correctamente el total de su deuda ahora es de ",Total)
                
            else:
                if usu <= 0:
                    print("No puede ingresar un valor menor o igual a 0 ")
                else:
                    try:
                        if usu > 100000:
                            print("No puede ingresar un valor mayor a su deuda")
                    except:
                        print("Ingresaste un valor erroneo, vuelve a intentarlo")
        case 2:
            
                compra=int(input("Ingrese el valor de la compra que desea realizar "))
                
                Total=Total+compra
                deuda=Total
                
                if compra > 0:
                    system("cls")
                    print("Perfecto su tarjeta de credito tiene ahora un valor de",deuda)
                    
            
        case 3:
            print("El valor actualizado de su tarjeta es de ",Total)
            

                
            



    
                

