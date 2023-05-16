# 4. Calcular y visualizar la suma y el promedio de los números pares comprendidos entre 20 y N (ambos incluidos). 
#     N es un número ingresado por el usuario, valide si el usuario ingresa un número menor a 20.

num = int(input("Ingrese un numero: "))

sumatoria = 0
cantidad = 0
contador = 20

if num < 20:
    print("El numero ingresado es menor a 20")
else:
    while num >= contador:
        sumatoria= sumatoria+contador
        cantidad= cantidad+1
        contador=contador+2
        
    print("El Sumatoria de Numeros pares entre 20 y "+str(num)+" es: "+str(sumatoria));
    print("El Promedio de los Numeros pares entre 20 y "+str(num)+" es: "+str(sumatoria/cantidad));