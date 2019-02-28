#Hyungsuk Do
# Sample code for starting the mesh processing project
import math
from random import randint
rotate_flag = True    # automatic rotation of model?
time = 0   # keep track of passing time, for automatic rotation

vertTemp = []
cornerTemp = []
oppos = []
s = 0
vertexnormals = False
randcolors = False

# initalize stuff
def setup():
    size (600, 600, OPENGL)
    noStroke()

# draw the current mesh
def draw():
    global time
    
    background(0)    # clear screen to black

    perspective (PI*0.333, 1.0, 0.01, 1000.0)
    camera (0, 0, 5, 0, 0, 0, 0, 1, 0)    # place the camera in the scene
    scale (1, -1, 1)    # change to right-handed coordinate system
    
    # create an ambient light source
    ambientLight (102, 102, 102)
  
    # create two directional light sources
    lightSpecular (204, 204, 204)
    directionalLight (102, 102, 102, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    
    pushMatrix();

    fill (200, 200, 200)            # set polygon color
    ambient (200, 200, 200)
    specular (0, 0, 0)            # no specular highlights
    shininess (1.0)
  
    rotate (time, 1.0, 0.0, 0.0)
    randomSeed(s)
    # THIS IS WHERE YOU SHOULD DRAW THE MESH
  
    # beginShape()1
    # normal (0.0, 0.0, 1.0)
    # vertex (-1.0, -1.0, 0.0)
    # vertex ( 1.0, -1.0, 0.0)
    # vertex ( 1.0,  1.0, 0.0)
    # vertex (-1.0,  1.0, 0.0)
    # endShape(CLOSE)

    for i in range(0, len(cornerTemp)/3):
        v1 = vertTemp[cornerTemp[3*i]]
        v2 = vertTemp[cornerTemp[3*i + 1]]
        v3 = vertTemp[cornerTemp[3*i + 2]]
        beginShape()
        if randcolors:
            fill(random(0,255), random(0,255), random(0,255))
        if vertexnormals:
            nor = getNormal(v1)
            normal(nor.x, nor.y, nor.z)
        vertex(v1.x,v1.y,v1.z)
        if vertexnormals:
            nor = getNormal(v2)
            normal(nor.x,nor.y,nor.z)
        vertex(v2.x,v2.y,v2.z)
        if vertexnormals:
            nor = getNormal(v3)
            normal(nor.x,nor.y,nor.z)
        vertex(v3.x,v3.y,v3.z)
        endShape(CLOSE)
    popMatrix()
    
    # maybe step forward in time (for object rotation)
    if rotate_flag:
        time += 0.02

# process key presses
def keyPressed():
    global rotate_flag, vertexnormals, randcolors, s
    if key == ' ':
        rotate_flag = not rotate_flag
    elif key == '1':
        read_mesh ('tetra.ply')
    elif key == '2':
        read_mesh ('octa.ply')
    elif key == '3':
        read_mesh ('icos.ply')
    elif key == '4':
        read_mesh ('star.ply')
    elif key == '5':
        read_mesh ('torus.ply')
    elif key == 'n':
        if vertexnormals is True:
            vertexnormals = False
        else:
            vertexnormals = True
          # toggle per-vertex shading
    elif key == 'r':
        randcolors = True
        s = randint(0,1000)  # randomly color faces
        print(s)
    elif key == 'w':
        randcolors = False  # color faces white
    elif key == 'd':
        dualD()  # calculate the dual mesh
    elif key == 'q':
        exit()

# read in a mesh file (THIS NEEDS TO BE MODIFIED !!!)
def read_mesh(filename):
    global vertTemp, cornerTemp
    
    vertTemp = []
    cornerTemp = []
    
    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()
        
    # determine number of vertices (on first line)
    words = lines[0].split()
    num_vertices = int(words[1])
    print "number of vertices =", num_vertices

    # determine number of faces (on first second)
    words = lines[1].split()
    num_faces = int(words[1])
    print "number of faces =", num_faces

    # read in the vertices
    for i in range(num_vertices):
        words = lines[i+2].split()
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        print "vertex = ", x, y, z
        vertTemp.append(vertexTemp(x,y,z))
    
    # read in the faces
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        if nverts != 3:
            print "error: this face is not a triangle"
            exit()
        index1 = int(words[1])
        index2 = int(words[2])
        index3 = int(words[3])
        print "face =", index1, index2, index3
        cornerTemp.append(index1)
        cornerTemp.append(index2)
        cornerTemp.append(index3)
    generateAdj()


class vertexTemp(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.adj = []
        self.faces = []
    
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
    
    def equalTo(self, v):
        return ((v.x > (self.x -.001)) and (v.x < (self.x + .001)) and (v.y > (self.y - .001)) and (v.y < (self.y + .001)) and (v.z > (self.z - .001)) and (v.z < (self.z + .001)))
    
    def divide(self, d):
        return vertexTemp(self.x/d, self.y/d, self.z/d)
    
    def plus(self, p):
        return vertexTemp(self.x+p.x, self.y+p.y, self.z+p.z)
    
    def addFace(self,f):
        global faces
        self.faces.append(f)
        
    def addAdj(self,v):
        global adj
        for i in range(0, len(self.adj)):
            if self.adj[i] is v:
                return
        self.adj.append(v)


def getNormal(v):
    global vertTemp
    result = vertexTemp(0.0,0.0,0.0)
    for i in v.faces:
        v1 = vertTemp[cornerTemp[i*3]]
        v2 = vertTemp[cornerTemp[i*3 + 1]]
        v3 = vertTemp[cornerTemp[i*3 + 2]]
        nor = v2.subtract(v1).unit().crossP(v3.subtract(v1).unit())
        result = result.plus(nor)
    return result.divide(len(v.faces)).unit()

def generateAdj():
    global oppos, vertTemp, cornerTemp
    for i in range(0, len(cornerTemp), 3):
        vertTemp[cornerTemp[i]].addFace(i/3)
        vertTemp[cornerTemp[i+1]].addFace(i/3)
        vertTemp[cornerTemp[i+2]].addFace(i/3)
        vertTemp[cornerTemp[i]].addAdj(i+1)
        vertTemp[cornerTemp[i]].addAdj(i+2)
        vertTemp[cornerTemp[i+1]].addAdj(i)
        vertTemp[cornerTemp[i+1]].addAdj(i+2)
        vertTemp[cornerTemp[i+2]].addAdj(i)
        vertTemp[cornerTemp[i+2]].addAdj(i+1)
    oppos = []
    for i in range(0, len(cornerTemp)):
        oppos.append(0)
    for i in range(0, len(cornerTemp)):
        inn = 0
        ipp = 0
        if i % 3 is 0:
            inn = i + 1
            ipp = i + 2
        elif i % 3 is 1:
            inn = i + 1
            ipp = i - 1
        else:
            inn = i - 2
            ipp = i - 1
        for j in range(0, len(cornerTemp)):
            jnn = 0
            jpp = 0
            if j % 3 is 0:
                jnn = j + 1
                jpp = j + 2
            elif j % 3 is 1:
                jnn = j + 1
                jpp = j - 1
            else:
                jnn = j - 2
                jpp = j - 1
            if (cornerTemp[inn] is cornerTemp[jpp]) and cornerTemp[jnn] is cornerTemp[ipp]:
                oppos[i] = j
                oppos[j] = i

def create_sphere(l, lo):
    global vertTemp, cornerTemp
    vertTemp = []
    cornerTemp = []
    for i in range(1-l, l):
        for j in range(0, lo):
            t = HALF_PI*(i/l)
            s = TWO_PI*(j/lo)
            tplus = HALF_PI*((i+1)/l)
            tminus = HALF_PI*((i-1)/l)
            splus = TWO_PI*((j+1)/lo)
            cornerTemp.append(getVIndex(cos(t) * cos(s), cos(t) * sin(s), sin(t), vertTemp ) )
            cornerTemp.append(getVIndex(cos(t) * cos(splus), cos(t) * sin(splus), sin(t), vertTemp ) )
            cornerTemp.append(getVIndex(cos(tplus) * cos(s), cos(tplus) * sin(s), sin(tplus), vertTemp ) )
            cornerTemp.append(getVIndex( cos(t) * cos(s), cos(t) * sin(s), sin(t), vertTemp ) )
            cornerTemp.append(getVIndex( cos(tminus) * cos(splus), cos(tminus) * sin(splus), sin(tminus), vertTemp ) )
            cornerTemp.append(getVIndex( cos(t) * cos(splus), cos(t) * sin(splus), sin(t), vertTemp ) )
            
    generateAdj()
    
def getVIndex(x,y,z,vList):
    for i in range(0, len(vList)):
        v = vList[i]
        if v.equalTo(vertexTemp(x,y,z)):
            return i
    
    vList.append(vertexTemp(x,y,z))
    return len(vList) - 1

def dualD():
    global vertTemp, cornerTemp, face
    newvertTemp = []
    newcornerTemp = []
    
    for i in range(0, len(vertTemp)):
        v = vertTemp[i]
        cents = []
        if v.faces[0] == None:
            sFace = 0
        else:
            sFace = v.faces[0]
        face = sFace
        failsafe = 0
        while True:
            cents.append(centroid1(face))
            corneroffset = 0
            for j in range(0, 3):
                if cornerTemp[face*3 + j] == i:
                    corneroffset = j
            face = oppos[face*3 + ((corneroffset+1)%3)] / 3
            failsafe = failsafe + 1
            if (face is not sFace and failsafe<100) is False:
                break
        newcentroid = centroid(cents)
        for i in range(0, len(cents)):
            k = (i+1)%len(cents)
            newcornerTemp.append(getVIndex(newcentroid.x, newcentroid.y, newcentroid.z, newvertTemp))
            newcornerTemp.append(getVIndex(cents[i].x, cents[i].y, cents[i].z, newvertTemp))
            newcornerTemp.append(getVIndex(cents[k].x, cents[k].y, cents[k].z, newvertTemp))
    
    vertTemp = newvertTemp
    cornerTemp = newcornerTemp
    generateAdj()

def centroid1(t):
    tri = []
    tri.append(vertTemp[cornerTemp[t*3]])
    tri.append(vertTemp[cornerTemp[t*3+1]])
    tri.append(vertTemp[cornerTemp[t*3+2]])
    return centroid(tri)

def centroid(p):
    x= 0
    y= 0
    z =0
    for i in range(len(p)):
        x = x + p[i].x
        y = y + p[i].y
        z = z + p[i].z
    x = x/len(p)
    y = y/len(p)
    z = z/len(p)
    return vertexTemp(x,y,z)
            