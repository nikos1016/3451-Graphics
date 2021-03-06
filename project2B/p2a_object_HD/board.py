from cylinder import *

# board
def board():
    stroke(0, 0, 0)
    smooth()
    strokeWeight(0.1)
    fill(255, 255, 255)
    pushMatrix()
    #translate (-37, 8, 0)
    scale(15, 15, 1)
    cylinder(64, 1)
    popMatrix()

    stroke(0, 0, 0)
    smooth()
    strokeWeight(0.1)
    fill(0, 0, 0)
    pushMatrix()
    #translate (-37, 8, 0)
    scale(13, 13, 1.01)
    cylinder(64, 0)
    popMatrix()

    stroke(0, 0, 0)
    smooth()
    strokeWeight(0.1)
    fill(5, 104, 199)
    pushMatrix()
    #translate (-37, 8, 0)
    scale(11, 11, 1.02)
    cylinder(64, 0)
    popMatrix()

    stroke(0, 0, 0)
    strokeWeight(0.1)
    fill(5, 104, 199)
    pushMatrix()
    #translate (-37, 8, 0)
    scale(9, 9, 1.02)
    cylinder(64, 0)
    popMatrix()

    stroke(0, 0, 0)
    smooth()
    strokeWeight(0.1)
    c = color(255, 51, 0)
    fill(c)
    pushMatrix()
    #translate (-37, 8, 0)
    scale(7, 7, 1.03)
    cylinder(64, 0)
    popMatrix()

    stroke(0, 0, 0)
    smooth()
    strokeWeight(0.1)
    c = color(255, 51, 0)
    fill(c)
    pushMatrix()
    #translate (-37, 8, 0)
    scale(5, 5, 1.03)
    cylinder(64, 0)
    popMatrix()

    stroke(0, 0, 0)
    smooth()
    strokeWeight(0.1)
    c = color(255, 204, 0)
    fill(c)
    pushMatrix()
    #translate (-37, 8, 0)
    scale(3, 3, 1.04)
    cylinder(64, 0)
    popMatrix()

    stroke(0, 0, 0)
    smooth()
    strokeWeight(0.2)
    c = color(255, 204, 0)
    fill(c)
    pushMatrix()
    #translate (-37, 8, 0)
    scale(1, 1, 1.04)
    cylinder(64, 0)
    popMatrix()

    stroke(0, 0, 0)
    smooth()
    strokeWeight(0.1)
    c = color(0, 0, 0)
    fill(c)
    pushMatrix()
    #translate (-37, 8, 0)
    scale(0.1, 0.1, 1.05)
    cylinder(64, 0)
    popMatrix()
