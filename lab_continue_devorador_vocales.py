# Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:
# •	Un bucle for.
# •	El concepto de ejecución condicional (if-elif-else).
# •	La sentencia continue.
# Tu programa debe:
# •	Pedir al usuario que ingrese una palabra.
# •	Utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos
#  sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
# •	Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
# •	Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.
# Prueba tu programa con los datos que le proporcionamos

from ast import Continue
from difflib import HtmlDiff
from multiprocessing import Condition


user_word = input("Ingrese una palabra:")
user_word = user_word.upper()
user_word2 = ""
# print(user_word)
for i in user_word:
    if i == "A":
        continue
    elif i == "E":
        continue
    elif i == "I":
        continue
    elif i == "O":
        continue
    elif i == "U":
        continue
    else:
        user_word2 += i
for i in user_word2:
    print(i,end = "\n")
