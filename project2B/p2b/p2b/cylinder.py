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