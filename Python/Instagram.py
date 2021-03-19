import csv


def leggiFile (dizionario):
    with open("instagram.csv", newline="", encoding="ISO-8859-1") as file:
        csv_reader = csv.reader(file, delimiter=',')

        for riga in csv_reader:
            dizionario[riga[0]] = dizionario[riga[0]] + int(riga[3])

def richiestaMese(dizionario, mese):
    numeroPost = 0

    with open("instagram.csv", newline="", encoding="ISO-8859-1") as file:
        csv_reader = csv.reader(file, delimiter=',')

        for riga in csv_reader:
            if mese == riga[0]:
                numeroPost = numeroPost + 1

    print(f"Numero di post: {numeroPost}\nLike totali: {dizionario[mese]}")


def main():
    dizionario = {"gennaio": 0, "febbraio" : 0, "marzo" : 0, "aprile" : 0, "maggio" : 0, "giugno" : 0, "luglio" : 0, "agosto" : 0, "settembre" : 0, "ottobre" : 0, "novembre" : 0, "dicembre" : 0}

    leggiFile(dizionario)

    mese = input("Inserisci un mese: ")
    richiestaMese(dizionario, mese)

    print(f"\nDIZIONARIO COMPLETO\n{dizionario}")

main()