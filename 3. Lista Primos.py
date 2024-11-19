#3. Lista Primos

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


if __name__ == '__main__':
    lista = [2,25,43,41,12,97]
    print(lista_primos(lista))
