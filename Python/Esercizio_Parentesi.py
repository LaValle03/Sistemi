def push_(stack, element):
    stack.append(element)

def pop_(stack):
    return stack.pop()

def is_open(elemento):
    if elemento == '(' or elemento== '[' or elemento == '{' : 
        return True
    else:
        return False

def is_close(elemento):
    if elemento == ')' or elemento == ']' or elemento == '}':
        return True
    else:
        return False

def trovaErrori(stringa):
    errore = False
    pila = []

    for elemento in stringa:
        if is_open(elemento):
            push_(pila,elemento)

        if is_close(elemento):
            if elemento == ")":
                if pop_(pila) != '(':
                    errore = True
                    break

            elif elemento == "]":
                if pop_(pila) != '[':
                    errore = True
                    break

            elif elemento == "}":
                if pop_(pila) !='{':
                    errore = True
                    break

    open = 0
    close = 0

    for elemento in stringa:
        if is_open(elemento):
            open = open + 1 
        
        if is_close(elemento):
            close = close + 1

    if (open != close):
        errore = True


    if (errore):
        print("L'espressione inserita ha degli errori")
    else:
        print("L'espressione inserita è corretta")



def main():
    stringa = input()
    trovaErrori(stringa)

if __name__ == "__main__":
    main()