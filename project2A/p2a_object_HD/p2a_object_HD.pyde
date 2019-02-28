# CS3451 Project2A
# Hyungsuk Do
# hdo31
# 903012915

# an arrow: 2 spheres, a cylinder, 4 my own polygons(feathers)
# a board: 9 cylinders

time = 0

def setup():
    size(1600, 1600, OPENGL)
    perspective(60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view

def draw():
    global time
    time += 0.01

    camera(0, 0, 100, 0, 0, 0, 0, 1, 0)
    background(51, 102, 51)

    ambientLight(50, 50, 50)
    #lightSpecular(255, 255, 255)
    directionalLight(100, 100, 100, -0.3, 0.5, -1)

    noStroke()
    specular(180, 180, 180)
    shininess(15.0)

    # a board
    pushMatrix()
    rotateY(radians(65))
    rotateX(radians(30))
    #translate (-44, 1, 0)
    translate(-35, -7, 0)
    rotateY(-time)
    rotateX(-time)
    board()
    popMatrix()

    # 3 arrows
    pushMatrix()
    translate(35, -40, 0)
    rotateY(-time)
    # rotateX(-time)
    arrow()
    popMatrix()

    pushMatrix()
    translate(35, -20, 0)
    # rotateY(-time)
    rotateX(-time)
    arrow()
    popMatrix()

    pushMatrix()
    translate(35, 0, 0)
    # rotateY(-time)
    # rotateX(-time)
    rotateZ(-time)
    arrow()
    popMatrix()



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
    # arrow
    #stroke(255, 0, 0)
    noStroke()
    smooth()
    # strokeJoin(ROUND)
    fill(255, 0, 0)
    pushMatrix()
    translate(-10, 0, 0)
    scale(8, 1, 1)
    sphere(0.15)
    popMatrix()

    # strokeWeight(0.1)
    smooth()
    fill(204, 102, 0)
    pushMatrix()
    # rotateY(-time)
    #translate (0, -50, 0)
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


# cylinder for a bow body
def cylinder1(sides=64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        z = cos(theta)
        y = sin(theta)
        vertex(-1, y, z)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        z = cos(theta)
        y = sin(theta)
        vertex(1, y, z)
    endShape(CLOSE)
    # sides
    z1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        z2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal(0, y1, z1)
        vertex(1, y1, z1)
        vertex(-1, y1, z1)
        normal(0, y2, z2)
        vertex(-1, y2, z2)
        vertex(1, y2, z2)
        endShape(CLOSE)
        z1 = z2
        y1 = y2


# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides, sideColor):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex(x, y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex(x, y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        if sideColor == 1:
            fill(153, 77, 0)
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal(x1, y1, 0)
        vertex(x1, y1, 1)
        vertex(x1, y1, -1)
        normal(x2, y2, 0)
        vertex(x2, y2, -1)
        vertex(x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2