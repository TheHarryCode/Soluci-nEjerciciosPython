# 9. Analice e implemente un programa en Python que ingrese sólo números pares (se debe validar) hasta que la suma de todos ellos sea superior a 300.
# El programa debe imprimir la suma final.

pedirNumeros = True
sumatoria = 0
while pedirNumeros:
    num = int(input("Ingrese un numero par: "))
    
    if num % 2 ==0:
        sumatoria=sumatoria+num
    else:
        print("Numero invalido, solo se permiten numeros pares")
    
    if sumatoria > 300:
        pedirNumeros = False

print("La sumatoria de los numeros ingresados es: "+str(sumatoria))    
