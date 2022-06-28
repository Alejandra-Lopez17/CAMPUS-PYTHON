# FUNCIONES--> que es una funcion es una porción reutilizable que ejecuta alguna acción
"""print() es una funcion"""


def nombre_funcion():
    print("Hola a todos")


print("hola desde fuera de la funcion")

nombre_funcion()

"""ASI PODEMOS DEFINIR NUESTRAS PROPIAS FUNCIONES DENTRO DE PYTHON"""

# PARAMETROS--> como utilizar una funcion, y de como podemos pasarle argumentos o parametros a nuestras funciones


def saludar(
    nombre):                      """EN ESTE CASO SALUDAR SE LLAMA LA FUNCION"""


print(f"Hola me llamo alejandra")

saludar("")

"""Hay una diferencia entre parametro y argumento. 
un parametro se utiliza cuando nosotros definimos las funciones.
un argumento se utiliza cuando le damos un valor a dicho parametro"""

# TIPOS DE FUNCIONES--> hay 2 tipos de funciones, las funciones que realizan alguna accion, y las funciones que devuelven algun dato

#Funciones que realizan alguna accion
print("Hola")


#Funciones que devuelven un dato
def sumar(n1, n2):
    return n1 + n2


suma = sumar(2, 7)
print(suma)
print(sumar(2, 5))

print(2+7)


# KEYWORDS ARGUMENTS-->esta característica es muy utilizada, para darle una mejor legibilidad al codigo
def incrementar(numero, by):
    return numero + by


"""incremento = incrementar(2,1) """

print(incrementar(2, by=1))

"""Recuerda que los nombre de las variables deben llamarse iguales
los nombres de las funciones, cortas y descriptivas posibles"""


# PARAMETROS POR DEFECTO-->que podemos recibir dentro de las funciones
def incrementar(numero, by=5):
    return numero + by


print(incrementar(2, 2))

"""ESTA ES LA MANERA MAS SENCILLA DE DEFINIR PARAMETROS POR DEFECTOS DENTRO DE NUESTRAS FUNCIONES
MUCHAS VECES TENEMOS QUE DEFINIR FUNCIONES QUE RECIBAN CIERTA CANTIDAD DE PARAMTROS, YA VEREMOS QUE ES EL SHART
PUEDE QUE NECESITEMOS QUE ALGUNO DE ESTOS PARAMETROS SEAN FIJOS Y QUE EN OCACIONES TENGA QUE SER VARIABLES.
EN ESTE CASO LO PODEMOS HACER DE LA SIGUIENTE MANERA, 
DANDOLE UN VALOR EN LA DECLARACION DE LA FUNCION PARA QUE ESE VALOR SEA FIJO, Y EN EL CASO QUE SE LO PASEMOS COMO ARGUMENTO,
ESE VALOR CAMBIA CUANDO YO LO DECLARO AQUI, Y CUANDO LLAMO Y DIGO QUE EL SEGUNDO PARAMETRO VALE 2 
PYTHON LO QUE HACE ES QUITARME EL 5 DE HAY Y PONERME UN 2 HAY
def incrementar(numero, by=5):
    return numero + by

print (incrementar(2,2))
"""


# PARAMETROS XARG-->Lo que hacen los xarg son los argumentos valorativos dentro de python
def sumar(n1, n2, n3, n4):
    total = n1 + n2 + n3 + n4
    return total


print(sumar(1, 2, 3, 4))

"""xargs"""


def sumar_x_args(*numeros):
    total = 0 
    for numero in numeros:
        total += numero
        return total

print(sumar_x_args(1,2,3,4,5,6,7))


# PARAMETROS XXARG-->Como recibir un diccionario dentro de python y poder mostrar los diferentes valor de dicho diccionario
def mostrar_usuario(**usuario):
    print(usuario) 

print(mostrar_usuario(id=1, nombre="Alejandra"))
