""" 
* EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *

"""

#Operadores aritmeticos----------------------------------

x=34+6

print(x)

x=12-3

print(x)

x=45/3

print(x)

x=3*5

print(x)

x=16%3

print(x)

x=3**2

print(x)

x=16//5

print(x)

#Operadores logicos--------------------------------------

x=True

a=False

print(x and a)
print(x or a)
print(not a) #Devuelve true si algunos de los operandos es falso



#Operadores de asignacion---------------------------------

a=5
x*=4
x/=2
x+=2
x-=1
x%=3
x//=3
x**=3

#Especiales

a=2

a&=3
a|=2
a^=5
a>>=34
a<<=2

#Operadores de identidad-------------------------------------

a=3
b=56
c=3

print(a is b)
print(a is not b)
print(a is not c)


#Operadores de pertenencia------------------------------------

x=[1,2,3,4,5]

print(4 in x)
print(23 in x)