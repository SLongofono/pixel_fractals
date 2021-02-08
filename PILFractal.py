from PIL import Image
import random
import numpy.random as npr
import time

HEIGHT = 960
WIDTH  = 960
BUFFER = 60

# 0,0 is in the upper left corner
pointSets = {
    3:[(WIDTH//3, (HEIGHT*2)//3),((WIDTH*2)//3,(HEIGHT*2)//3),(WIDTH//2,HEIGHT//3)],
    4:[(WIDTH//4,HEIGHT//4),(WIDTH//4,(HEIGHT*3)//4),((WIDTH*3)//4,HEIGHT//4),((WIDTH*3)//4,(HEIGHT*3)//4)]
}

def getRGB():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def doDrawingFast(nPoints, divisor, iters, points, probs):
    theImg = Image.new('RGB', (WIDTH,HEIGHT), (0,0,0))
    pixels = theImg.load()
    choices = [points[i] for i in npr.choice([ x for x in range(nPoints)], size=iters, p=probs) ]
    lastx = points[0][0]
    lasty = points[0][1]
    for i in range(iters):
        curPoint = choices[i]
        newx = lastx + (curPoint[0] - lastx)//divisor
        newy = lasty + (curPoint[1] - lasty)//divisor
        lastx = newx
        lasty = newy
        pixels[newx,newy] = (255,255,0)
    filename = f'temp_{time.strftime("%m%d%y_%I%M%S")}.jpg'
    theImg.save(filename)
    return filename

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
    
    divisor = int(divisor)
    nPoints = int(nPoints)
    points = pointSets[nPoints]

    
    # Uniform probability over points
    probs = [1.0/nPoints for x in range(nPoints)]

    lastImg = doDrawingFast(nPoints,divisor,50000,points,probs)
    print(f'Image saved to {lastImg}')
    response = input('Press y to start over, any other key to quit:\t')
    if response != 'y':
        done = True

    

