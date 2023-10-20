# Función para calcular el promedio de un arreglo
def calcular_promedio_arreglo(arreglo):
    suma = sum(arreglo) # Función (sum) para sumar los números dentro del arreglo
    promedio = suma / len(arreglo) # Para el promedio, dividendo es la suma delos numeros y el divisor es la cantidad de elementos en el arreglo
    return promedio # Retorna el promedio

# Iniciar programa
if __name__ == "__main__": 
    arreglo = [] # Definir vacío el arreglo para que se elija que números poner 
    cantidad_numeros = int(input("¿Cuantos números quiere en su arreglo?: ")) # Para la cantidad de números
    for _ in range(cantidad_numeros): # Para recorrer en el rango de la cantidad de números
        numero = float(input("Ingrese un número para el arreglo: ")) # Pedir los números las veces que el rango diga
        arreglo.append(numero) # Agregar cada numero en el arreglo con la función (append)
    promedio = calcular_promedio_arreglo(arreglo) # Definir variable "promedio" que contenga la función "calcular_promedio_arreglo"
    print("Arreglo:", arreglo) # Imprimir el arreglo
    print("Promedio:", promedio) # Imprimir el promedio