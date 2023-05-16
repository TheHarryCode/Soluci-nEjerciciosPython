#8. Determina si un número positivo es número primo. 
#    Un número es primo si sus únicos divisores son el mismo y el uno. 
#    Dicho de otro modo un número no es primo si existe algún divisor menor que él, excepto el uno. 
#    El usuario ingresa el número, y si este es primo  recibe un valor verdadero.

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True

numero = int(input("Ingrese un numero: "))

es_primo(numero)
