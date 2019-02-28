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
from string import *

# bg = PImage()
time = 0.0
distance = 0.0
cameraTime = 0.0

camzoom = 20.0

def setup():
    global bg
    size(1600, 1600, OPENGL)
    perspective(60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    # bg = loadImage("background.jpg")
    # image(bg, 0, 0);
    # # bg.resize(1600, 1600);
    # # image(bg,0,0)

def draw():
    global time, distance, bg, cameraTime
    time += 0.01
    cameraTime += 0.001
    distance = 50 * -time
    distance1 = -distance/1.635
    # stringTime += 2*0.01

    # camera(5, -100*sin(cameraTime), 100*cos(cameraTime), 0, 0, 0, 0, 1, 0)
    
    camera(100,-5,-20,0,0,0,0,1,0)
    # camera(0, -50, 100, 0, 0, 0, 0, 1, 0)
    # camera(0, -5*time, 100-5*time, 0, 0, 0, 0,  1, 0)
    # background(255,15,10)
    background(76,153,0)
    # background(bg)

    ambientLight(50, 50, 50)
    lightSpecular(255, 255, 255)
    directionalLight(100, 100, 100, -0.3, 0.5, -1)

    noStroke()
    specular(180, 180, 180)
    shininess(15.0)
    
    translate(0,0,-camzoom)
    
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

    # # arrows
    # pushMatrix()
    # # translate(-25, 16, 0)
    # translate(25, -30, 55)
    # # translate (distance if distance > -44.5 else -44.5 , distance1 if distance > -44.5 else 27.217, 0)
    # rotateZ(radians(-35))
    # scale(0.4,0.5,0.5)
    # # rotateY(-time)
    # rotateX(-time * 30 if distance > -44.5 else 0)
    # arrow()
    # popMatrix()

    # pushMatrix()
    # # translate(35, -20, 0)
    # # rotateY(-time)
    # scale(0.7,1,1)
    # rotateX(-time * -30)
    # arrow()
    # popMatrix()

    # pushMatrix()
    # translate(35, 0, 0)
    # # rotateY(-time)
    # # rotateX(-time)
    # scale(0.7,1,1)
    # rotateZ(-time)
    # arrow()
    # popMatrix()
 
    #bow1
    pushMatrix()
    # mouseRotate()
    translate(45.0, 2.0, 0.0)
    # scale(0.5,0.5,0.5)
    # rotateX(-time)
    bowBody()
    popMatrix()
    
    # pushMatrix()
    # string()
    # popMatrix()
    