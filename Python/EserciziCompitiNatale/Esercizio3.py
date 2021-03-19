def fibonacci(numero):
    if numero < 0 :
        return - 1
    
    if numero == 0 :
        return 0
    elif numero == 1 :
        return 1
    else:
        return (fibonacci(numero - 1) + fibonacci (numero - 2))
    

for k in range (20):
    print(fibonacci(k))

