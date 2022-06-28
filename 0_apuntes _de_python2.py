# OPERACIONES DE COMPARACION --->
"""(son expresiones y como tal las expresiones dentro de los lenguajes de programacion devuelven un valor tanto TRUE O FLASE)
(POSITIVO O NEGATIVO)"""

verdad= False

#Mayor
print(4>1)

#Menor
print(4<1)

#Mayor o igual
print(4>=1)

#Menor o igual 
print(4>=1)

#Igualdad
print(4==1)

#Negacion
print(not verdad)  

"""ESTOS SON BASICAMENTE TODOS LOS OPERADORES DE COMPARACION( ==, !=, <, >, >=, <= ) QUE TENEMOS DENTRO DE PYTHON"""



# SENTENCIA DE CONTROL DE FLUJO IF, (ES SUPER COMUN EN TODOS LOS LENGUAJES DE PROGRAMACION)
edad = 16
if edad > 18:
    print("Eres mayor de edad")

elif edad <= 16:
    print("Eres menor de edad")

"""Esto lo que hace es concatenar, diferentes expresiones,
porque la edad es es menor o igual a 16 por lo tanto se ejecuta el valor 2.  
si cambio el valor y pongo donde dice(edad = 20) me dira que soy mayor de edad"""

edad = 20
if edad > 18:
    print("Eres adulto")

elif edad <= 16:
    print("Eres pequeño")

else: 
    print("No tienes edad eres un vampiro")


# OPERADOR TERNARIO (EN PYTHON)---> vAMOS A SEGUIR CON EL EJEMPLO ANTERIOR
"""AQUI ES MAS LEGIBLE Y FUNCIONA COMPLETAMENTE MEJOR"""

edad = 20
if edad > 18:
    print("Eres super grande")

elif edad <= 16:
    print("Eres super pequeño")

else: 
    print("No tienes edad")

mensaje = "Eres super grande" if edad >= 18 else "Eres super pequeño" #ESTO ES LO QUE SE DENOMINA UN OPERADOR TERNARIO-->(UNA SOLA LINEA)
print(mensaje)  


# OPERADORES LÓGICOS (DENTRO DE PYTHON)
x = True
y = True

"""and las dos verdaderas para ser verdadero"""
if x == y and x > y: 
    print("AND es true")

"""Una de ellas debe ser verdadero para ser verdadero"""
if x == y or x > y:
    print("OR es true")  


# CIRCUITO CORTO DE EVALUACION --> Esto casi no lo explican los desarrolladores
primera = True
segunda = True
tercera = True

if primera and segunda and tercera:
    print("Todo esta ok")

"""El AND lo que hace es evaluar entre la primera, segunda, y tercera son positivas y todas son True entonces pasa"""


#Segundo ejemplo ---> CIRCUITO CORTO
primera = False
segunda = True
tercera = True

if primera and segunda and tercera:
    print("Todo esta bien")
    print("Fin del programa")

"""Si la primera expresion da falso las otras expresiones a python le da igual"""

# CONCATENACIONES (DE OPERADORES DE COMPARACION)
edad = 18
if edad >= 18 and edad < 65:
 if 18 >= edad <65:
    print("Estas en edad de trabajar")

"""De esta forma nos podemos podemos evitar los operadores (and) y los operadores (or)
puedo quitar la linea (if edad >= 18 and edad < 65:) 
y sigue funcionando normal sin el and y el or"""


# FOR LOOPS --> (ESTE BLUQUE ES BASTANTE UTIL)
for intento in range(4):
    print("Intento de envio")


# bucle WHILE->(hay que saber manera para que no se convierta en infinito)"""SI COLOCO PRINT (MENSAJE) SE VUELVE INFINITO, ENTONCES EMPIZA LA MEMORIA RAM A COLAPSAR """
while True:


#Entonces vamos a ponerle numero a (BUCLE WHILE)
 numero = 100
while numero > 0:
 print(numero)
numero //=2


#Otro ejemplo de (BUCLE WHILE)
comando = ""
while comando != "salir":
    comando = input(">")
    print(f"el comando introducido es {comando}")

"""Esto me da para decir el comando introducido es Hola, 
el comando introducido es Adios

HASTA AQUI TERMINE MI APUNTE 2""" 