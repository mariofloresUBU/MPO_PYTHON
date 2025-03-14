import random
import math
from operator import truediv
from xmlrpc.client import boolean

#1. Longitud de una cadena
nombre = "Mario Flores"
print("Longitud del nombre: ", len(nombre))

#2. Convertir texto a mayusculas y minusculas
#upper
print("Estoy soy yo en mayúsculas: ", nombre.upper())
#lower
print("Esto soy yo en minúsculas: ", nombre.lower())

#3. Slicing
print("Primeros 3 caracteres: ", nombre[:3])
print("Últimos 4 caracteres: ", nombre[-4:])

#4. Reemplazar palabras en una cadena
frase = "Me gusta Java"
print("Cambio la palabra: ", frase.replace("Java", "Python"))
print(frase)

#5. Verificar si una cadena existe en otra
print("Python" in frase)
nueva_frase= "Me gusta Python"
nueva_frase= "Me gusta python"
print("Cambio a Python", nueva_frase.lower())
print("Python" in nueva_frase)

#6. Unir varias palabras en una cadena
palabras = ["Hola", "Mundo", "en", "Python"]
print("Frase completa con join: "," ".join(palabras))
print("\nHola Mundo")
#7. Split

oracion = "Python es divertido"
palabritas = oracion.split()
print("Lista de palabras de mi grupo: ", palabritas)

#8. Redondear un numero decimal
numero = 3.1416
print("Mi numero redondeado es: ", round(numero,6))

#9. Formateo de numeros decimales
precio = 19.99
print("Precio con dos decimales: {:.2f}".format(precio))

#10. Obtener el valor ASCII de un carácter
print("Esto es el código ASCII de 'A': ", ord('A'))

#11. Elevar al cuadrado
numero_al_cuadrado = 100
print("5 al cuadrado es: ", numero_al_cuadrado ** 2)

#12. Raiz cuadrada
print("Raiz cuadrada de 25 es: ", 25 ** 0.5)

import math
numerito = 100
raiz = math.sqrt(numerito)
print("La raiz del numero 100 es: ", raiz)

#13. Divisiones enteras y resto
print("Division normal: ", 10/3)
print("Division entera: ", 10//3)
print("Resto: ", 10%3)

#14. Generar un numero aleatorio
print("Numero aleatorio entre 1 y 10: ", random.randint(1,10))

#15. Convertir numeros a cadenas y viceversa
numerajo = 300
texto = str(numerajo)
print("Convertido a texto, soy: ", texto)

cadena = "200"
numerajo = int(cadena)
print("Convertido a numero soy: ", numerajo)

#16. Redondear hacia arriba y hacia abajo
print("Redondeo hacia arriba del numero 3.6: ", math.ceil(3.6))
print("Redondeo hacia arriba del numero 3.2: ", math.floor(3.2))

#17. Convertir una lista en un conjunto, es decir, eliminar duplicados
numeroides = [1,2,3,3,4,5,5]
sin_duplicados = set(numeroides)
print("La lista de numeroides sin duplicados es: ",sin_duplicados)

#18. Repetir una cadena
print("Money!" * 3)

#19. Tipo de dato
dato = 3.14
print("El tipo de variable de DATO es: ", type(dato))

#20. Combinar cadenas y variables en un print
name = "Mario"
edad = 32
print(f"Hola, soy {name} y tengo {edad} años.")
boolean mario = true;