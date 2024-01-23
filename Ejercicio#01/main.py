
""" 
* EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""


#https://es.wikipedia.org/wiki/Python

#----Comentarios en una sola linea

"""----Bloque de comentarios"""

#Constantes 

PI = 3.1415
SEGUNDOS_HORA=3600

#Variables

x = input("Ingresa algo:")

#Variables con tipos de dato

#Numericos
integer_x=33
float_x=3.1223
Complex_value_x=3+4

#Cadenas de texto

s1="Hola "
s2="mundo 1"

print(s1+s2)

#Booleanos 

truev = True
falsev = False
print(type(truev))
print("True y False->", truev and falsev)

#Diccionarios

usuario = {
    
    "Nombre":"Mauricio",
    "Edad":"18 años",
    "Escuela":"TESJI"
}

print(usuario.get("Nombre"))

#Hola mundo

print("Hola mundo 2")