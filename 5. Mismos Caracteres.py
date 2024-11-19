#5 Mismos Caracteres

def mismos_caracteres(palabras):
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


if __name__ == '__main__':
    elementos = ['arroz','zorra','rozar','leon','elefante']
    
    print(mismos_caracteres(elementos))