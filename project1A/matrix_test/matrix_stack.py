# CS3451 Project 1
# Hyungsuk Do
# hdo31@gatech.edu

# Matrix Stack Library
import copy
ctm = [0] * 4 # 4*4 identity matrix
stack = [] #stack
temp = [] # for copying top of the stack 
imat = [0] * 4 # 4*4 identity matrix
temp1 = [] # the result matrix after two matrixs multiply

# you should modify the routines below to complete the assignment

# a two-dimensional list cannot be created simply by repeating a string
# create a list of n elements (say, of n zeros) 
# and then make each of the elements a link to another one-dimensional list of m elements
def gtInitialize():
    stack[:] = []
    for i in range(4):
        ctm[i] = [0] * 4
        ctm[i][i] = 1
    stack.append(ctm) # first top of the stack

def gtPushMatrix():
    stack.append(stack[-1]) # push in the stack

def gtPopMatrix():
    if len(stack) == 1 : # if there is one in the stack
        println("cannot pop the matrix stack")
    else :
        stack.pop() # pop from the top of the stack

def gtTranslate(x, y, z):
    gtImatInit() # initialize a identity matrix
    temp = copy.deepcopy(stack[-1]) # copy top of the stack 
    temp1 = copy.deepcopy(stack[-1]) # copy top of the stack 
    imat[0][3] = float(x) 
    imat[1][3] = float(y) 
    imat[2][3] = float(z) 
    imat[3][3] = float(1)
    gtMult(temp, imat, temp1) #temp1 = temp * imat 
    stack[-1] = temp1 # store the matrix on the top of stack
    
def gtScale(x, y, z):
    gtImatInit()
    temp = copy.deepcopy(stack[-1])
    temp1 = copy.deepcopy(stack[-1]) 
    imat[0][0] = imat[0][0] * x
    imat[1][1] = imat[1][1] * y
    imat[2][2] = imat[2][2] * z
    gtMult(temp, imat, temp1)
    stack[-1] = temp1

def gtRotateX(theta):
    gtImatInit()
    temp = copy.deepcopy(stack[-1])
    temp1 = copy.deepcopy(stack[-1]) 
    imat[1][1] = cos(radians(theta))
    imat[1][2] = -sin(radians(theta))
    imat[2][1] = sin(radians(theta))
    imat[2][2] = cos(radians(theta))
    gtMult(temp, imat, temp1)
    stack[-1] = temp1
    
def gtRotateY(theta):
    gtImatInit()
    temp = copy.deepcopy(stack[-1])
    temp1 = copy.deepcopy(stack[-1]) 
    imat[0][0] = cos(radians(theta))
    imat[0][2] = sin(radians(theta))
    imat[2][0] = -sin(radians(theta))
    imat[2][2] = cos(radians(theta))
    gtMult(temp, imat, temp1)
    stack[-1] = temp1

def gtRotateZ(theta):
    gtImatInit()
    temp = copy.deepcopy(stack[-1])
    temp1 = copy.deepcopy(stack[-1])
    imat[0][0] = cos(radians(theta))
    imat[0][1] = -sin(radians(theta))
    imat[1][0] = sin(radians(theta))
    imat[1][1] = cos(radians(theta))
    gtMult(temp, imat, temp1)
    stack[-1] = temp1

# def gtGetMatrix():
#     pass

def print_ctm():
    for i in range(0, 4):
        println(stack[-1][i])
    #println(len(stack[-1]))
    print("\n")
    
# Multiply with two 4*4 matrix 
def gtMult(mat1, mat2, mat3):
    for r in range(len(mat1)) :
        for c in range(len(mat2[-1])):
            mat3[r][c] = 0 # initialize 4*4 matrix with all 0 in temp1
            for run in range(len(mat1)) :
                  mat3[r][c] += mat1[r][run] * mat2[run][c] # store multiplication of two elements and add

# Initialize a 4*4 Identity Matrix
def gtImatInit() :
    for i in range(4):
        imat[i] = [0] * 4 ## 4*4 identity matrix
        imat[i][i] = 1
    