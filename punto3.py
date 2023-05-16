"""
3. Dado N notas de un estudiante calcular:
a) ¿Cuántas notas tiene reprobadas?.
b) ¿Cuántas notas aprobadas?.
c) El promedio de notas.
d) El promedio de notas aprobadas
e) El promedio de notas reprobadas.
"""

cantidadNotas = 0
sumatoriaNotas = 0
cantidadNotasAprobadas = 0
sumatoriaNotasAprobadas = 0
cantidadNotasReprobadas = 0
sumatoriaNotasReprobadas = 0
 
criterioGanarNota = int(input("Ingrese a partir de que valor de nota, es aprobada: "))
 
pedirNotas = True
while pedirNotas:
    nota = int(input("Ingrese su nota: "))
    
    if nota == 0:
        pedirNotas = False
    else:
        cantidadNotas=cantidadNotas+1
        sumatoriaNotas=sumatoriaNotas+nota
        
    if pedirNotas:
        if nota >= criterioGanarNota:
            cantidadNotasAprobadas=cantidadNotasAprobadas+1
            sumatoriaNotasAprobadas=sumatoriaNotasAprobadas+nota
        else:
            cantidadNotasReprobadas=cantidadNotasReprobadas+1
            sumatoriaNotasReprobadas=sumatoriaNotasReprobadas+nota
 
print("Cantidad de Notas Reprobadas: "+str(cantidadNotasReprobadas))
print("Cantidad de Notas Aprobadas: "+str(cantidadNotasAprobadas))
print("Promedio de Notas: "+str(sumatoriaNotas/cantidadNotas))
print("Promedio de Notas Aprobadas: "+str(sumatoriaNotasAprobadas/cantidadNotasAprobadas))
print("Promedio de Notas Reprobadas: "+str(sumatoriaNotasReprobadas/cantidadNotasReprobadas))
