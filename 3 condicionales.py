#3 BOOLEANOS, CONDICIONALES Y ENTRADA DE USUARIO

# ENTRADA DE DATOS DEL USUARIO

edad = input ("Escribe tu edad por favor: ") 
print(edad) 

"""INPUT : (para hasta que el usuario le confirme la edad)
Esta función permite obtener el texto escrito por el usuario, 
el cual se asignará a un espacio de memoria con el nombre que el programador vea conveniente.
Al llegar a la linea que contiene el comando, (LA CONSOLA ESPERARA RESPUESTA) """


# COMO IDENTIFICAR EL TIPO DE DATOS, ---> (automaticamente desde nuestro programa)
edad = input ("Escribe tu edad por favor: ")
tipo_de_datos = type(edad) 
print(edad) 
print(tipo_de_datos) 

"""type la funcion, type es para que me retorne la variable (edad)
en este caso (mi variable de entrada es edad), y lo que (retorna es tipo de datos, de la variable edad)"""

# BOOLEANOS, IF --> solo guardan verdadero o falso, (van muy ligados de condicionales)
verdadero = True
falso = False

if(verdadero == True):
    print("Soy verdadero!!!")

if(falso == False):
    print("Efectivamente, soy falso") 


# Operadores de Compraración, elif, else ( ==, !=, <, >, >=, <= )
edad = input("Dime tu edad, por favor: ") 
edad = int(edad) 
if(edad >= 18):
    print("Eres mayor de edad, puedes pasar") 

elif(edad <14):
    print("Oye eres muy pequeño")

elif(edad <0):
    print("Oye, esto es imposible")

else:
    print("Eres menor de edad, no puedes pasar")  

"""
INT : (ES UN TIPO DE DATO ENTERO ES UN TIPO DE DATO NUMERICO,
Y ESTO AL LLAMAR A LA FUNCION INT, EN INGLES ES UN CASTING O CASTEAR, 
LO QUE NOS VA DEVOLVER ES SU VALOR NUMERICO) 

IF : (La palabra reservada if , da inicio al condicional if.
La siguiente parte es la condición. Esta puede evaluar si la declaración es verdadera o falsa.
En Python estas son definidas por las palabras reservadas (True or False) )   

ELIF : ("elif" sirve para enlazar varios "else if", sin tener que aumentar las tabulaciones en cada nueva comparación.
En Python no existe una orden "switch" o "case", sino que se deben realizar enlazando varios casos con "elif") 

---> PUEDO PONER VARIOS (ELIF, COMO QUERAMOS NO HAY RESTRICCIÓN)
---> (IF Y ELSE, UNICAMENTE PODEMOS PONER 1)
"""


"""OPERADORES LÓGICOS and, or, not
NOS SIRVEN PARA COMPROBAR VARIAS EXPRESIONES ALA VEZ.

and  Returns True if both statements are true x < 5 and  x < 10 

(AND : SE DEBERAN CUMPLIR TODAS LAS CONDICIONES QUE PONGAMOS)


or Returns True if one of the statements is true x < 5 or x < 4

(OR : PUEDES ENTRAR CON UNA ENTRADA VIP NO, PERO TIENES UNA ENTRADA NORMAL TE DEJO ENTRAR, UNICAMENTE NECESITAMOS
QUE SE CUMPLA 1 DE VARIAS CONDICIONES QUE PONGAMOS)

not Reverse the result, returns False if the result is true not(x < 5 and x < 10)

(NOT : SIRVE PARA HACER( LA LOGICA INVERSA) SI ESTA EXPRESION ES (TRUE), EL NOT LA CONVIERTE A (FALSE), 
Y SI ESTA EXPRESION ES (FALSE) EL NOT LA CONVIERTE EN (TRUE) 
"""


# OPERADORES LÓGICOS and, or, not
edad = input("Dime tu edad, por favor: ") 
edad = int(edad) 

if(type(edad) == int):
    if(edad > 120 or edad < 0):
        print("Esto no es posible") 
    elif(edad > 18 and edad < 40):
        print("Puedes entrar a mi club")
    elif(edad < 18 and edad > 15):
        print("Todavia eres un pelado, no puedes entrar") 
    else:
        print("No ha sucedido ninguna de las condiciones")
else:
    print("Oye, que la edad debe ser un numero entero")

if(not(edad <= 18)):
    print("Puedes pasar") 

#Ejercicio: comprobar si el usuario introduce un numero, si no es un numero
#indicar que debe introducirun entero. Si es un numero, debemos comprobar
#si es o no PAR y notificarselo al usuario.   

#PISTAS:
#  isnumeric, num%2 = 0
texto = "hola"
txt = "22"
print(texto.isnumeric())
print(txt.isnumeric()) 


#SOLUCION
num = input("Dime un numero: ")
if(not(num.isnumeric())):
    print("Datos incorrectos. Debe ser un numero") 
else:
    num = int(num)
    if(num%2 == 0):
        print("Es par") 
    else:
        print("Es impar") 