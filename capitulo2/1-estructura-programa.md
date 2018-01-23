# Estructura general de un programa

Nuestros programas tendrán la siguiente estructura mínima:

```python
import sys

def main():
    print('¡Hola, mundo!')

# llamar al punto de inicio del programa
if __name__ == '__main__':
    main()
```

Veamos qué hace cada línea:

```python
import sys
```
Esta línea permite usar el módulo básico del sistema Python, *sys*, en nuestros programas. *sys* tiene lista una gran serie de servicios útiles a muchos programas. En vez de re-escribir la rueda cada vez, podemos apoyarnos de sus bondades y **reutilizar** código.

```python
def main():
```
Define el punto de inicio de nuestros programas. El punto de inicio de los programas en la mayoría de los lenguajes de programación se llama *main*.

```python
print('¡Hola, mundo!)
```
Es el cuerpo de nuestro programa. En este ejemplo, nuestro programa sólo imprime **¡Hola, mundo!** en la salida estándar.

```python
# llamar al punto de inicio del programa
```
Es un comentario. Los comentarios, estrictamente, no son parte del programa. Podemos decir que son "meta elementos". Nos ayudan a esclarecer a los lectores de nuestro código qué hace este, o a justificar por qué se tomaron ciertas decisiones.

```python
if __name__ == '__main__':
    main()
```
Instruye al intérprete de Python que el punto de inicio del programa se llama main().