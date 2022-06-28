#   FUNCIONES LAMBDA:
#   Son funciones anónimas (no tienen nombre):
#   - Permiten múltiples argumentos.
#   - Solo puede tener una exmpresión.
#   - Estructura: lambda arg1, arg2 : expression

#   Apartado 1: Definir una función lambda

def suma(a, b): return a+b


print(suma(2, 3))
print(suma(5, 5))


def saludar(nombre): return f"Hola {nombre}!!"


print(saludar("Juan"))
print(saludar("ana"))


#   Apartado 2: Llamar funciones dentro de una lambda
#   Dentro de la expresión de una función lambda podemos
#   llamar otras funciones:

def maximo(
    a, b, c): return f"El máximos entre {a}, {b} y {c} es: {max(a, b, c)}"


print(maximo(3, 4, 5))


#   Apartado 3: Funciones lambda dentro de funciones
#   Podemos definir funciones lambda dentro de funciones
#   convencionales.
#
#   Esto nos permite generar funciones lambda con
#   distintos parámetros.


def ponerPrefijo(prefijo):
    return lambda nombre: f"{prefijo} {nombre}"


addMr = ponerPrefijo("Mr")
addMiss = ponerPrefijo("Miss")
addSr = ponerPrefijo("Sr")


print(addMr("Manuel"))
print(addMiss("Nerea"))
print(addSr("Rodolfo"))


def elevarA(exponente):
    return lambda base: base**exponente


elevarCuadrado = elevarA(2)
elevarCubo = elevarA(3)


print(elevarCuadrado(3))
print(elevarCubo(2))
