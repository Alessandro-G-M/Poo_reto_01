#1. Calculadora Simple

def calculadora(x,op,y):
    print(f'{x} {op} {y} \n')
    #suma
    if op == '+':
        return x + y
    
    #resta
    elif op == '-':
        return x - y
    
    #multiplicación
    elif op == '*':
        return x * y
    
    
    #división
    elif op == '/':
        return x/y
        
    else: return 'Operación no valida'
    
if __name__ == "__main__":

    num1 = int(input(''))
    operador = input('')
    num2 = int(input(''))


    print(calculadora(num1,operador,num2))
