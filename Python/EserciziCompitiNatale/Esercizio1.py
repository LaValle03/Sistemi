import random
import string


scelta = input("0- Esci\n1- Password semplica\n2- Password complessa\n")
scelta = int(scelta)

while scelta != 0:

    if scelta == 1 :
        lettere = string.ascii_letters
        password = ''.join(random.choice(lettere) for i in range(8)) 
        print(password)

    if scelta == 2 :
        lettere = string.ascii_letters + string.punctuation
        password = ''.join(random.choice(lettere) for i in range(20)) 
        print(password)

    scelta = input("0- Esci\n1- Password semplica\n2- Password complessa\n")
    scelta = int(scelta)
    


print("Fine programma")