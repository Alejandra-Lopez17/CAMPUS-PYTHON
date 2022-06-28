#5: BUCLES 

#   Breve introducción a las listas
#Los bucles y las listas van un poco ligada

"""Una lista es un tipo de dato nativo de python que va agrupar informacion, es decir va agrupar otros datos como
"""

"""las posiciones o los indices simplemente es en que lugar de la lista esta ubicado cada elemento por ejemplo
[El elemento 1, esta ubicado en la posicion 0] 
[El elemento 2, esta ubicado en la posicion 1]
[El elemento 3, esta ubicado en la posicion 2]
[El elemento 4, esta ubicado en la posicion 3]
[El elemento 5, esta ubicado en la posicion 4]
"""
numeros = [1,2,3,4,5] 


# Las posiciones de las listas van desde el 0 hasta la posicion longitud - 1
print(numeros)
print(numeros[0])
print(numeros[2])

print(len(numeros)) 

"""Porque sale 5, porque tenemos 5 elementos""" 

"""La funcion len, la podemos utilizar con lista, cadenas de texto,"""

# Ejemplo: lista de cadenas de texto 
texto = ["Juliana", "Botella", "taza"] 
print(texto) 
print(texto[2]) 

variada = [1, 2.3, False, "Hola"] 

print(texto[len(texto) -1])

"""print(texto[len(texto) -1]) 
ES PARA ACCEDER ALA ULTIMA POSICION, Y NO SABEMOS CUANTOS ELEMENTOS TIENE PORQUE ES MUY LARGA,
O PORQUE HEMOS CONSEGUIDO ESTO DE OTRA FUENTE
"""
#Breve introducción a las listas
numeros = [0, 1, 2, 3, 4, 5]
nombres = ["Jorge", "Juan", "Javier", "Jairo"]
variada = ["Juan", 3, False, True, 2, "arroz"]

longitudnumeros = len(numeros)
longitudnombres = len(nombres)
longitudvariada = len(variada)

print(longitudnumeros)
print(numeros)
print(longitudnombres)
print(nombres)
print(longitudvariada)
print(variada)

#Elementos de una lista
print("Primer elemento de numeros")
print(numeros[0])
print("Último elemento de nombres")
print(nombres[longitudnombres-1])



#  BUCLES: BUCLE FOR
"""Un BUCLES es algo que se repite y en programacion que vamos a querer repetir una serie de intrucciones es decir un pequeño bloque de codigo
es muy util en todos los lenguajes en cualquier tipo de programa van a existir bucles.
BUCLES tenemos dos tipos for y tenemos while"""

for x in range(5):
    print(x)

for x in range(3, 10):
    print(x)

for x in range(5, 21, 2):
    print(x)


"""for x in range(5,21, 2): 
print(x) 

19 MAS 2 ES 21 Y 21 ES EL LIMITE SUPERIOR, SI ME PASO DE 20 ME VOY A QUEDAR EN EL VALOR ANTERIOR.
PARA NO SUPERAR EN LA SIGUIENTE INTERACCION EL LIMITE SUPERIOR"""
for x in range(5):
    print(x)

for letra in "Alejandra":
    print(letra)


#  MINI EJEMPLO, IMPRIMIR SOLO LAS VOCALES DE UNA PALABRA
palabra = "cocodrilo"
for letra in palabra:
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print(letra)
    else:
        print("Es una consonante") 


#MINI EJEMPLO, IMPRIMIR SOLO LAS VOCALES DE UNA PALABRA
for letra in "cococdrilo":
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print(letra)
    else:
        print("No es una vocal")


#  MINI EJEMPLO, ITERAR SOBRE UNA LISTA
numeros = [22, 33, 44, 55]
for numero in numeros:
    print(numero)
    numero += 10
    print(numero)

print(numeros) 

for indice in range(len(numeros)):
    numeros [indice]+= 10

print(numeros)


#Mini ejemplo, iterar sobre una lista
print("Lista original de numeros: ")
print(numeros)

for num in numeros:
    print(num)
    num += 10

print("Lista modificada de numeros: ")
print(numeros)


# BUCLES WHILE 
"""los BUCLES WHILE sirven de lo que ya he visto al inicio de ejecutar el codigo hasta que se cumpla una condicion
"""

#La idea principal de un bucles while
contador = 0
while(contador < 10):
    print(contador)
    contador +=1


#Ejemplo: encontrar todas las (a) en una frase
i = 0
while(i < 10):
    print(i)
    i += 1

letraEncontrada = False
letra = "a"
frase = "En este momento estoy buscando la letra a"
pos = 0

while(not(letraEncontrada)):
    if(frase[pos] == "a"):
        letraEncontrada = True
        print(f"Encontrada la letra {letra} en la posición {pos}")
    else:
        pos += 1


#  BREAK, CONTINUE, PASS

#  BREAK
frase = "En este momento estoy buscando la letra a"
letra = "y"

for caracter in frase:
    if(caracter == letra):
        print(f"Letra {letra} encontradaben la posicion {frase.index(caracter)}!!")
        print(caracter)
        break
    else:
        print("No hemos encontrado nada de momento")


"""(BREAK): ES DECIRTE HASTA AQUI HEMOS LLEGADO, TU RELACION CON ESTE BUCLES A TERMINADO. 
YA NO REPETIMOS NADA MAS."""


#BREAK
frase = "No sé cuando encontraré la letra a"
letra = "a"

for x in frase:
    if(x == "a"):
        print(f"Encontrada en la posición: {frase.index(x)}")
        break



#  CONTINUE 
frase = "Hola Yovana"
letra = "a"
count = 0

for caracter in frase:
    if(caracter == letra):
        count += 1
        print(f"Letra encontrada {count} veces")
        continue
    print("No he encontrado nada")


"""(CONTINUE): QUE HACE EL CONTINUE TE DICE VETE PARA LA SIGUIENTE ITERACCION, Y FUNCIONA BASICAMENTE IGUAL QUE EL BREAK,
NO SALE DEL BUCLE, SI ESTAMOS EN LA ITERACCION 0 Y LLEGAMOS A UN CONTINUE PASAREMOS DIRECTAMENTE A LA ITERACCION 1
INDEPENDIENTEMENTE DE CUANTO CODIGO ALLA DEBAJO DE LA INSTRUCCION CONTINUE."""


#Continue
frase = "Hola Ana"
count = 0
for x in frase:
    if(x == "a"):
        count = count + 1
        continue
    print("No hemos encontrado nada")
print(count)



# PASS
lista = [0, 10, 20, 43]
for andres in lista:
    if(andres == 10):
        pass
        print(f"El valor de andres es: {andres}")


"""(PASS): SIGNIFICA YO PASO, NO HAGO NADA."""


#PASS
frase = "frase corta"
for x in frase:
    if(x == "a"):
        pass
    print("Seguimos con la iteración")



#  Else 
frase = "Todos los caracteres de una frase "
count = 0
for caracter in frase:
    count +=1 
else:
    print(f"La frase tiene {count} caracteres") 



#Else
frase = "Quiero contar todas las a de esta frase"
count = 0

for x in frase:
    if(x == "a"):
        count = count + 1
        continue
    print("No hemos encontrado nada")
else:
    print(f"Hemos encontrado {count} veces la letra a")



#   Ejercicio: El usuario debe adivinar un número entre 0 y 10.
#   El programa deberá pedir que el usuario introduzca un número
#   y debe decir si ha acertado, si el número es menor o mayor que
#   el que ha introducido.

def pedirYComprobar(numero):
    num = int(input("Introduce el número: "))
    if(num == numero):
        print("Has acertado")
        return True
    elif(numero > num):
        print("Casi! Prueba con un número más grande")
        return False
    elif(numero < num):
        print("Casi! Prueba con un número pequeño")
        return False

while(True):
    if(pedirYComprobar(7)):
        break
else:
    print("Cuando hay un break, no se ejecuta el else")


while(not(pedirYComprobar(7))):
    pass
