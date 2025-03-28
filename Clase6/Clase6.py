#1. Crea la lista con los dias de la semana y muestrame el primero y el ultimo
#ALT SHIFT E
from traceback import print_tb

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print("Primer dia de la semana: ", dias[0])
print("Ultimo dia de la semana: ", dias[-1])

#2. Modificar un elemento de una lista de frutas y añadir una nueva fruta al final
frutas = ["Manzana", "Platano", "Pera"]
frutas[0]="Mango"
print(frutas)
#añado una fruta al final
frutas.append("Sandia")
print(frutas)

#3. Crea una lista vacia y llenala con tres colores usando append()
colores = []
print(colores)
colores.append("Rojo")
colores.append("Amarillo")
colores.append("Rojo")
print(colores)

#4. Ordename una lista de numeros desordenados y muestrala al reves
numeros = [6,2,4,0,1,12,6,8]
#ordenalos
numeros.sort()
print(numeros)
#Invierto el orden
numeros.reverse()
print(numeros)

#5. Elimina un elemento de una lista y muestra el resultado
animales = ["Perro", "Pulpo", "Gato", "Rinoceronte"]
print(animales)
animales.remove("Gato")
print(animales)

#6. Cuentame cuantas veces aparece un numero en la lista
numeritos = [4,6,7,8,2,3,4,5,6,7,8,9]
cantidad = numeritos.count(9)
print("El numero de veces que se repite el numero es: ", cantidad)


#7. Crea una tupla con tres elementos de distinto tipo cada uno
mi_tupla = (19,"Mario", True)
print("Numero: ", mi_tupla[0])
print("String: ", mi_tupla[1])
print("Boolean: ", mi_tupla[2])

#8. Acceder al segundo elemento de una tupla anidada dentro de una lista
datos = ["Nombre", (100,200), "Apellido"]
tupla_intermedia = datos[1]
print(tupla_intermedia)

#9. Desempaquetar una tupla en 3 variables y muestramelas
persona = ("Sara", 32, "Madrid")
nombre, edad, ciudad = persona
print("Nombre: ",nombre)
print("Edad: ", edad)
print("Ciudad: ", ciudad)













