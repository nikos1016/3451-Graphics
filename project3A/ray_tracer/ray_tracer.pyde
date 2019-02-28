#Hyungsuk Do
#hdo31@gatech.edu

# This is the starter code for the CS 3451 Ray Tracing project.
#
# The most important part of this code is the interpreter, which will
# help you parse the scene descrip_intersectionion (.cli) files.


import math

global angle, Bgr, Bgg, Bgb, lightTemp, shapeTemp, colorTemp, returnValue, Cdr,Cdg,Cdb
angle = 0
Bgr = 0 #background Red
Bgg = 0 #background Green
Bgb = 0 #background Blue
lightTemp = [] # for light
shapeTemp = [] # for intersection
colorTemp = [] # for color
returnValue = [] # return value

class vertexTemp(object):
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def distance(self, dista):
        temp1 = dista.x-self.x
        temp2 = dista.y-self.y
        temp3 = dista.z-self.z
        return math.sqrt((temp1)*(temp1) + (temp2)*(temp2) + (temp3)*(temp3))
    
    def dotP(self, dotp):
        temp1 = self.x*dotp.x
        temp2 = self.y*dotp.y
        temp3 = self.z*dotp.z
        return (temp1 + temp2 + temp3)
    
    def getLength(self):
        temp = math.sqrt(self.dotP(self))
        return temp
    
    def crossP(self, cros):
        temp1 = self.y*cros.z - self.z*cros.y
        temp2 = self.z*cros.x - self.x*cros.z
        temp3 = self.x*cros.y - self.y*cros.x
        return vertexTemp(temp1, temp2, temp3)
    
    def unit(self):
        unit_length = math.sqrt(self.dotP(self))
        temp1 = self.x/unit_length
        temp2 = self.y/unit_length
        temp3 = self.z/unit_length
        return vertexTemp(temp1, temp2, temp3)
    
    def subtract(self, subs):
        temp1 = self.x-subs.x
        temp2 = self.y-subs.y
        temp3 = self.z-subs.z
        return vertexTemp(temp1, temp2, temp3)

def setup():
    size(500, 500) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)

# read and interpret the appropriate scene descrip_intersectionion .cli file based on key press
def keyPressed():
    if key == '1':
        interpreter("i1.cli")
    elif key == '2':
        interpreter("i2.cli")
    elif key == '3':
        interpreter("i3.cli")
    elif key == '4':
        interpreter("i4.cli")
    elif key == '5':
        interpreter("i5.cli")
    elif key == '6':
        interpreter("i6.cli")
    elif key == '7':
        interpreter("i7.cli")
    elif key == '8':
        interpreter("i8.cli")
    elif key == '9':
        interpreter("i9.cli")

def interpreter(fname):
    resetting()
    global angle, Bgr, Bgg, Bgb, Cdr,Cdg,Cdb
    
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse each line in the file in turn
    for line in lines:
        words = line.split()  # split the line into individual tokens
        if len(words) == 0:   # skip emp_intersectiony lines
            continue
        if words[0] == 'sphere':
            radius = float(words[1])
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])
            # call your sphere creation routine here
            # for example: create_sphere(radius,x,y,z)
            shapeTemp.append(Create_sphere(radius, x, y, z))
        elif words[0] == 'fov':
            angle = float(words[1])
        elif words[0] == 'background':
            Bgr = float(words[1])
            Bgg = float(words[2])
            Bgb = float(words[3])
        elif words[0] == 'light':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            r = float(words[4])
            g = float(words[5])
            b = float(words[6])
            lightTemp.append(Light(x, y, z, r, g, b))
        elif words[0] == 'surface':
            Cdr = float(words[1])
            Cdg = float(words[2])
            Cdb = float(words[3])
        elif words[0] == 'begin':
            pass
        elif words[0] == 'vertexTemp':
            pass
        elif words[0] == 'end':
            pass
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])  # write the image to a file
            pass

# render the ray tracing scene
def render_scene():
    
    global angle, Bgr, Bgg, Bgb
    k = math.tan(radians(angle/2.0))
    
    for j in range(height):
        for i in range(width):
            # create an eye ray for pixel (i,j) and cast it into the scene
            #create a Ray from Eye to the pixel's position in 3D
            #convert 3D to 2D
            j_1 = height - j
            temp1 = (i-(width/2))*(2*k/(width)) #convert x
            temp2 = (j_1-(height/2))*(2*k/(height)) # convert y
            temp = vertexTemp(temp1, temp2, -1)
            temp3 = vertexTemp(0, 0, 0)
            ray = RayTrac(temp3, temp)
            cPoint, pIntersection = surface(ray) # closest point, intersection point
            
            if(cPoint is None):
                pix_color = color(Bgr, Bgg, Bgb)
                set (i, j, pix_color)  
            else:
                colorTemp = calcColor(ray, cPoint, pIntersection)
                pix_color = color(colorTemp[0], colorTemp[1], colorTemp[2]) # you should calculate the correct pixel color here
                set (i, j, pix_color) # fill the pixel with the calculated color

# should remain emp_intersectiony for this assignment
def draw():
    pass

def surface(ray):
    ind = 0
    p_intersection = None
    closest_point = None
    while (ind < len(shapeTemp)):
        hit = shapeTemp[ind].intersect(ray)
        #find the closest point with the ray
        if hit is not None and ((p_intersection is None)
                        or (hit.distance(ray.rayOrigin) < p_intersection.distance(ray.rayOrigin))):
            p_intersection = hit
            closest_point = shapeTemp[ind]
        ind = ind + 1
    return closest_point, p_intersection
     
class Create_sphere(object):
    
    def __init__(self, radius, x, y, z):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z
        self.Cdg = Cdg
        self.Cdb = Cdb
        self.Cdr = Cdr
        self.vertexTemp = vertexTemp(x, y, z)
    
    def intersect(self, rayTemp):  #intersection of Eye ray and sphere
        # a = dx^2, dy^2, dz^2
        a = rayTemp.directionVec.dotP(rayTemp.directionVec)
        
        # b = 2((X0-Cx)dx), (Y0-Cy)dy, (Z0-Cz)dz)
        temp = (rayTemp.rayOrigin.subtract(self.vertexTemp)).dotP(rayTemp.directionVec)
        b = 2*temp
        
        #c=(x0-cx)^2 , (y0-cy)^2 , (z0-cz)^2 - r^2
        temp1 = (rayTemp.rayOrigin.subtract(self.vertexTemp)).dotP(rayTemp.rayOrigin.subtract(self.vertexTemp))
        temp2 = self.radius*self.radius
        c = temp1 - temp2
        
        discriminant = (b*b) - (4*a*c)
        
        if (discriminant < 0): # There are no intersections
            return None
        else:
            root = (-b - math.sqrt(discriminant)) / (2*a)  #discriminant >= 0
            if (root > 0): #only positive
                return rayTemp.getNewPoint(root)
            else:
                return None
    
    def getNormal(self, nor):
        #nor is normal
        temp = nor.subtract(self.vertexTemp).unit()  #(intersect - sphere_center).normalize
        return temp
    
class RayTrac(object):
    
    def __init__(self, rayOrigin, directionVec):
        self.rayOrigin = rayOrigin
        self.directionVec = directionVec
        
    def getNewPoint(self, t): #t is parameter
        x = self.rayOrigin.x + t*self.directionVec.x
        y = self.rayOrigin.y + t*self.directionVec.y
        z = self.rayOrigin.z + t*self.directionVec.z
        return vertexTemp(x, y, z)
        
class Light(object):
    
    def __init__(self, x, y, z, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.vertexTemp = vertexTemp(x, y, z)

def calcColor(ray, surface, pIntersection):
    
    N = surface.getNormal(pIntersection) # normal suface
    r = 0
    g = 0
    b = 0
    ind = 0
    
    while ind < len(lightTemp):
        light_Vector = lightTemp[ind].vertexTemp.subtract(pIntersection)
        temp = light_Vector.dotP(N) / light_Vector.getLength()
        light_color = max(0, temp)
        r += surface.Cdr * lightTemp[ind].r * light_color
        g += surface.Cdg * lightTemp[ind].g * light_color
        b += surface.Cdb * lightTemp[ind].b * light_color
        ind = ind + 1
    returnValue = [r, g, b]
    return returnValue

def resetting():
    
    global lightTemp, shapeTemp, colorTemp, returnValue, Cdr, Cdg, Cdb, angle, Bgr, Bgg, Bgb
    lightTemp = [] 
    shapeTemp = [] 
    colorTemp = []
    returnValue = []
    Cdr = 0
    Cdg = 0
    Cdb = 0
    angle = 0
    Bgr = 0
    Bgg = 0
    Bgb = 0
    background(0, 0, 0)