# Poo_reto_01
## 1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

\
 Para llegar a la solución de este ejercicio utilicé una funcion que reciba 3 parametros, dos numeros y un operador en forma de string para realizar la operación requerida en cada paso. Luego, crear 4 if que lea el operador entregado y realice la operacion correspondiente entre los dos numeros


```python
#1. Calculadora Simple

def calculadora(x,op,y):
    print(f'{x} {op} {y} \n')
    #suma
    if op == '+':
        return x + y
    
    #resta
    if op == '-':
        return x - y
    
    #multiplicación
    if op == '*':
        return x * y
    
    
    #división
    if op == '/':
        return x/y
```

## 2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.
\
 Para este caso simplemente utilicé un iterador que compruebe las letras utilizando un for y un if comparando la primera letra y la ultima; aumentando y disminuyendo hasta que la condición sea falsa para acabar el programa, optimizando el tiempo.


```python
def palindromo(palabra):
    
    n = len(palabra)
    
    for i in range(n//2):
        if (palabra[i] != palabra[n-1-i]):
            return False
        
    return True

```

## 3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

\
En este problema fue necesario usar 2 funciones, una que compruebe si un numero es primo y otro que agregue en una lista aquellos que lo seán. Para esto hallé un metodo que comprueba si un numero es primo utilizando una operación de modulo hasta cierto punto para utilizar menos tiempo. Luego de ello la segunda función comprueba cada numero, agregandolo en la lista si este cumple con la condición de ser primo lo agrega a una lista previamente creada.

```python
def es_primo(n):

  for k in range(2,int(n**0.5)+1):
    if((n%k)== 0):
      return False

  return True

def lista_primos(N):
    n = len(N)
    X = []
    
    for i in range(n):
        if es_primo(N[i]):
            X.append(N[i])
            
    return X

```
 
## 4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

\
Para este problema utilizando un ciclo se puede comprobar cada suma cambiando el valor de una variable, previamente iniciada en 0, si es que la suma consecutiva de los dos valores es mayor que ella.

```python
def suma_consecutiva(M):
    n = len(M)
    x = 0
    
    for i in range(n-1):
        sum = M[i]+M[i+1]
        if sum > x:
            x = sum
            
    return x
```

## 5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

\
En este caso ordeno cada palabra en orden alfabetico para que sea mas sencillo comparar las palabras, y de esta forma agregarlas a una lista si es que son iguales

```pyhton
def mismas_letras(palabras):
  resultado = []
  n = len(palabras)
    
  for i in range(n):
    for j in range(i + 1, n):
    
      if sorted(palabras[i]) == sorted(palabras[j]):
        if palabras[i] not in resultado:
          resultado.append(palabras[i])

        if palabras[j] not in resultado:
          resultado.append(palabras[j])

  return resultado

```









