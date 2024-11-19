#4 Suma Consecutiva

def suma_consecutiva(M):
    n = len(M)
    x = 0
    
    for i in range(n-1):
        sum = M[i]+M[i+1]
        if sum > x:
            x = sum
            
    return x


if __name__ == '__main__':
    x = [165,2,3,4,500,6,7,8139293,9]

    print(suma_consecutiva(x))