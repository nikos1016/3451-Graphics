from cylinder import *

# my own polygon function for a feather of the arrow
def feather():
    fill(255, 0, 0)
    pushMatrix()
    beginShape()
    vertex(0, 0, 0)
    vertex(10, 0, -1)
    vertex(10, 0, 1)
    endShape()
    popMatrix()

    pushMatrix()
    beginShape()
    vertex(0, 0, 0)
    vertex(10, 0, 1)
    vertex(10, -3, 0)
    endShape()
    popMatrix()

    pushMatrix()
    beginShape()
    vertex(0, 0, 0)
    vertex(10, 0, -1)
    vertex(10, -3, 0)
    endShape()
    popMatrix()

    pushMatrix()
    beginShape()
    vertex(10, 0, -1)
    vertex(10, 0, -1)
    vertex(10, -3, 0)
    endShape()
    popMatrix()

# an arrow
def arrow():
    noStroke()
    smooth()
    fill(255, 0, 0)
    pushMatrix()
    translate(-10, 0, 0)
    scale(8, 1, 1)
    sphere(0.15)
    popMatrix()

    smooth()
    fill(204, 102, 0)
    pushMatrix()
    scale(10, 0.15, 0.15)
    cylinder1()
    popMatrix()

    smooth()
    fill(255, 0, 0)
    pushMatrix()
    translate(10, 0, 0)
    scale(3, 1, 1)
    sphere(0.15)
    popMatrix()

    # first feather
    smooth()
    fill(255, 0, 0)
    pushMatrix()
    translate(4, 0, 0)
    scale(0.5, 0.25, 0.15)
    feather()
    popMatrix()

    # second feather
    smooth()
    fill(255, 0, 0)
    pushMatrix()
    rotateX(radians(90))
    translate(4, 0, 0)
    scale(0.5, 0.25, 0.15)
    feather()
    popMatrix()

    # third feather
    smooth()
    fill(255, 0, 0)
    pushMatrix()
    rotateX(radians(180))
    translate(4, 0, 0)
    scale(0.5, 0.25, 0.15)
    feather()
    popMatrix()

    # fourth feather
    smooth()
    fill(255, 0, 0)
    pushMatrix()
    rotateX(radians(270))
    translate(4, 0, 0)
    scale(0.5, 0.25, 0.15)
    feather()
    popMatrix()