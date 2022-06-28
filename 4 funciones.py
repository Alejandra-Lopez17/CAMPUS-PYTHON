#4: FUNCIONES 
"""Las funciones son un concepto que esta en todos los lenguajes de programacion, es algo global"""

# DEFINICION DE LAS FUNCIONES
"""def es una palabra clave, una palabra reservada. 
No podemos dar este nombre a variables porque esto esta reservado para esta funcion que es la de definir funciones"""

def saludar():
    print("Hola ¿Que tal?") 

saludar()  # <--- Esto se puede imprimir varias veces ejemplo: saludar() saludar() me va salir 2 veces Hola ¿Que tal?


# FUNCIONES CON ARGUMENTOS   
# <-- Que echo en el print e echo lo que se llama concatenar string print("Hola" + nombre + "¿Que tal?") 
# <-- Ese (nombre) es una variable.
# <-- SaludarDos es una funcion.

def saludarDos(nombre):                        
    print("Hola" + nombre + "¿Que tal?")     

saludarDos("Alejandra")
saludarDos("Lopez")        


# FUNCIONES CON RFETORNO 
"""Las funciones pueden retornar un valor, ese valor puede ser de cualquier tipo de datos que hemos visto que son
(los enteros, los numeros decimales, cadenas de texto, booleanos) y muchos mas que iremos viendo en el camino de nuestro proceso"""


def suma(a, b):
    resultado = a + b
    return resultado


valor = suma(10, 5)
print(valor)
valor = suma(23, 12)
print(valor)


def sumaDos(a, b):
    return a + b


valor = sumaDos(10, 5)
print(valor)


def sonIguales(num1, num2):
    return num1 == num2


verdad = sonIguales(3, 3)
if(verdad):
    print("Son iguales !!!")
else:
    print("Son diferentes")

print(verdad)
verdad = sonIguales(3, 3)
print(verdad)

"""(RETURN ES UNA PALABRA DE RETORNO)
Esto lo podemos ver como valores de entrada que son los argumentos valor de entrada --> suma(a, b):

Y esto como el valor de salida como el resultado de ejecutar esta funcion --> return resultado

Y este valor de salida lo podemos asignar a una variable con la cual podemos ir trabajando con esta variable VALOR 
si que podemos trabaja fuera de nuestra funcion --> valor = suma(10, 5) """


"""Cuando nosotros llamamos a la funcion ---> return num1 == num2  
esta funcion va a coger estos 2 numeros los va a comparar y recordar que estas expresiones comparativas
retornan un booleano y un booleano puede tener un valor true o false por tanto va a comparar estos dos numeros
y si son iguales el resultado de esto va a hacer true por tanto va a hacer un return de true 
y si son distintos el resultado de esta comparacion va ser false por tanto va a ser va a retornar un false aqui funciona
exactamente igual primero coge los dos numeros los suma y retorna el valor de esta suma---> num1 num2
no necesitamos utilizar una variable intermedia 
"""


# FUNCIONES CON ARGUMENTOS CON VALOR POR DEFECTO 
def saludarPorDefecto(nombre="Keren"):
    print("Hola " + nombre + " ¿Què tal?")


saludarPorDefecto()
saludarPorDefecto("Alejandra") 

"""IMPORTANTE🆘LAS COMILLAS SON IMPORTANTES PARA SEPARAR EL TEXTO Y NO QUEDE PEGADO EJEMPLO:
def saludarPorDefecto(nombre = "Keren"):
    print("Hola " + nombre + " ¿Què tal?")
saludarPorDefecto()
saludarPorDefecto("Alejandra") 

VA QUEDAR SEPARADO POR COMO ESTAS LAS COMILLAS SEPARADAS"""


# FUNCIONES QUE RETORNAN VARIOS VALORES 
def sumaYResta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

print("Apartado 5: Funciones con múltiples retornos. Función para saludar")
resultadoSuma, resultadoResta = sumaYResta(10, 5)
print("El resultado de la suma es: " + str(resultadoSuma) + "\n Y el de la resta: " + str(resultadoResta))


"""Tambien puedo retornar --> return a+b, a-b"""

"""resultado1 lo que va hacer es que se nos va guardar el valor de sumar. 

resultado2 lo que va hacer es que se nos va guardar el valor de resta. 

Este barra print("Los resultados son:\n") significa salto de linea, forzamos a que la salida sea con un salto de linea

concatenamos el resultado1 --> print("Los resultados son:\nsuma: "+resultado1 +"\nresta: "+resultado2) 
con el + puedo concatenar cadenas de texto, y esto que estoy haciendo para concatenar en cadena de texto 

Aqui voy hacer lo siguiente lo voy a convertir en str, cadena de texto
print("Los resultados son:\nsuma: "+str(resultado1) +"\nresta: "+str(resultado2))

"""

#   EJERCICIO 1: Función máximo -> Dados dos números, la función debe encontrar cuál de los dos
#   es el más grande y retornarlo.Extra: Se deben comprobar que los argumentos de la función sean
#   de tipo int o float. Si alguno de los dos no lo es, mostrar un mensaje de error y retornar False.


#   #SOLUCIÓN EJERCICIO 1

def maximo(num1, num2):
    if((type(num1)==int or type(num1)==float) and (type(num2)==int or type(num2)==float)):
        if(num1 > num2):
            return num1
        else:
            return num2
    else:
        print("Los argumentos no son válidos")
        return False

print("Apartado 6: Ejercicio 1. Encontrar el máximo de dos números")

num = maximo(3, 10)
if(type(num) != bool):
    print("El máximo es: " + str(num))

num = maximo(3, "Rojo") 
if(type(num) != bool):
    print("El máximo es: " + str(num))


"""Tengo que asegurarme que la funcion se haya ejecutado sin errores,
cuando me ejecuta con errores cuando nos retorna un booleano con valor false, por tanto yo me tengo que asegurar que lo que me a retornado
no es de tipo booleano si no es de tipo booleano, es de tipo numerico por tanto puedo decirle al usuario cual es el maximo.  
"""



#   EJERCICIO 2: Mini calculadora. Pedirle al usuario una operación y dos números.
#   Las operaciones pueden ser suma, resta, potencia. Si introduce una operación diferente
#   a estas, mostrar un mensaje de error. Si la operación es correcta, mostrar el resultado.


#   #SOLUCIÓN EJERCCICIO 2

def calculadora():
    operacion = input("¿Qué operación quieres hacer? Las operaciones posibles son:\n-suma\n-resta\n-potencia\n")
    num1 = float(input("Introduce el primer valor: "))
    num2 = float(input("Introduce el segundo valor: "))
    if(operacion == "suma"):
        print(num1 + num2)
    elif(operacion == "resta"):
        print(num1 - num2)
    elif(operacion == "potencia"):
        print(num1**num2)
    else:
        print(
            "Operación errónea. Las operaciones posibles son:\n-suma\n-resta\n-potencia\n")


print("Apartado 6: Ejercicio 2. Mini calculadora")
calculadora()


"""Si la operacion no es ni suma, ni resta, ni potencia, return lo e utilizado sin ningun valor. 
cuando utilizo return sin ningun valor dentro de una funcion significa acabas aqui ya no me ejecutas nada. 

El return siempre es la ultima instruccion de una funcion, despues del return no podemos escribir mas instrucciones
porque no se van a ejecutar, el return es como ya e acabado"""
