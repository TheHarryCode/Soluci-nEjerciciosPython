# 2. Realizar un algoritmo que permita pedir 50 números naturales y determine e imprima cuantos son pares, impares, positivos y negativos.

cantidadNumeros = int(input("Cantidad de numeros a ingresar: "))
pares = 0
impares = 0
negativos = 0
positivos = 0
neutros = 0
cont = 0

while cont < cantidadNumeros:

    n = int(input("Ingresa un numero: "))

    if n > 0:
        if n % 2 == 0:
            pares = pares+1
        else:
            impares = impares+1
    elif n < 0:
        negativos = negativos+1
    else:
        #el cero no es ni positivo ni negativo
        neutros = neutros+1
        
    cont=cont+1

positivos = impares + pares

print(f"Ingreso {pares} numeros pares")
print(f"Ingreso {impares} numeros impares")
print(f"Ingreso {negativos} numeros negativos")
print(f"Ingreso {positivos} numeros positivos")
print(f"Ingreso {neutros} numeros neutros")
