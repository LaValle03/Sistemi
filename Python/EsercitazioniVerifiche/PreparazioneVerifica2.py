import csv 

def leggiFile (dizionario):
    with open("Volo_drone.csv", newline="", encoding="ISO-8859-1") as file:
        csv_reader = csv.reader(file, delimiter=',')

        for riga in csv_reader:
            dizionario[riga[0]] = (riga[1], riga[2], "")

def leggiAnomalie (dizionario):
    with open("Anomalie_drone.csv", newline="", encoding="ISO-8859-1") as file:
        csv_reader = csv.reader(file, delimiter=',')
        
        for riga in csv_reader:
            dizionario[riga[0]] = (dizionario[riga[0]][0], dizionario[riga[0]][1], riga[1])


        

def main():
    dizionario = {}

    leggiFile(dizionario)

    leggiAnomalie(dizionario)
    
    print(dizionario)


        

main()