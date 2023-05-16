#7. Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará,
# la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.    
# Si ingresa un monto negativo, no se debe procesar
# Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1,000,000.00, se le debe aplicar un 10% de descuento.

totalPagar = 0
descuento = 0

pedirMasMontos = True
while pedirMasMontos:
    monto = int(input("Ingrese Monto del producto: "))

    if monto == 0:
        pedirMasMontos = False
    elif monto > 0:
        totalPagar = totalPagar+monto
        
if totalPagar > 1000000:
    descuento = totalPagar*10/100
        
print("Su total a pagar es "+str(totalPagar-descuento))
