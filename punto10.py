#10. Si tiene el siguiente diccionario en Python,  
#       frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja', 'Manzana':'amarilla', 'Guayaba':'rosa'}
#  Haga un algoritmo que permita iterar sobre el diccionario mostrando el contenido de este así:
#            Fresa es de color roja
#             Limon es de color verde 
#              Manzana es de color amarilla
#               Papaya es de color naranja
#                Guayaba es de color rosa

#Diccionario original
frutas = {'Fresa':'roja', 'Limon':'verde', 'Manzana':'amarilla', 'Papaya':'naranja','Guayaba':'rosa'}

#Se modificaan las claves para darle el orden indicando en el enunciado
frutas.pop("Papaya")
frutas.pop("Guayaba")

frutas["Papaya"]="naranja"
frutas["Guayaba"]="rosa"

for clave, valor in frutas.items(): 
    print(clave + " es de color " +valor)