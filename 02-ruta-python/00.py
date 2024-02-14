"""
    00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO:
    EJERCICIO:
    - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
    - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
    - Crea una variable (y una constante si el lenguaje lo soporta).
    - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""

# https://python.org ---> Página oficial de Python

# Así se realiza un comentario en una línea

"""
Esto también es un comentario en varias líneas, se suele usar para documentar una función, o un resumen general del código
"""

"""
Esto también es un comentario en varias líneas, '''comentario''', lo realizo dentro de las comilas dobles porque tengo auto format de código
"""

my_variable = "Mi variable"  # Declaro una variable
my_variable = (
    "Nuevo valor de mi variable"  # Piso la variable y toma ahora el nuevo valor
)

MY_CONSTANT = "Mi constante"  # por convención

my_int = 5
my_float = 5.9
my_bool = True
my_bool = False
my_string = "Esto es una cadena de texto"
my_other_string = "Mi otra cadena de texto"

print("¡Hola, Python!")

print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))
