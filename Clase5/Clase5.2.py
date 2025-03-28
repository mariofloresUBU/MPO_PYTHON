# Creame un diccionario

persona = {
    "nombre" : "Mario",
    "edad" : 32,
    "registrado" : True
}
print(persona)
#Accedeme a un valor por su clave
print(persona["edad"])

#Añadir una nueva clave-valor
persona["ciudad"] = "Vurgos"
persona["Numero de hijos"] = 3
print(persona)

#Cambiar el valor de una clave
persona["ciudad"] = "Burgos"
persona["Numero de hijos"] = 7
print(persona)

#Eliminar una clave
# del persona["registrado"]
# print(persona)

#Comprobar si una clave ya existe
existe_nombrecito = "Mario" in persona
existe_mario = "Mario" in persona["nombre"]
print(existe_nombrecito)
print(existe_mario)

#Comparar dos valores booleanos
es_menor_y_registrado = persona["edad"]>18 and persona["registrado"]
print(es_menor_y_registrado)

#Usar NOT con un booleano
no_veo_registro = not persona["registrado"]
print(no_veo_registro)

#Creame un conjunto a partir de una lista con duplicados
numeritos = [5,7,2,6,8,4]

#convierto a conjunto. PORQUE ASI ELIMINO DUPLICIDADES
conjuntito = set(numeritos)
print(conjuntito)

#Comparar si dos colecciones tienen los mismos elementos unicos
coleccion_a = set([1,2,2,3,4])
coleccion_b = set([3,4,2,1])

mismos_elementitos = coleccion_a == coleccion_b
print(mismos_elementitos)

