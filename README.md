# RETO 10 👽
## Arreglos

#### En el repositorio se encuentra documentado los ejercicios de el Reto 10 en archivo indivual  `.py` y en un archivo notebook `ipynb`.
+ Los algoritmos de sorting sirven para organizar elementos de una lista en un orden específico, generalmente en orden ascendente o descendente. 
+ Bubble Sort es un algoritmo de ordenamiento que organiza una lista de elementos comparando pares de elementos contiguos y, si están fuera de orden, los intercambia. Este proceso se repite a lo largo de la lista hasta que ningún intercambio es necesario. El algoritmo continúa pasando por la lista hasta que esté completamente ordenada.

+ Un ejemplo del Bubble Sort en python para ordenar números en forma ascendente de una lista:
```python
# función bubble_sort que toma una lista como argumento
def bubble_sort(lista):
    n = len(lista)  # longitud de la lista
    cambios = True  # Inicializar una variable que indicará si se realizaron cambios
    while cambios:  # Iniciar un bucle mientras se sigan realizando cambios en la lista
        cambios = False  # Antes de comenzar , asumimos que no hay cambios
        for i in range(1, n):  # Recorrer la lista desde el segundo elemento hasta el último
            if lista[i - 1] > lista[i]:  # Comparar el elemento actual con el siguiente
                lista[i - 1], lista[i] = lista[i], lista[i - 1]  # Si el elemento actual es mayor, intercambiarlos
                cambios = True  # Indicar que se realizó un cambio
numeros = [5, 2, 9, 3, 4]  # Crear una lista de números desordenados
bubble_sort(numeros)  # Llamar a la función bubble_sort para ordenar la lista 
print(numeros)  # Imprimir la lista en orden ascendente
```

+ Para entender mejor el funcionamiento del Bubble Sort:
  
<div align='center'>
<figure> <img src="https://media.geeksforgeeks.org/wp-content/uploads/20230526103842/1.webp" alt="" width="1000" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
<div align='center'>
<figure> <img src="https://media.geeksforgeeks.org/wp-content/uploads/20230526103914/2.webp" alt="" width="1000" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
<div align='center'>
<figure> <img src="https://media.geeksforgeeks.org/wp-content/uploads/20230526103949/3.webp" alt="" width="1000" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

Tomado de:
[Link Bubble Sort](https://www.geeksforgeeks.org/bubble-sort/)
