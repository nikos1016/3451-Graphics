# CS3451 Project2B
# Hyungsuk Do
# hdo31
# 903012915

# an arrow: 2 spheres, a cylinder, 4 my own polygons(feathers)
# a board: 9 cylinders

from arrow import *
from cylinder import *
from board import *
from bow import *


bg = PImage()
time = 0.0
time1 = 0.0
time2 = 0.0
distance = 0.0
distance1 = 0.0
distance2 = 0.0
cameraTime = 0.0

camzoom = 20.0

def setup():
    global bg
    size(1600, 1600, OPENGL)
    perspective(60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    bg = loadImage("background.jpg")
    # image(bg, 0, 0);
    # # bg.resize(1600, 1600);
    # # image(bg,0,0)

def draw():
    global time, time1, time2, distance, distance1, distance2, bg, cameraTime
    time += 0.02
    time1 = time - 2
    time2 = time1 - 2
    cameraTime += 0.003
    distance = 50 * -time
    distance1 = 50 * -time1
    distance2 = 50 * -time2

    # if frameCount < 600 :
    #     camera(5, -100*sin(cameraTime)*1.5, 100*cos(cameraTime), 0, 0, 0, 0, 1, 0)
    # else :
    #     camera (0,-20,100,0,0,0,0,1,0)
    if frameCount > 330:
        if (100 - 10*time) > 0:
            camera(100 - 10*time,-5,20,0,0,0,0,1,0)
        else :
            camera(0, -10, 100, 0,0,0,0,1,0)
    else :
        camera(5, -100*sin(cameraTime)*1.5 -20, 100*cos(cameraTime), 0, 0, 0, 0, 1, 0)
    
    textSize(100)
    fill (255,0,0)

    background(bg)

    ambientLight(50, 50, 50)
    lightSpecular(255, 255, 255)
    spotLight(100, 100, 100, -50, 1, 1, 0, 1, 0, 0, 10)
    directionalLight(100, 100, 100, -0.3, 0.5, -1)

    noStroke()
    specular(180, 180, 180)
    shininess(15.0)
    
    translate(0,0,-20)
    
    # a board
    pushMatrix()
    #translate (-44, 1, 0)
    translate(-50.0, 0, 0)
    # rotateY(-time)
    # rotateX(-time)
    rotateY(radians(90))
    # rotateX(radians(30))
    scale(1.5,1.5,1)
    board()
    popMatrix()

     
    # arrows
    pushMatrix()
    # translate(-25, 16, 0)
    translate(52, 0, 0)
    translate (distance if distance > -92 else -92 , sin(time*10.3)/2 if distance > -92 else 0, 0)
    # rotateZ(radians(-35))
    scale(0.9,0.5,0.5)
    # rotateY(-time)
    rotateX(-time * 30 if distance > -92 else 0)
    arrow()
    popMatrix()
    
    if distance < -91.5 and distance > -110:
        textSize(10)
        fill (255,0,0)
        textAlign(CENTER)
        text("10!! wow",-20,-40,10)
    elif frameCount > 350:
        textSize(10)
        fill (255,0,0)
        textAlign(CENTER)
        text("Total: 24 Good Job",0,-40,10)

    if time >= 2 :
        pushMatrix()
        translate (distance1 if distance1 > -92 else -92 , 3*(-time1) if distance1 > -92 else -5.52, 2*(-time1) if distance1 > -92 else -3.68)
        translate(52, 0, 0)
        # rotateZ(radians(-35))
        scale(0.9,0.5,0.5)
        # rotateY(-time)
        rotateX(-time1 * 30 if distance1 > -92 else 0)
        arrow()
        popMatrix()
        if distance1 < -91.5 and distance1 > -130:
            textSize(10)
            # fill (255,0,0)
            textAlign(CENTER)
            text("8 Close!!",-20,-40,10)
    
    if time >= 4 :
        pushMatrix()
        translate (distance2 if distance2 > -94 else -94 , 2*(time2) if distance2 > -94 else 3.76, 6*(time2) if distance2 > -94 else 11.28)
        translate(52, 0, 0)
        # rotateZ(radians(-35))
        scale(0.9,0.5,0.5)
        # rotateY(-time)
        rotateX(-time2 * 30 if distance2 > -94 else 0)
        arrow()
        popMatrix()
        if distance2 < -91.5 and distance2 > -130:
            textSize(10)
            # fill (255,0,0)
            textAlign(CENTER)
            text("6 Focus it!!",-20,-40,10)
            
    

    #bow1
    pushMatrix()
    # mouseRotate()
    translate(45.0, 2.0, 0.0)
    # scale(0.5,0.5,0.5)
    # rotateX(-time)
    bowBody()
    popMatrix()
    
    print(frameCount)

    