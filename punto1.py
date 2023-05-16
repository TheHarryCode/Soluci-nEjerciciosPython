# 1. Calcular mediante un algoritmo repetitivo usando Python, la suma de los N primeros números naturales.

n = int(input("Ingrese un número entero, para conocer su sumatoria: "))

suma = 0

for valor in range(1, n+1):
    suma = suma + valor
    print(suma)
    
print(f"La sumatoria de los primeros {n} numeros naturales es {suma}")