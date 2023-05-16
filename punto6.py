#6.  Escriba un programa que pregunte una y otra vez si desea terminar el programa, salvo si se contesta S o s (en mayúsculas o en minúsculas).

noTerminarPrograma = True
while noTerminarPrograma:
    respuesta = input("Desea terminar el programa?: ")
    if respuesta == "s" or respuesta =="S":
        noTerminarPrograma = False
        print("Programo terminado!!!")    

