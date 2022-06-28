#2: VARIABLES, TIPOS DE DATOS Y OPERADORES ARITMÉTICOS. (COMENTARIO # ) 

"""VARIABLES DE PYTHON  (Este es un comentario de varias lineas (COMENTARIO DE COMILLAS DOBLES)

Variable es un nombre que se usa para referirse a la ubicación de la memoria
La variable de Python también se conoce como un identificador y se usa para
mantener el valor.

En Python, no necesitamos especificar el tipo de variable porque Python es un
lenguaje de inferir y lo suficientemente inteligente como para obtener el tipo
de variable.

Los nombres de las variables pueden ser un grupo de letras y dígitos, pero
deben comenzar con una letra o un guion bajo."""


#  VARIABLES, TIPOS DE DATOS NUMÉRICOS (MOSTRAR VARIABLES POR CONSOLA)
'UN NUMERO ENTERO OCUPA MENOS VIX, QUE LOS NUMEROS DECIMALES (COMENTARIO EN COMILLAS SIMPLES)' 

numero_entero = 1                                                       
print(numero_entero)                                

numero_decimal = 2.46
print(numero_decimal) 

#LAS PODEMOS COMBINAR
numero_entero = numero_entero +2 
print(numero_entero)

#Otra cosa que podemos hacer es (definir un numero a secas numero nuevo, con un numero decimal)
"""Y PODEMOS SUMAR UN NUMERO ENTERO, CON UN NUMERO DECIMAL"""
numero = numero_entero + numero_decimal 
print(numero)

#Una forma rapida de sumar estos números, (DE FORMA CORTA)
"""ES COMO UN ATAJO LE ESTOY DICIENDO COGE EL VALOR ACTUAL DE NUMERO ENTERO Y LE SUMAS 2"""
numero_entero += 2 
print(numero_entero)

#Vamos a definir una nueva variable, le vamos a llamar (VARIABLE NUMERICA)

#RESTAR
variable_numerica = 20 
variable_numerica = variable_numerica - 10
print(variable_numerica)

#DIVIDIR
variable = 10
variable = variable / variable_numerica 
print(variable)

#Podemos definir una nueva variable (QUE HAGA / + )
numero = 2/2+3 
print(numero) 

#MULTIPLICACION
multiplicacion = 2*3
print(multiplicacion) 
multiplicacion = numero_entero*numero_decimal
print(multiplicacion)

#POTENCIA (exponenciacion es decir elevar un numero a otro, y el modulo)
"""EL MODULO ES EL RESIDUO DE UNA DIVISION, ES DECIR SI DIVIDO 11%2
(NOS DEVUELVE EL RESIDUO DE HACER LA DIVISION 11%2 VEREMOS QUE ES UTIL PARA MUCHAS COSAS, ESTE OPERADOR ES BASTANTE UTIL) """
potencia = 2**3 
modulo = 11%2 
print(potencia) 
print(modulo)

"""BUENO ESTOS SERIAN OPERADORES ARITMETICOS MAS BASICOS
SON IMPORTANTES SABER LO UTILIZAREMOS EN NUESTROS PROGRAMAS (Aqui termina el tema 1)"""


#tema 2, TIPOS DE DATOS DE (TEXTO)
texto = "Esta es nuestra frase" 
text = "Texto 'entre comillas' chimba" 
textt = 'Texto "entre comillas" chimba' 
txt = 'Hola'

print(texto)
print(text)
print(textt)
print(txt) 

#TEXTO CON FORMATO
texto_con_formato = """Esto es un texto 
con formato
"""
print(texto_con_formato) 


"""(BUENO LO QUE HICIMOS EN EL TEMA 2)

ESTA ES NUESTRA FRASE
---> NO SE MUESTRAN NINGUNAS COMILLAS EN LA (CONSOLA) PORQUE NO HEMOS PUESTO

Texto 'entre comillas' chimba
---> AQUI SE MUESTRAN LAS COMILLAS SIMPLES, PORQUE LAS TENEMOS AQUI DENTRO EN LA (CONSOLA)

Texto "entre comillas" chimba
---> AQUI MUESTRA LAS COMILLAS DOBLES, EN LA (CONSOLA)

Hola
---> AQUI SE MUESTRA SIMPLEMENTE ESTE TEXTO, QUE HEMOS DECLARADO SIMPLEMENTE PORQUE LO COLOCAMOS CON COMILLAS SIMPLES 


(AQUI ES PARA VER TEXTO CON FORMATO)

Esto es un texto 
con formato
---> ME VA SALIR EN LA CONSOLA CON EL ESPACIO CON EL SALTO DE LINEA 

(Aqui termina el tema 2) """   