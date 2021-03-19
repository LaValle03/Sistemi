import turtle
import random
import time

#costanti per lo schermo
LUNGHEZZA = 600
ALTEZZA = 600


#inizializzazioni di variabili di tipo turtle

#schermo
schermo = turtle.Screen()
schermo.title("SNAKE")
schermo.bgcolor("green")

schermo.setup(width = LUNGHEZZA, height = ALTEZZA)
schermo.tracer(0)

#snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("blue")
snake.penup()
snake.goto(0,0)
snake.direzione = "destra"

#mela
mela = turtle.Turtle()
mela.speed(0)
mela.shape("circle")
mela.color("red")
mela.penup()
mela.goto(100,100)

#funzioni per cambiare direzione
def up():
    if snake.direzione != "down":
        snake.direzione = "up"

def sinistra():
    if snake.direzione != "destra":
        snake.direzione = "sinistra"
    
def destra():
    if snake.direzione != "sinistra":
        snake.direzione = "destra"

def down():
    if snake.direzione != "up":
        snake.direzione = "down"

#funzione per muovere lo snake
def salta():
    if snake.direzione == "up":
        snake.sety(snake.ycor() + 20)
    
    if snake.direzione == "down":
        snake.sety(snake.ycor() - 20)

    if snake.direzione == "sinistra":
        snake.setx(snake.xcor() - 20)

    if snake.direzione == "destra":
        snake.setx(snake.xcor() + 20)

#funzione di reset per lo snake
def reset():
    snake.goto(0, 0)
    snake.direzione = "destra"
    for coda in VetCoda:
        coda.goto(1000,1000)
    VetCoda.clear()

    time.sleep(1)


#cambio della direzione dello snake con la pressione dei tasti wasd
schermo.listen()
schermo.onkeypress(up, "w")
schermo.onkeypress(down, "s")
schermo.onkeypress(sinistra, "a")
schermo.onkeypress(destra, "d")


VetCoda = []

while True:
    schermo.update() #aggiornamento dello snake con le coordinate attuali

    #se lo snake esce dallo schermo il gioco ricomincia
    if snake.xcor() > (LUNGHEZZA / 2 - 10) or snake.xcor() < -(LUNGHEZZA / 2 - 10) or snake.ycor() > (ALTEZZA / 2 - 10) or snake.ycor() < -(ALTEZZA / 2 - 10):
        reset()
    

    #allungare il serpente e spostare la mela
    if snake.distance(mela) < 20:
        x = random.randint(-(LUNGHEZZA / 2 - 30), LUNGHEZZA / 2 - 30)
        y = random.randint(-(ALTEZZA / 2 - 30), ALTEZZA / 2 - 30)
        mela.goto(x, y)

        coda = turtle.Turtle()
        coda.speed(0)
        coda.shape("square")
        coda.color("blue")
        coda.penup()
        VetCoda.append(coda)


    #controllo se la testa del serpente tocca la coda, se è così il gioco ricomincia
    for k in range(len(VetCoda) - 1, 0, -1):
        x = VetCoda[k - 1].xcor()
        y = VetCoda[k - 1].ycor()
        VetCoda[k].goto(x, y)
    
    if len(VetCoda) > 0:
        x = snake.xcor()
        y = snake.ycor()
        VetCoda[0].goto(x, y)

    salta()


    for coda in VetCoda:
        if coda.distance(snake) < 20:
            reset()

    if len(VetCoda) >= (LUNGHEZZA * ALTEZZA) / 20:
        print("HAI VINTO")
        reset()
    time.sleep(0.1)
