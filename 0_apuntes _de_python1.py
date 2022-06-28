"""Si hago esto me va contar 26 caracteres de lo que escribi (Hola que tal desde python!)<-- (ESTO ES UN STRINGS)
y cuenta los espacios"""

frase= "Hola que tal desde python!"
print(len(frase)) 

"""Aqui me va a aparecer una esclamacion (!) si le coloco (-5) me da la letra (T) 
porque empieza a coger (Hola que tal desde python!)""" 
frase= "Hola que tal desde python!" 
print(len(frase))
print(frase[-1]) 

#COMO PUEDO FORMATEAR EL STRINGS-->(ESTA ES LA FORMA DONDE PODEMOS INTRODUCIR UNA VARIABLE DENTRO DE UN STRINGS EN PYTHON)
frase = "Hola me llamo Alejandra"
print(frase)
nombre = "Alejandra"
print(f"hola me llamo {nombre}") 

# CLASS
"""
CLASS-STR, (TEXTO)--->QUIERE DECIR QUE ES STRING, (CADENA DE TEXTO)

CLASS-iNT, (NUMERO)--->QUIERE DECIR QUE ES DE TIPO, (NUMERICO)

CLASS-BOOL, (VERDADERO)--->QUIERE DECIR QUE ES DE TIPO, (BOOLEANAS)

CLASS-FLOAT, (DECIMAL)--->QUIERE DECIR QUE ES DE TIPO, (FLOAT, FLOTANTE O DECIMALES)
"""


# TIPADO DE DATOS, COMO INTRODUCIR DATOS EN CONSOLA, Y COMO PODEMOS MODIFICAR EL TIPADO
texto = "texto"
numero = 45 
verdadero = True
decimal = 4.5
print(type(decimal)) 

#input---> la consola va esperar que escriba
nombre = input("introduce tu nombre") 
saludo = f"hola me llamo {nombre}"
print(saludo) 

"""SI QUIERO SUMAR NUMEROS DEBO PONER int QUE ES DE TIPO NUMERICO,
Y QUIERO INTRODUCIR ALGO COMO EDAD O NOMBRE DEBO PONER INPUT

---> STR, int, BOOL, FLOAT, (ESTOS SON LOS 4 METODOS DE CONVERTIR UN TIPO A OTRO)"""
edad = int(input("introduce tu edad"))
suma = edad + 20
print(suma) 