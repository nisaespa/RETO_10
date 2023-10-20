def conteo_de_ceros():
    arreglo = [] # Definir vacío el arreglo para que se elija que números poner 
    cantidad_numeros = int(input("¿Cuantos números quiere en su arreglo?: ")) # Para la cantidad de números
    for i in range(cantidad_numeros): # Para recorrer en el rango de la cantidad de números
        numeros = int(input("Ingrese los números que quiera en el arreglo")) # Números del arreglo
        arreglo.append(numeros) # Para añadir los números al arreglo
    conteo_0 = arreglo.count(0) # Con la función 'count' para contar cuantas veces está el número '0' en el arreglo
    print(f"El arreglo es: {arreglo}") # Imprimir arreglo
    print(f"La cantidad de veces que aparece el número '0' es: {conteo_0}") # Imprimir el conteo de ceros
# Iniciar programa
if __name__ == "__main__": 
    conteo_de_ceros() # Llamar función2
