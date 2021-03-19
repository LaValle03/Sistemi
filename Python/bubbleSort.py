#bubble sort di un vettore intero
vet = [1, 7, 0, 9, 8] 

print ("----VETTORE 1----")
print ("VETTORE INIZIALE: ", vet)

for k in range(len(vet)-1):                         # for (int k = 0; k < dim - 1; k++) {
    for j in range (len(vet)-k-1):                  # for (int j = 0, j < dim - k - 1; j++) {
        if vet[j] > vet[j+1]:                       # if (vet[j] > vet[j+1]) {
            vet[j], vet[j+1] = vet[j+1], vet[j]     # funzione scambio

print ("VETTORE ORDINATO: ", vet)


#bubble sort di un vettore intero casuale
import random                                       #importo di una libreria con IMPORT
vet2 = []                                           #vettore vuoto

for k in range(0, 10):                              #for che assegna a 10 celle del vettore un valore casuale da 0 a 100
    vet2.append (random.randint(0, 100))

print ("----VETTORE 2----")
print ("VETTORE CASUALE INIZIALE: ", vet2)

for k in range(0, len(vet2)):                       #bubble sort                            
    for j in range (0, len(vet2)-k-1):                      
        if vet2[j] > vet2[j+1]:                       
            vet2[j], vet2[j+1] = vet2[j+1], vet2[j]

print ("VETTORE CASUALE ORDINATO: ", vet2)


#altro modo per bubble sort di un vettore intero casuale
import random
vet3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for k in range (0, 10):
    vet3[k] = random.randint(0, 100)

print ("----VETTORE 3----")
print ("VETTORE CASUALE INIZIALE: ", vet3)

for k in range(0, len(vet3)):                       #bubble sort                            
    for j in range (0, len(vet3)-k-1):                      
        if vet3[j] > vet3[j+1]:                       
            vet3[j], vet3[j+1] = vet3[j+1], vet3[j]

print ("VETTORE CASUALE ORDINATO: ", vet3)