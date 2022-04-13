import turtle
import random

tim = turtle.Turtle()
tim.color("black")
screen = turtle.Screen()

##height and width of the shell
height = 600
width = 700
screen.setup(width,height)

def draw_star(side):
    tim.begin_fill()
    for i in range(side):           #drawing a star
        tim.fd(100)
        tim.right(180-(180/side))
        tim.fd(100)
    tim.end_fill()

for i in range(10):#the amount of stars you want to draw
    random_x = random.randint(-width/2,width/2)
    random_y = random.randint(-height/2,height/2)
    tim.penup()
    tim.goto(random_x, random_y)
    tim.pendown()
    random_side = random.randint(5,8)#the amount of sides you want in each star
    draw_star(random_side)

#just make sure you open fullscreen mode first
