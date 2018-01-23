# Elementos básicos de programación

En esta sección veremos cuáles son los elementos más básicos del lenguaje de programación python.

## Palabras reservadas

Los lenguajes de programación por lo general tienen varias palabras reservadas, que no son más que
palabras que no pueden utilizarse como nombres de variables, al tener un significado especial para
el lenguaje de programación. Ejemplos de palabras reservadas en Python:

- import
- from
- if
- for
- def
- while

## Literales

Los literales son notaciones para representar valores dentro del código fuente de un lenguaje de programación.
Por ejemplo, **569**, **93.22**, y **'¡Hola, mundo!'** son literales.

## Variables

Las variables se utilizan para almacenar data, con el fin de esta ser manipulada por el programa. Cada variable
debe tener un nombre. Los nombres de las variables en python contienen al menos un caracter, que puede ser cualquier
letra del alfabeto inglés, en mayúscula o en minúscula; también, un dígito de 0-9; por último, el underscore(_). El
nombre de una variable no puede iniciar con un número.

Los siguientes son nombres válidos de variables:

- contador
- acumulador
- posicion_actual
- variable1
- _nombre

Los siguientes son nombres inválidos de variables:

- 1valor
- $costo
- %porcentaje

## Tipos de datos

Todos los datos pertenecen a cierta familia. Los números enteros son de la familia "números enteros", los números
decimales son de la familia "números decimales", y los textos son de la familia "cadenas de caracteres".

### Ejemplo de números enteros:
- 5
- 10
- 559

### Ejemplo de números decimales:
- 27.59
- 50.29
- 19.33

### Ejemplos de cadenas de caracteres
- 'Hola mundo'
- 'En la noticia de hoy'
- '6549'

Fíjate muy bien en el último ejemplo de cadenas de caracteres. Aunque perfectamente se ve el número 6549, el tipo de dato
de ese valor es realmente *cadena de caracteres*, al estar rodeado de comillas simples. Si no le pones las comillas simples,
el lenguaje de programación dicta que el literal es un número entero. 

Si el literal fuera 'Hola', y omites las comillas simples, el lenguaje de programación dictaría que *Hola* es una variable de 
tu programa. Lo más probable es que produzcas un error.

## Operadores aritméticos

Sin operadores matemáticos, un programa de computadora sería muy limitado. Python soporta los siguientes operadores:

- *: multiplicación
- /: división
- %: residuo
- +: suma
- -: resta
- **: potencia

## Operadores lógicos (booleanos)

El concepto es sencillo. Habilitan a los lenguajes de programación para controlar el flujo de ejecución de los programas.
Los operadores lógicos más sencillos son:

### NOT

Niega el valor de verdad de una expresión.


| not | Valor | Resultado |
|--|--|--|
| not | True |  False |
| not | False |  True |

### AND

Operador booleano binario. Produce un valor booleano verdadero si y sólo si los valores de los operandos son verdaderos.


| and | operando1 | operando2 | Resultado |
|--|--|--|--|
| and | True |  True | True|
| and | True |  False | False|
| and | False |  True | False|
| and | False |  False | False|

### OR

Operador booleano binario. Produce un valor booleano verdadero falso si y sólo si los valores booleanos de sus dos operandos son falsos.


| or | operando1 | operando2 | Resultado |
|--|--|--|--|
| or | True |  True | True|
| or | True |  False | True|
| or | False |  True | True|
| or | False |  False | False|

## Expresiones

Una expresión es una combinación de literales, variables, operadores y otros elementos de lenguajes de programación, que
produce un resulado. También se puede decir que una expresión *se evalúa ella misma* y produce un valor.

### Ejemplos de expresiones:

- `n > 0`. Compara n con 0, y si el primero es mayor, la expresión se evalúa al valor de verdad Verdadero. De lo contrario, se evalúa a falso.
- `5 + 8/2`. Divide 8 / 2, produciendo 4, y luego se lo suma a 5, produciendo el valor final 9.
- `a == True or b == False`. Evalúa `a == True` y `b == False` por separado. Luego, aplica el operador lógico OR sobre el resultado de ambas
  expresiones. El resultado de la aplicación del operador será el resultado de la expresión.