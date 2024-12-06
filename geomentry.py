import math,turtle
def daxis(x=300,y=None):#draw axis
    if y==None:
        y=x
    turtle.penup()
    turtle.goto(0,x)
    turtle.pendown()
    turtle.goto(0,-x)
    turtle.penup()
    turtle.goto(y,0)
    turtle.pendown()
    turtle.goto(-y,0)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
turtle.speed(0)
def eq(x):
    y=1/x
    return y
def eq2(x):
    y=x**-3
    return y
def eq3(x):
    y=x**-2
    return y

for i in range(-360,360,45):
    turtle.penup()
    turtle.goto(i,0)
    turtle.write(i)
def draw():
    for x in range(1,200):

        if x=='n':
            continue
        y=eq(x)
        turtle.penup()
        turtle.goto(x/10,y/10)
        turtle.dot(5,'blue')
    turtle.goto(0,0)

def draw1():
    for x in range(1,200):

        if x=='n':
            continue
        y=eq2(x)
        turtle.penup()
        turtle.goto(x/10,y/10)
        turtle.dot(5,'yellow')
    turtle.goto(0,0)

def draw2():
    for x in range(1,200):

        if x=='n':
            continue
        y=eq3(x)
        turtle.penup()
        turtle.goto(x/10,y/10)
        turtle.dot(5,'green')
    turtle.goto(0,0)

turtle.penup()
turtle.goto(300,300)
turtle.write('blue=1/x\nyellow=x**-3\ngreen= x**-2',font=('red',15))
    
daxis()       
draw()
draw1()
draw2()


