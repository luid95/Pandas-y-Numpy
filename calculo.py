#https://docs.python.org/2/tutorial/modules.html


#Fibonacci numbers module

def fib(n):  #Write fibonacci series up to n
    a, b = 0, 1
    while(b <= n):
        print(b)
        a, b = b, a+b

def fib_list(n): # Return fibonacci seriesup to n
    result = []
    a, b = 0, 1
    while(b <= n):
        result.append(b)
        a, b = b, a+b
    return result


# Funcion calculadora
def calcular(operacion, valor1, valor2):
    calculo =0
    if(operacion == 'suma'):
        calculo = valor1 + valor2
       
    elif(operacion == 'resta'):
        calculo = valor1 - valor2
    
    elif(operacion == 'multiplicacion' or operacion == 'multiplicación' or operacion == 'multi'):
        calculo = valor1*valor2
    
    elif((operacion == 'division' or operacion == 'división') and valor2 != 0):
        calculo = valor1 / valor2
    
    return calculo