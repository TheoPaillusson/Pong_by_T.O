import turtle, winsound
from playsound import playsound

wn = turtle.Screen()
wn.title("Pong by T.O")
wn.bgcolor("black")

wn.setup(width=800, height=600)
wn.tracer(0)

# joueur 1- OK
joueur_1 = turtle.Turtle()
joueur_1.speed(0)
joueur_1.shape("square")
joueur_1.color("white")
joueur_1.shapesize(stretch_wid=5, stretch_len=1)
joueur_1.penup()
joueur_1.goto(-350, 0)

# joueur 1 - fonctions de déplacement
def joueur_1_haut():
    y = joueur_1.ycor()
    y += 20
    joueur_1.sety(y)

def joueur_1_bas():
    y = joueur_1.ycor()
    y -= 20
    joueur_1.sety(y)

# joueur 1 - définition OK
joueur_2 = turtle.Turtle()
joueur_2.speed(0)
joueur_2.shape("square")
joueur_2.color("white")
joueur_2.shapesize(stretch_wid=5, stretch_len=1)
joueur_2.penup()
joueur_2.goto(350, 0)

# joueur 2 - déplacement
def joueur_2_haut():
    y = joueur_2.ycor()
    y += 20
    joueur_2.sety(y)

def joueur_2_bas():
    y = joueur_2.ycor()
    y -= 20
    joueur_2.sety(y)

# balle - définition OK
balle = turtle.Turtle()
balle.speed(0)
balle.shape("square")
balle.color("white")
balle.shapesize(stretch_wid=1, stretch_len=1)
balle.penup()
balle.goto(0, 0)
balle.dx = 0.25
balle.dy = 0.25

# score
score_1 = 0
score_2 = 0

# affichage
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("J 1:{}  J 2:{}".format(score_1, score_2), align="center", font=("Courier", 24, "bold"))

# contrôles du clavier
wn.listen()
wn.onkeypress(joueur_1_haut, 'z')
wn.onkeypress(joueur_1_bas, 's')
wn.onkeypress(joueur_2_haut, 'Up')
wn.onkeypress(joueur_2_bas, 'Down')

# BOUCLE PRINCIPALE
while True:
    wn.update()

    # faire bouger la balle
    balle.sety(balle.ycor() + balle.dy)
    balle.setx(balle.xcor() + balle.dx)
    
    # frontières pour la balle
    if balle.ycor()> 290: # frontière du haut
        balle.dy *= -1
        playsound('D:\CODE\Workplace folder VS\scripts\myscripts\pong by T.O\hit.wav')

    if balle.ycor()< -290: # frontière du bas
        balle.dy *= -1
        playsound('D:\CODE\Workplace folder VS\scripts\myscripts\pong by T.O\hit.wav')

    if balle.xcor() > 390: # reset à droite
        playsound('D:\CODE\Workplace folder VS\scripts\myscripts\pong by T.O\point.wav')
        balle.goto(0, 0)
        balle.dx *= -1
        score_1 = score_1 + 1
        pen.clear()
        pen.write("J 1:{}  J 2:{}".format(score_1, score_2), align="center", font=("Courier", 24, "bold"))


    if balle.xcor() < -390: # reset à gauche
        playsound('D:\CODE\Workplace folder VS\scripts\myscripts\pong by T.O\point.wav')
        balle.goto(0, 0)
        balle.dx *= 1
        score_2 = score_2 + 1
        pen.clear()
        pen.write("J 1:{}  J 2:{}".format(score_1, score_2), align="center", font=("Courier", 24, "bold"))

    # collision avec les joeurs
    if (balle.xcor() < -340 and balle.xcor() > -350) and (balle.ycor() < joueur_1.ycor() + 40 and balle.ycor() > joueur_1.ycor() -40):
        balle.setx(-340)
        balle.dx *= -1

    if (balle.xcor() > 340 and balle.xcor() < 350) and (balle.ycor() < joueur_2.ycor() + 40 and balle.ycor() > joueur_2.ycor() -40):
        balle.setx(340)
        balle.dx *= -1