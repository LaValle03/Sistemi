def cripta (stringa):
    newStringa = ""
    for k in range (len(stringa)):
        newStringa = newStringa + "".join(chr(ord(stringa[k]) + 15))
    return newStringa

def decripta (stringa):
    newStringa = ""
    for k in range (len(stringa)):
        newStringa = newStringa + "".join(chr(ord(stringa[k]) - 15))
    return newStringa
    
    
print(cripta("CIAO A TUTTI"))
print(decripta("RXP^/P/cdccX"))