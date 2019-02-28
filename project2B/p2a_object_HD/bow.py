from cylinder import *
# from arrow import *
stringTime = 0

def bowBody():
    global stringTime
    stringTime += 2*0.01
    j=0
    k=0
    for i in range(60):
        fill(139,69,19)
        pushMatrix()
        noStroke()
        translate(0+j,0,0+k)
        translate(0,-1,2)
        sphere(1)
        popMatrix()
        
        pushMatrix()
        noStroke()
        translate(0+j,0,0-k)
        translate(0,-1,-2)
        sphere(1)
        popMatrix()
        j+= 0.1
        k+= 0.2
    i=0
    k=0
    for i in range(40):
        pushMatrix()
        noStroke()
        translate(0,0,0+k)
        translate(0,-1,-2)
        sphere(1)
        popMatrix()
        k+= 0.1
    
    i=0
    k=0
    for i in range(15):
        pushMatrix()
        noStroke()
        translate(0+j,0,-12+k)
        translate(0,-1,-2)
        sphere(1)
        popMatrix()
        
        pushMatrix()
        noStroke()
        translate(0+j,0,12-k)
        translate(0,-1,2)
        sphere(1)
        popMatrix()
        j+= 0.1
    
    #bowbody
    pushMatrix()
    # fill(210,105,30)
    translate(9.5,1,0)
    scale(20,3,4)    
    box(1)
    popMatrix()
    
    #bowHead
    pushMatrix()
    # fill(255,51,51)
    translate(-4.5,2.5,0)
    scale(2,3,2.03)
    bowHead()
    popMatrix()
    
    i=0
    k=0
    #bow hand
    for i in range(40):
        fill(139,69,19)
        pushMatrix()
        noStroke()
        translate(0+j,0+k,0)
        translate(7,2,0)
        sphere(1)
        popMatrix()
        j+= 0.1
        k+= 0.1
        
    # for i in range(20):
    #     pushMatrix()
    #     noStroke()
    #     #rotateX(-time)
    #     translate(0+j,0,0)
    #     translate(7,6,0)
    #     sphere(1)
    #     popMatrix()
    #     j+= 0.1
    
    # for i in range(40):
    #     pushMatrix()
    #     noStroke()
    #     #rotateX(-time)
    #     translate(0+j,0+k,0)
    #     translate(-11,-18,0)
    #     sphere(1)
    #     popMatrix()
    #     k+= 0.1
    
    pushMatrix()
    fill (139,69,19)
    translate(13,-1,0)
    scale(0.5,0.5,0.5)
    rotateZ(radians(-90))
    cylinder1()
    popMatrix()
    
    pushMatrix()
    translate(7.5,-1,-6.5)
    # rotateY(radians(90))
    # rotateY(radians(45))
    # translate(width/2, height/2)
    # translate(7.5*sin(-stringTime), 0, -(7.5 - 7.5*cos(-stringTime)))
    # rotateY(-stringTime)
    if stringTime < 0.6:
        translate(7.5*sin(-stringTime), 0, -(7.5 - 7.5*cos(-stringTime)))
        rotateY(-stringTime)
    translate(7.5*sin(0.43), 0, -(7.5 - 7.5*cos(0.43)))
    rotateY(0.43)
    rotateX(radians(90))
    string()
    popMatrix()
    
    pushMatrix()
    translate(7.5,-1,6.5)
    # rotateY(radians(90))
    # rotateY(radians(45))
    # translate(width/2, height/2)
    if stringTime < 0.6:
        translate(-7.5*sin(stringTime), 0.0, (7.5 - 7.5*cos(stringTime)))
        rotateY(stringTime)
    # else :
    #     translate(-7.5*sin(-0.43), 0, (7.5 - 7.5*cos(-0.43)))
    #     rotateY(-0.43)
    translate(-7.5*sin(-0.43), 0.0, (7.5 - 7.5*cos(-0.43)))
    rotateY(-0.43)
    rotateX(radians(90))
    string()
    popMatrix()
    
def string():
    
    #string
    pushMatrix()
    fill (245,255,250)
    # translate(30, -30, 0)
    # rotateZ(radians(-45))
    # translate(0.5,0,10)
    # translate()
    scale(0.1, 8, 0.1)
    # rotateX(radians(-90))
    cylinder(64, 0)
    popMatrix()

# my own polygon for the bow's head
def bowHead():
    pushMatrix()
    beginShape()
    vertex(0,0,0)
    vertex(2,0,-1)
    vertex(2,0,1)
    endShape()
    popMatrix()
    
    pushMatrix()
    beginShape()
    vertex(0,-1,0)
    vertex(2,-1,-1)
    vertex(2,-1,1)
    endShape()
    popMatrix()
    
    pushMatrix()
    beginShape()
    vertex(0,-1,0)
    vertex(0,0,0)
    vertex(2,0,1)
    vertex(2,-1,1)
    endShape()
    popMatrix()
    
    pushMatrix()
    beginShape()
    vertex(0,-1,0)
    vertex(0,0,0)
    vertex(2,0,-1)
    vertex(2,-1,-1)
    endShape()
    popMatrix()
    
    pushMatrix()
    beginShape()
    vertex(2,-1,1)
    vertex(2,-1,-1)
    vertex(2,0,-1)
    vertex(2,0,1)
    endShape()
    popMatrix()