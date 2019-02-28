#Hyungsuk Do
#hdo31@gatech.edu

# This is the starter code for the CS 3451 Ray Tracing project.
#
# The most important part of this code is the interpreter, which will
# help you parse the scene description (.cli) files.

import math

global angle, Bgr, Bgg, Bgb, lightTemp, shapeTemp, colorTemp, returnValue, Cdr,Cdg,Cdb,Car,Cag,Cab,Csr,Csg,Csb,P,Krefl,norma,D
angle = 0
Bgr = 0 #background Red
Bgg = 0 #background Green
Bgb = 0 #background Blue
# Cdr=Cdg=Cdb=Car=Cag=Cab=Csr=Csg=Csb=P=Krefl=D=0
lightTemp = [] # for light
shapeTemp = [] # for intersection
colorTemp = [] # for color
returnValue = [] # return value
TriangleTemp = []
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
    
    def scale1(self, s):
        return vertexTemp(s*self.x, s*self.y, s*self.z)



def setup():
    size(500, 500) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)

# read and interpret the appropriate scene description .cli file based on key press
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
    elif key == '0':
        interpreter("i10.cli")
def interpreter(fname):
    resetting()
    global angle, Bgr, Bgg, Bgb, Cdr,Cdg,Cdb,Car,Cag,Cab,Csr,Csg,Csb,P,Krefl
    
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse each line in the file in turn
    for line in lines:
        words = line.split()  # split the line into individual tokens
        if len(words) == 0:   # skip empty lines
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
            Car = float(words[4])
            Cag = float(words[5])
            Cab = float(words[6])
            Csr = float(words[7])
            Csg = float(words[8])
            Csb = float(words[9])
            P = float(words[10])
            Krefl = float(words[11])
            
        elif words[0] == 'begin':
            A=B=C=None
        elif words[0] == 'vertex':
            if A == None:
                A = vertexTemp(float(words[1]), float(words[2]), float(words[3]))
            elif B == None:
                B = vertexTemp(float(words[1]), float(words[2]), float(words[3]))
            else:
                C = vertexTemp(float(words[1]), float(words[2]), float(words[3]))
                shapeTemp.append(Triangle(A,B,C))
                # print(shapeTemp)
                A=B=C=None
        elif words[0] == 'end':
            A=B=C=None
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])  # write the image to a file
            pass

# render the ray tracing scene
def render_scene():
    global angle, Bgr, Bgg, Bgb, Cdr,Cdg,Cdb,Car,Cag,Cab,Csr,Csg,Csb,P,Krefl
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
            # ind = 0
            # p_intersection = None
            # closest_point = None
            # while (ind < len(shapeTemp)):
            #     hit = shapeTemp[ind].intersect(ray)
            #     #find the closest point with the ray
            #     if hit is not None and ((p_intersection is None) or (hit.distance(ray.rayOrigin) < p_intersection.distance(ray.rayOrigin))):
            #         p_intersection = hit
            #         closest_point = shapeTemp[ind]
                    # ind = ind + 1
            cPoint, pIntersection = surface(ray) # closest point, intersection point
            # cPoint = closest_point
            # pIntersection = p_intersection
            
            if(cPoint == None):
                pix_color = color(Bgr, Bgg, Bgb)
                set (i, j, pix_color)  
            else:
                r=g=b=0
                colorTemp = calcColor(ray, cPoint, pIntersection,r,g,b,0)
                pix_color = color(colorTemp[0], colorTemp[1], colorTemp[2]) # you should calculate the correct pixel color here
                set (i, j, pix_color) # fill the pixel with the calculated color
    
def calcColor(ray, surface, pIntersection,r,g,b,depth):
    global angle, Bgr, Bgg, Bgb, Cdr,Cdg,Cdb,Car,Cag,Cab,Csr,Csg,Csb,P,Krefl
    N = surface.getNormal(pIntersection) # normal suface
    ind = 0
    # e = ray[::-1]
    if surface.Krefl > 0 and depth < 12:
        unitRayDirect = ray.directionVec.unit()
        reflDirec = RayTrac(pIntersection, N.scale1(2 * N.dotP(unitRayDirect)).subtract(unitRayDirect).scale1(-1))
        reflClosest = None
        reflPoint = None
        for s in shapeTemp:
            if (s != surface):
                tempP = s.intersect(reflDirec)
                if tempP != None and (reflPoint == None or tempP.distance(reflDirec.rayOrigin) < reflPoint.distance(reflDirec.rayOrigin)):
                    reflClosest = s
                    reflPoint =tempP
        if reflClosest != None:
            reflColors = calcColor(reflDirec, reflClosest, reflPoint,r,g,b,depth+1)
            r += surface.Krefl * reflColors[0]
            g += surface.Krefl * reflColors[1]
            b += surface.Krefl * reflColors[2]
        else:
            r += surface.Krefl * Bgr
            g += surface.Krefl * Bgg
            b += surface.Krefl * Bgb
    
    r += surface.Car
    g += surface.Cag
    b += surface.Cab
    
    # while ind < len(lightTemp):
    #     light_Vector = lightTemp[ind].vertexTemp.subtract(pIntersection)
    #     temp = light_Vector.dotP(N) / light_Vector.getLength()
    #     light_color = max(0, temp)
    #     r += surface.Cdr * lightTemp[ind].r * light_color
    #     g += surface.Cdg * lightTemp[ind].g * light_color
    #     b += surface.Cdb * lightTemp[ind].b * light_color
    #     ind = ind + 1
    # returnValue = [r, g, b]
    # return returnValue
    
    for l in lightTemp:
        lray = RayTrac(pIntersection, l.vertexTemp.subtract(pIntersection))
        lPoint = None
        for s in shapeTemp:
            tempP = s.intersect(lray)
            if tempP != None and (lPoint == None or tempP.distance(lray.rayOrigin) < pIntersection.distance(ray.rayOrigin)):
                lPoint = tempP
        if lPoint == None or lPoint.distance(lray.rayOrigin) > l.vertexTemp.distance(lray.rayOrigin):
            cosTheta = max(0,(lray.directionVec.dotP(N)) / (lray.directionVec.getLength()))
            r += cosTheta * surface.Cdr * l.re
            g += cosTheta * surface.Cdg * l.gr
            b += cosTheta * surface.Cdb * l.bl
            
            L = lray.directionVec.unit()
            R = N.scale1(2 * N.dotP(L)).subtract(L).unit()
            E = ray.directionVec.unit()
            if (R.dotP(E) < 0):
                phong = math.pow(R.dotP(E), surface.P)
                r += phong * surface.Csr * l.re
                g += phong * surface.Csg * l.gr
                b += phong * surface.Csb * l.bl
    returnValue = [r, g, b]
    return returnValue
                

# should remain empty for this assignment
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

class Triangle(object):
    global Cdg, Cdb, Cdr, Csr, Csg, Csb,P,Krefl, Cag, Cab, Car,norma,D
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
        self.Cdg = Cdg
        self.Cdb = Cdb
        self.Cdr = Cdr
        self.Car = Car
        self.Cag = Cag
        self.Cab = Cab
        self.Csr = Csr
        self.Csg = Csg
        self.Csb = Csb
        self.P = P
        self.Krefl = Krefl
        self.norma = B.subtract(A).crossP(C.subtract(A)).unit()
        self.D = self.norma.dotP(A)
        
    def intersect(self, ray):
        # D = self.norma.dotP(self.a)
        deno = self.norma.dotP(ray.directionVec)
        if deno == 0:
            return None
        t = (self.D - self.norma.dotP(ray.rayOrigin)) / deno
        if t <= 0.000001:
            return None
        point1 = ray.getNewPoint(t)
        if (self.B.subtract(self.A).crossP(point1.subtract(self.A)).dotP(self.norma) >= -.0000000000001):
            if (self.C.subtract(self.B).crossP(point1.subtract(self.B)).dotP(self.norma) >= -.0000000000001):
                if (self.A.subtract(self.C).crossP(point1.subtract(self.C)).dotP(self.norma) >= -.0000000000001):
                    return point1
        return None
    
    def getNormal(self, v):
        return self.norma.scale1(-1)
    
class Create_sphere(object):
    global Cdg, Cdb, Cdr, Csr, Csg, Csb, P, Krefl, Cag, Car, Cab
    def __init__(self, radius, x, y, z):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z
        self.Cdg = Cdg
        self.Cdb = Cdb
        self.Cdr = Cdr
        self.Car = Car
        self.Cag = Cag
        self.Cab = Cab
        self.Csr = Csr
        self.Csg = Csg
        self.Csb = Csb
        self.P = P
        self.Krefl = Krefl 
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
            root1 = (-b - math.sqrt(discriminant)) / (2*a)  #discriminant >= 0
            root2 = (-b + math.sqrt(discriminant)) / (2*a)
            root = min(root1, root2)
            if (root > -0.000001): #only positive
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
    
    def __init__(self, x, y, z, re, gr, bl):
        self.re = re
        self.gr = gr
        self.bl = bl
        self.vertexTemp = vertexTemp(x, y, z)

def resetting():
    
    global lightTemp, shapeTemp, colorTemp, returnValue, Cdr, Cdg, Cdb, angle, Bgr, Bgg, Bgb,Car,Cag,Cab,Csr,Csg,Csb,P,Krefl,norma,D
    lightTemp = [] 
    shapeTemp = [] 
    colorTemp = []
    returnValue = []
    Cdr = 0
    Cdg = 0
    Cdb = 0
    Car = 0
    Cab = 0
    Cag = 0
    Csr = 0
    Csg = 0
    Csb = 0
    P = 0
    # D = 0
    Krefl = 0
    angle = 0
    Bgr = 0
    Bgg = 0
    Bgb = 0
    background(0, 0, 0)