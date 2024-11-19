# 2. Palabra Palindromo

def palindromo(palabra):
    
    n = len(palabra)
    
    for i in range(n//2):
        if (palabra[i] != palabra[n-1-i]):
            return False
        
    return True


if __name__ == '__main__':
    
    pal = input('Ingrese la palabra:  ')

    print(palindromo(pal))