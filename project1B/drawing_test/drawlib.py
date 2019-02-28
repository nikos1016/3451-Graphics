#CS3451 Project 1B
#Hyungsuk Do
#hdo31

# Drawing Routines, like OpenGL

from matlib import *
import copy
import math

tVL = []
tM = [0] * 4
tempM = []
k = 0.0
th = 0.0
th1 = 0
th2 = 0
th3 = 0
th4 = 0
per = 0.0

def gtOrtho(left, right, bottom, top, near, far):
    global per, th1, th2, th3, th4, th
    per = 0.0
    th = 1.0
    th1 = left
    th2 = right
    th3 = bottom
    th4 = top

def gtPerspective(fov, near, far):
    global k, per, th
    k = float(tan(radians(fov/2)))
    per = 1.0
    th = 0.0

def gtBeginShape():
    tVL[:] = []

def gtEndShape():
    i = 0
    j = 0
    while j < len(tVL) :
        tempM = copy.deepcopy(tVL[j])
        gtMult(stack[-1], tVL[j], tempM)
        tVL[j] = tempM
        j = j + 1
    while i < len(tVL) :
        if tVL[i][2][0] != 0 : 
            if per == 1.0 :
                tVL[i][0][0] = ((tVL[i][0][0]/abs(tVL[i][2][0])) + k) * (width/(2*k))
                tVL[i][1][0] = -((((tVL[i][1][0]/abs(tVL[i][2][0])) + k) * (height/(2*k))) - height)
                tVL[i+1][0][0] = ((tVL[i+1][0][0]/abs(tVL[i+1][2][0])) + k) * (width/(2*k))
                tVL[i+1][1][0] = -(((tVL[i+1][1][0]/abs(tVL[i+1][2][0])) + k) * (height/(2*k)) - height)
                line(tVL[i][0][0], tVL[i][1][0], tVL[i+1][0][0], tVL[i+1][1][0])
            elif th == 1.0:
                    tVL[i][0][0] = (tVL[i][0][0] - th1) * (width/(th2 - th1))
                    tVL[i][1][0] = -((tVL[i][1][0] - th3) * (height/(th4 - th3)) - height)
                    tVL[i+1][0][0] = (tVL[i+1][0][0] - th1) * (width/(th2 - th1))
                    tVL[i+1][1][0] = -((tVL[i+1][1][0] - th3) * (height/(th4 - th3)) - height)
                    line(tVL[i][0][0], tVL[i][1][0], tVL[i+1][0][0], tVL[i+1][1][0])
        else :
            if th == 1.0:
                tVL[i][0][0] = (tVL[i][0][0] - th1) * (width/(th2 - th1))
                tVL[i][1][0] = -((tVL[i][1][0] - th3) * (height/(th4 - th3)) - height)
                tVL[i+1][0][0] = (tVL[i+1][0][0] - th1) * (width/(th2 - th1))
                tVL[i+1][1][0] = -((tVL[i+1][1][0] - th3) * (height/(th4 - th3)) - height)
                line(tVL[i][0][0], tVL[i][1][0], tVL[i+1][0][0], tVL[i+1][1][0])
            else :
                line(tVL[i][0][0], -(tVL[i][1][0] - height), tVL[i+1][0][0], -(tVL[i+1][1][0] - height))
        i = i + 2
    
def gtVertex(x, y, z):
    tV = tM
    tVL.append(tV)
    tV = copy.deepcopy(tVL[-1])
    tV[0] = [x]
    tV[1] = [y]
    tV[2] = [z]
    tV[3] = [1]
    tVL[-1] = tV