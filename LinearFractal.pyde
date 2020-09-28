posV = []
negV = []

def setup():
    size(600, 600)
    background(255, 255, 255)
    posV.append(0) 
    posV.append(0) 
    negV.append(1)
    negV.append(0)
    noStroke()

def draw():
    fill(255, 255, 255)
    rect(0, 0, 600, 600)
    v = [] 
    v = realNumbers()
    linearFractal(v, posV, 0)
    textSize(15);
    fill(0, 0, 0)
    text("Madeline Ben-Yoseph: Warm-Up Project - Linear Fractal", 10, 20)
    fill(0, 42, 255)
    text("v: (" + str(((mouseX - 300.0) / 100.0)) + ", " + str(-((mouseY - 300.0) / 100.0)) + ")", 10, 40)
    
def realNumbers():
    points = []
    x = ((mouseX - 300.0) / 100.0)
    y = - ((mouseY - 300.0) / 100.0) 
    points.append(posV)
    points.append(negV)
    for i in range (0, 11):
        points.append(imagNumbers(x, y, points[i+1]))
    return points

def imagNumbers(x, y, points):
    newPoint = []
    xPoint = (x * points[0]) - (y * points[1])
    yPoint = (x * points[1]) + (y * points[0])
    newPoint.append(xPoint)
    newPoint.append(yPoint)
    return newPoint

def linearFractal(vVals, currV, iteration):
    if (iteration > 11):
        return;
    currPoint = []
    currPoint.append(vVals[iteration + 1])

    addCurrPoint = []
    addCurrPoint.append(currV[0] + currPoint[0][0])
    addCurrPoint.append(currV[1] + currPoint[0][1])
    
    subCurrPoint = []
    subCurrPoint.append(currV[0] - currPoint[0][0])
    subCurrPoint.append(currV[1] - currPoint[0][1])
    
    linearFractal(vVals, addCurrPoint, iteration + 1)
    linearFractal(vVals, subCurrPoint, iteration + 1)
    
    if (iteration < 2):
        fill(255, 0, 255)
    if (iteration >= 2 and iteration < 4):
        fill(0, 0, 153)
    if (iteration >= 4 and iteration < 6):
        fill(0, 128, 255)
    if (iteration >= 6 and iteration < 8):
        fill(51, 153, 255)
    if (iteration >= 8 and iteration < 10):
        fill(204, 153, 255)
    x = currV[0] * 100 + 300 
    y = -(currV[1]) * 100 + 300 
    ellipse(x, y, 10, 10)


 
 
         
    

    