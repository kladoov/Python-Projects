#### ***Operadores de Python ordenados por prioridad***
- \*\* = potencia (ej. 2 \*\* 3 es 2 \* 2 \* 2 = 8)
- +, - = unarios afecta solo a un numero (ej. -2 \*\* 2 se interpreta como -(2 \*\* 2) = -4)
- \*, /, //, % = multiplicación, división, división entera, módulo/resto
- +, - = suma y resta convencional
#### ***Operadores logicos
- and = si ambos operandos son verdaderos, la condición es verdadera, por ejemplo, (True and True) es True
- or =  si alguno de los operandos es verdadero, la condición es verdadera, por ejemplo, (True or False) es True
- not = devuelve False si el resultado es verdadero y devuelve True si es falso, por ejemplo, not True es False
#### ***Comparaciones***
- `==` Operador de igualdad 
- `!=` Operador de desigualdad
- `>` mayor que
- `<` menor que
- `>=` mayor o igual que
- `<=` menor o igual que
#### ***Conversión de tipos***
- ``float("23.5")`` = convierte un texto en número flotante
- ``int("2")`` = convierte un texto en un número entero
- ``str(22)`` = convierte un numero entero en texto
- ``type(var)`` = indica el tipo de dato de la variable pasada por argumento
#### ***Variables***
- Sintaxis correcta para variables y funciones = my\_variable o myVariable
- Cuidado con las palabras clave (reservadas) = if, while, and, True, etc.
- Ej. year = 2026, name = "Kladov", money = 1.25, ugly = False
- Operadores abreviados = (x = x \* 2  ==  x \*= 2) 
#### ***Comentarios***
- \# No hay nada que explicar, esto es un comentario
#### ***Funciones reservadas***
- ``round`` = permite redondear un valor decimal. Ej. round(2.3452) = 2, round(2.3452, 2) = 2.35 
- ``min`` = devuelve el numero mas pequeño de una serie de argumentos. Ej. min(2, 3, 5) = 2
- ``max`` = devuelve el numero mas grande de una serie de argumentos. Ej. max(2, 3, 5) = 5
- ``input`` = interacción con el usuario, devuelve siempre una cadena cuidado con las conversiones. Ej. input("Dime algo.") o input()
- `string.upper()` = convierte la cadena en mayúsculas.
- `len(numbers)` = devuelve la longitud de una lista

#### ***print*** = Es una función integrada imprime/envía un mensaje específico a la pantalla/ventana de consola.
Se delimitan por comillas dobles "" o simples '', si se trabaja con compillas simples cuidado con los caracteres especiales (poner la \\).
Ejemplos:
- print("¡Hola, Mundo!");
- print();
- print("Hola, me llamo\\nAlex"); = Carácter de escape newline.
- print("Hola","me","llamo","Alex"); = Argumentos posicionales
- print("Mi nombre es", "Kladov.", end=" "); = Argumentos de palabra clave (agrega al final del texto) deben ir al final del argumento
- print("Mi", "nombre", "es", "Kladov.", sep="-") = Argumento de palabra clave (agrega - en cada posición)
- print("\*"\*5) = \*\*\*\*\* multiplica el texto según el numero de veces

#### ***Condiciones***
```
if years >= 18:
	print("Puedes beber")
elif years = 5:
	print("Wow tienes 5 añazos")
else:
	print("A dormir que mañana hay cole")
```

También se puede escribir si solo tiene una instrucción:
```
if years >= 18: print("Puedes beber")
elif years == 5: print("Wow tienes 5 añazos")
else: print("A dormir que mañana hay cole")
```
#### ***Bucles***
``while`` ejecuta una sentencia o un conjunto de sentencias siempre que una condición booleana especificada sea verdadera:
```
i = 0
while i < 5:
    print(i)
    i = i + 1
else:
    print(i) <-- Devolveria 5, rara vez se usa
```

``for`` ejecuta un conjunto de sentencias muchas veces; se usa para iterar sobre una secuencia:
```
for i in range(5):
	print("El valor de i es", i)
	pass = se pondría únicamente cuando no hay argumentos rara vez se usa también
else: 
	print(i) <-- Devolveria 4, rara vez se usa
```

`range` = Cuenta de 0 a 9 
- Pueden pasarse por argumentos range(2, 8, 3)
- Primer argumento: Número de inicio de la secuencia
- Segundo argumento: Número de fin de la secuencia
- Tercer argumento: Número que indica la diferencia entre cada número

``else`` se ejecuta después de que el bucle finalice su ejecución siempre y cuando no haya terminado con break

`break` = para la instrucción y continua con el flujo
`continue` = se usa para omitir el bloque actual y avanzar a la siguiente iteración

#### ***LISTAS***
Es un tipo de dato en Python que se utiliza para **almacenar múltiples objetos**. Es una **colección ordenada y mutable** de elementos separados por comas entre corchetes, por ejemplo:
`my_list = [1, None, True, "Soy una cadena", 256, 0]`

O una lista anidada:
`my_list = [1, 'a', ["lista", 64, [0, 1], False]]`

Usos:
- `numbers = [1, 2, 3, 4, 5]` = creación de la lista con valores
- `numbers = []` = crea una lista vacía
- `numbers[1] = 10` = permite asignar un valor
- `numbers[1] = numbers[4]` = permite copiar el contenido del índice 4 al 1
- `numbers[1]` = accede a la posición de un índice
- `len(numbers)` = muestra la longitud de la lista
- `del numbers[1]` = elimina el índice de la lista y su contenido``
- `numbers[-1] = 5` = se permiten índices negativos dentro de la lista para ir a la inversa
- `numbers.append(value)` = añade un valor nuevo al final de la lista
- `numbers.insert(location, value)` = añade un valor en cualquier posición y mueve los demás valores a la derecha
- `numbers.sort()` = ordena la lista de menor a mayor
- `numbers.reverse()` = invertir la lista
- `numero_mayor = numbers.max()` = devuelve el numero mayor de una lista

**(Slicing) Rebanadas poderosas = operación de seleccionar una parte de la lista**
- `list_1 = [1]`
- `list_2 = list_1[:]` = crea una copia independiente de `list_1` y la guarda en `list_2`
- `list_2 = list_1` = esto no crea una copia independiente si no que apuntan a la **misma posición de memoria**, mucho cuidado con esto

```
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] = copia el primer índice 1 y termina en el 3 sin incluir
```

```
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]` = copia el 3 índice hasta el final
new_list2 = my_list[:3]` = copia el primer índice hasta el 3 sin incluir
```

```
del my_list[1:3] = elimina el índice 1 hasta el 3 sin incluir
del my_list[:] = elimina todos los índices de la lista
del my_list = elimina la lista no su contenido, cuidado.
```

Python ofrece dos operadores muy poderosos, capaces de revisar la lista para verificar si un valor específico está almacenado dentro de la lista o no:
```
my_list = [0, 3, 12, 8, 2]
print(5 in my_list) = False
print(5 not in my_list) = True
```


**ARREGLOS BIDIMENSIONALES**
Una lista bidimensional es una lista que contiene otras listas, cada par de corchetes permite acceder a un nivel de la estructura:
```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2]) = 6 para acceder a una posicion en concreto

cube = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]
print(cube[0][1][0]) = 3 
```

#### ***FUNCIONES***
Una **función** es un bloque de código que realiza una tarea especifica cuando la función es llamada (invocada). Las funciones son útiles para hacer que el código sea reutilizable, que este mejor organizado, y más legible. Las funciones contienen parámetros y pueden regresar valores
```
def my_function():
	print("Hello!")
```

Se puede pasar información a las funciones utilizando parámetros. Las funciones pueden tener tantos parámetros como sean necesarios.
```
def saludar(name_1, name_2):
    print("Hola,", name_2)
    print("Hola,", name_1)

saludar("Sebastián", "Konrad")
```

Se puede utilizar la técnica de argumentos con palabras clave para asignar valores **predefinidos** a los argumentos:
```
def name(first_name, last_name="Pérez"):
    print(first_name, last_name)

name("Andy")                 # salida: Andy Pérez
name("Bety", "Rodríguez")    # salida: Bety Rodríguez

o

def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro(b="Sean Connery") # salida: Mi nombre es Sean Connery. James Bond.
```

Las funciones pueden devolver un valor con `return` ya sea un valor real o `None`.
**Nota**: una variable que existe fuera de una función tiene alcance dentro del cuerpo de la función.

 Se puede emplear la palabra clave reservada global seguida por el nombre de una variable para que el alcance de la variable sea global:
```
var = 2
print(var) # salida: 2

def return_var():
    global var
    var = 5
    return var

print(return_var()) # salida: 5
print(var) # salida: 5
```

Una función puede invocar otras funciones o incluso a sí misma. Cuando una función se invoca a si misma, se le conoce como **recursividad**, y la función que se invoca a si misma y contiene una condición de terminación (la cual le dice a la función que ya no siga invocándose a si misma) es llamada una función **recursiva**.

#### ***TUPLAS***
Son similares a las listas, pero tienen una diferencia fundamental: **no se pueden modificar una vez creadas** (son inmutables).
Se utilizan cuando quieras almacenar varios valores que no deberían cambiar.
- `tuple_1 = (1, 2, 4, 8)` = tupla con paréntesis
- `tuple_2 = 1., .5, .25, .125` = tupla sin paréntesis
- `one_elem_tuple_1 = ("uno", )` = tupla de un solo elemento, si no se pone la coma Python crea una variable
- `empty_tuple = ()` = tupla vacía
- `print(tuple_1[0])` = acceso a una tupla
- `print(len(tuple_1))` = muestra la longitud de la tupla
- `tuple.count(2)` = devuelve el numero de repeticiones del valor argumentado
- `t = tuple(my_list)` = crea una tupla según la lista

#### ***DICCIONARIOS***
Los **diccionarios (**`dict`**)** son estructuras de datos que permiten almacenar información mediante pares de **clave y valor (**`key: value`**)**.
- `persona = {"nombre": "Alex", "edad": 25}` = creación de un diccionario
- `persona["nombre"] o persona.get("nombre")` = acceso a un valor
- `persona["edad"] = 23` = modificar un valor
- `persona["ciudad"] = "Albacete" o persona.update({"ciudad": "Albacete"})` = añadir un nuevo elemento
- `del persona["ciudad"]` = eliminar un elemento

- `persona.items()` = devuelve todas las claves y valores
- `persona.values()` = devuelve todos los valores
- `persona.keys()` = devuelve todas las claves
- `persona.popitem()` = elimina el ultimo elemento
- `persona.copy()` = permite copiar un diccionario entero
- `colors_dictionary = dict(colors)` = crea un diccionario a partir de una tupla

```
  for clave, valor in persona.items(): = recorrer un diccionario
    print(clave, valor)
```

#### ***EXCEPCIONES***
Las **excepciones (**`exceptions`**)** son errores que se producen durante la ejecución de un programa y que pueden interrumpir su funcionamiento.
```
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    ('No se que hacer con.')    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')    
except:
    print('Ha sucedido algo extraño, ¡lo siento!')
    
# Tambien se pueden integrar multiples excepciones en una misma
except (ValueError, ZeroDivisionError):
```



























