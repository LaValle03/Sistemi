import turtle       #importo della libreria turtle

tartaruga = turtle.Turtle ()        #creo una variabile di tipo turtle
tartaruga.color ("red")             #assegno alla tartaruga il colore rosso
tartaruga.begin_fill()              #comincio a riempire il poligono
lati = (int) (input("Numero di lati: "))        #input del numero di lati

for k in range (lati):              #for che disegna i lati del poligono
    tartaruga.forward(50)           #disegno una linea
    tartaruga.left(360 / lati)      #giro a sinistra di x gradi e disegno un'altro lato

tartaruga.end_fill()                #finisco di riempire il poligono
