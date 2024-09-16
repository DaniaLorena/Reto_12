# Reto_12

### Punto 1
> Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

Endswith | 
------------- |
Se utiliza para comprobar si una cadena termina con una subcadena específica. El método endswith() en Python devuelve True si la cadena termina con el valor especificado; de lo contrario, False.|
- Sintaxis
```python
cadena.endswith(subcadena[, inicio[, fin]])
```
- Ejemplo
```python
texto = "¡Hola, mundo!"
resultado = texto.endswith("mundo!")  # Verifica si termina con "mundo!"
print(resultado)  # Esto imprimirá True

resultado = texto.endswith("Hola")  # Verifica si termina con "Hola"
print(resultado)  # Esto imprimirá False
```
Startswith | 
------------- |
Se utiliza para verificar si una cadena comienza con un prefijo específico. Devuelve True si la cadena comienza con el prefijo especificado; de lo contrario, devuelve False.|
- Sintaxis
```python
string.startswith(valor, comienzo, fin)
```
- Ejemplo
```python
txt = "Bienvenido al curso de Python"

x = txt.startswith("Bien", 7, 20)

print(x)

```
Isalpha | 
------------- |
Se utiliza para verificar si una cadena contiene únicamente caracteres alfabéticos (letras) y no está vacía. Devuelve True si todos los caracteres en la cadena son letras, de lo contrario, devuelve False. Los espacios en blanco, números u otros caracteres especiales causarán que este método devuelva False.|
- Sintaxis
```python
cadena.isalpha()

```
- Ejemplo
```python
cadena = "Python3"
resultado = cadena.isalpha()
print(resultado)  # False

```
Isalnum | 
------------- |
Se utiliza para verificar si todos los caracteres en una cadena son alfanuméricos. Los caracteres alfanuméricos son aquellos que son letras (alfabéticas) o números (dígitos). Este método devuelve True si todos los caracteres en la cadena son alfanuméricos y False si la cadena contiene al menos un carácter que no es alfanumérico.|
- Sintaxis
```python
cadena.isalnum()
```
- Ejemplo
```python
texto = "Python123"
resultado = texto.isalnum()
print(resultado)  # True, ya que todos los caracteres son alfanuméricos

texto = "Python 123"
resultado = texto.isalnum()
print(resultado)  # False, ya que hay un espacio en blanco que no es alfanumérico

```
Isdigit| 
------------- |
Se utiliza para verificar si todos los caracteres de una cadena son dígitos. Devuelve True si todos los caracteres de la cadena son dígitos, de lo contrario, devuelve False.|
- Sintaxis
```python
cadena.isdigit()

```
- Ejemplo
```python
txt = "40700"

x = txt.isdigit()

print(x)

```
Isspace | 
------------- |
Se utiliza para verificar si una cadena de caracteres contiene solo espacios en blanco. Devuelve True si todos los caracteres de la cadena son espacios en blanco (como espacios, tabulaciones o saltos de línea), y False si la cadena contiene al menos un carácter que no es un espacio en blanco.|
- Sintaxis
```python
cadena.isspace()
```
- Ejemplo
```python
frase = "Esta es una prueba"
palabras = frase.split()

for palabra in palabras:
    if palabra.isspace():
        print(f"'{palabra}' contiene solo espacios en blanco.")
    else:
        print(f"'{palabra}' no contiene solo espacios en blanco.")

```
Istitle | 
------------- |
Se utiliza para verificar si una cadena tiene un formato de título. Una cadena se considera que está en formato de título si todas las palabras en la cadena comienzan con una letra mayúscula y el resto de las letras son minúsculas. Si la cadena está vacía o no contiene ninguna letra mayúscula inicial, el método istitle() devuelve False.|
- Sintaxis
```python
cadena.istitle()
```
- Ejemplo
```python
cadena = "Hola Mundo"
resultado = cadena.istitle()
print(resultado)  # True

```
Islower | 
------------- |
Se utiliza para verificar si todos los caracteres en una cadena están en minúsculas. Retorna True si todos los caracteres son letras minúsculas y False si la cadena contiene al menos un carácter en mayúsculas o algún otro tipo de carácter (como números o símbolos).|
- Sintaxis
```python
cadena.islower()
```
- Ejemplo
```python
# Ejemplo 1: Cadena en minúsculas
cadena1 = "hola mundo"
resultado1 = cadena1.islower()
print(resultado1)  # True

# Ejemplo 2: Cadena con mayúsculas
cadena2 = "Hola Mundo"
resultado2 = cadena2.islower()
print(resultado2)  # False

# Ejemplo 3: Cadena con números y símbolos
cadena3 = "123abc"
resultado3 = cadena3.islower()
print(resultado3)  # True, ya que solo verifica letras

```
Isupper | 
------------- |
Determina si todos los caracteres en una cadena están en mayúsculas (letras mayúsculas).|
- Sintaxis
```python
cadena.isupper()
```
- Ejemplo
```python
texto = "HOLA MUNDO"
resultado = texto.isupper()
print(resultado)  # Resultado: True

```
### Punto 2
> Procesar el archivo y extraer:
> - Cantidad de vocales
> - Cantidad de consonantes
> - Listado de las 50 palabras que más se repiten

```python
with open ("mbox.txt") as file_object:
    leer = file_object.read()

def num_vocales (leer):
    num_vocales : int = 0
    vocales = "aeiouáéíóúAEIOU"
    for letra in leer:
        if letra in vocales:
            num_vocales +=1
    print (num_vocales)


def num_consonantes (leer):
    num_consonantes : int = 0
    consonante :str ="bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    for letra in leer:
        if letra in consonante:
            num_consonantes+=1
    print (num_consonantes)

```
