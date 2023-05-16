# 5. Desarrollar un algoritmo para calcular e imprimir el factorial de un número usando ciclos, 
#     (Puede apoyarse de consultas en Internet, pero use ciclos, no utilice la forma recursiva o con recursividad de funciones)

numeroxFactoriar = int(input("Ingrese un numero: "))

if numeroxFactoriar < 0:
    print("Debe ingresar un valor mayor o igual a cero")
else:
    cont=1
    sumatoria=1
    
    while cont <= numeroxFactoriar:
        sumatoria = sumatoria * cont
        cont = cont+1
        
    print("El factorial de "+str(numeroxFactoriar)+" es "+str(sumatoria))