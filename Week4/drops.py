import turtle
import subprocess
from random import randint 


turtle.setup(800 ,800)
wn = turtle.Screen()
wn.bgcolor("navy")
wn.title("CLICK ANYWHERE YOU LIKE!")

sammy = turtle.Turtle()
sammy.hideturtle()



colorArray = ["blue", "medium blue", "deep sky blue", "dark cyan", "deep sky blue", "sky blue", "sea green", "cadet blue", "steel blue", "turquoise", "aquamarine", "yellow", "deep pink", "red", "indian red", "salmon", "gold", "tomato", "deep pink"]

audio_file = "/Users/svonhauske/Desktop/Drop.wav"

def ripple1(x, y):
    sammy.penup()
    radius = 15
    sammy.speed(0)
    return_code = subprocess.Popen(["afplay", audio_file])
    pSize = 3.1
    ringNumber = randint(10,30)
    for rings1 in range(0, ringNumber):
        randomColor = randint(0, 18)
        sammy.color(colorArray[randomColor])
        sammy.pensize(pSize)
        sammy.penup()
        sammy.goto(x, y - radius)
        sammy.pendown()
        sammy.circle(radius)
        sammy.penup()
        radius += 10
        pSize -=.1

wn.onclick(ripple1)

turtle.mainloop()