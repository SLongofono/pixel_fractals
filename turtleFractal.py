import turtle
import random
import numpy.random as npr

HEIGHT = 960
WIDTH  = 960
BUFFER = 60
pointSets = {
    3:[(WIDTH//3, HEIGHT//3),((WIDTH*2)//3,HEIGHT//3),(WIDTH//2,(HEIGHT*2)//3)],
    4:[(WIDTH//4,HEIGHT//4),(WIDTH//4,(HEIGHT*3)//4),((WIDTH*3)//4,HEIGHT//4),((WIDTH*3)//4,(HEIGHT*3)//4)]
}

def doSetup():
    screen = turtle.getscreen()
    screen.reset()
    screen.bgcolor('black')
    screen.colormode(255)
    screen.screensize(WIDTH,HEIGHT)
    screen.setworldcoordinates(0,0,WIDTH,HEIGHT)
    turtle.hideturtle()
    turtle.pencolor(255,255,0)
    turtle.penup()
    turtle.delay(0)

def getRGB():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def doDrawingFast(nPoints, divisor, iters, points, probs):
    choices = [points[i] for i in npr.choice([ x for x in range(nPoints)], size=iters, p=probs) ]
    lastx = points[0][0]
    lasty = points[0][1]
    image = []
    for i in range(iters):
        curPoint = choices[i]
        newx = lastx + (curPoint[0] - lastx)//divisor
        newy = lasty + (curPoint[1] - lasty)//divisor
        lastx = newx
        lasty = newy
        image.append((newx,newy))

    for i in range(len(image)):
        turtle.penup()
        turtle.setpos(image[i][0], image[i][1])
        turtle.pendown()
        turtle.dot(size=1)


done = False

while not done:
    nPoints = input('How many points? (3 or 4):\t')
    while not nPoints in ['3','4']:
        print(f"That isn't a valid number of points, choose from {list(pointSets.keys())}")
        nPoints = input('How many points? (3 or 4):')

    divisor = input('How should the distance be divided? (2,3,4,6,8,12):\t')
    while not divisor in ['2','3','4','6','8','12']:
        print(f"That is not a valid divisor, choose from [2,3,4,6,8,12]")
        divisor = input('How should the distance be divided? (2,3,4,6,8,12):')
    
    doSetup()
    divisor = int(divisor)
    nPoints = int(nPoints)
    points = pointSets[nPoints]

    
    # Uniform probability over points
    probs = [1.0/nPoints for x in range(nPoints)]

    doDrawingFast(nPoints,divisor,5000,points,probs)
    
    response = input('Press y to start over, any other key to quit:\t')
    if response != 'y':
        done = True


