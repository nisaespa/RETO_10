# Función para calcular el producto punto de dos arreglos
def producto_punto(arreglo_1, arreglo_2): # los arreglos son los argumentos
    producto_punto = 0 # Definimos la variable producto_punto en 0
    for i in range(cantidad_numeros): # Iteración del rango que quiera el usuario
        producto_punto += arreglo_1[i] * arreglo_2[i] # Formula para el producto punto, la suma de los productos de sus elementos (de los arreglos)
    return producto_punto # retorna producto_punto
# Iniciar programa
if __name__ == "__main__": 
    arreglo_1 = [] # Definir vacío el arreglo para que se elija que números poner 
    arreglo_2 = [] # Definir vacío el arreglo para que se elija que números poner 
    cantidad_numeros = int(input("¿Cuantos números quiere en su arreglo?: ")) # Para la cantidad de números
    for i in range(cantidad_numeros): # Para recorrer en el rango de la cantidad de números
        numeros_1 = int(input("Ingrese los números que quiera en el primer arreglo")) # Números del primer arreglo
        arreglo_1.append(numeros_1) # Añadir los números al primer arreglo
    for i in range(cantidad_numeros): # Para recorrer en el rango de la cantidad de números
        numeros_2 = int(input("Ingrese los números que quiera en el segundo arreglo")) # Números del segundo arreglo
        arreglo_2.append(numeros_2) # Añadir los números al segundo arreglo
    print(f"El arreglo 1 es:{arreglo_1}") # Imprimir arreglo 1
    print(f"El arreglo 2 es:{arreglo_2}") # Imprimir arreglo 2
    product_punto = producto_punto(arreglo_1, arreglo_2) # Definir variable como la función 'producto_punto'
    print(f"El producto punto de los dos arreglos es: {product_punto}") # Imprimir el producto punto de los dos arreglos