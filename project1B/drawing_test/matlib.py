#CS3451 Project 1B
#Hyungsuk Do
#hdo31

# Matrix Stack Library -- Use your code from Project 1A
import copy
ctm = [0] * 4 # 4*4 identity matrix
stack = [] #stack
temp = [] # for copying top of the stack 
imat = [0] * 4 # 4*4 identity matrix
tmat = [0] * 4 # a arbitrary vector
temp1 = [] # the result matrix after two matrixs multiply

def gtInitialize():
    stack[:] = []
    for i in range(4):
        ctm[i] = [0] * 4
        ctm[i][i] = 1.0
    stack.append(ctm) # first top of the stack
    #gtFlipY()

def gtPushMatrix():
    stack.append(stack[-1]) # push in the stack

def gtPopMatrix():
    if len(stack) == 1 : # if there is one in the stack
        println("cannot pop the matrix stack")
    else :
        stack.pop() # pop from the top of the stack

def gtTranslate(x, y, z):
    gtImatInit(imat) # initialize a identity matrix
    temp = copy.deepcopy(stack[-1]) # copy top of the stack 
    temp1 = copy.deepcopy(stack[-1]) # copy top of the stack 
    imat[0][3] = x 
    imat[1][3] = y 
    imat[2][3] = z 
    imat[3][3] = 1
    gtMult(temp, imat, temp1) #temp1 = temp * imat 
    stack[-1] = temp1 # store the matrix on the top of stack

def gtScale(x, y, z):
    gtImatInit(imat)
    temp = copy.deepcopy(stack[-1])
    temp1 = copy.deepcopy(stack[-1]) 
    imat[0][0] = imat[0][0] * x
    imat[1][1] = imat[1][1] * y
    imat[2][2] = imat[2][2] * z
    imat[3][3] = 1
    gtMult(temp, imat, temp1)
    stack[-1] = temp1

def gtRotateX(theta):
    gtImatInit(imat)
    temp = copy.deepcopy(stack[-1])
    temp1 = copy.deepcopy(stack[-1]) 
    imat[1][1] = cos(radians(theta))
    imat[1][2] = -sin(radians(theta))
    imat[2][1] = sin(radians(theta))
    imat[2][2] = cos(radians(theta))
    gtMult(temp, imat, temp1)
    stack[-1] = temp1

def gtRotateY(theta):
    gtImatInit(imat)
    temp = copy.deepcopy(stack[-1])
    temp1 = copy.deepcopy(stack[-1]) 
    imat[0][0] = cos(radians(theta))
    imat[0][2] = sin(radians(theta))
    imat[2][0] = -sin(radians(theta))
    imat[2][2] = cos(radians(theta))
    gtMult(temp, imat, temp1)
    stack[-1] = temp1

def gtRotateZ(theta):
    gtImatInit(imat)
    temp = copy.deepcopy(stack[-1])
    temp1 = copy.deepcopy(stack[-1])
    imat[0][0] = cos(radians(theta))
    imat[0][1] = -sin(radians(theta))
    imat[1][0] = sin(radians(theta))
    imat[1][1] = cos(radians(theta))
    gtMult(temp, imat, temp1)
    stack[-1] = temp1

# Multiply with two matrix 
def gtMult(mat1, mat2, mat3):
    for r in range(len(mat1)) :
        for c in range(len(mat2[-1])):
            mat3[r][c] = 0 # initialize mat3 matrix with all 0 in temp1
            for run in range(len(mat1)) :
                  mat3[r][c] += mat1[r][run] * mat2[run][c] # store multiplication of two elements and add

# Initialize a 4*4 Identity Matrix
def gtImatInit(a) :
    for i in range(4):
        a[i] = [0] * 4 ## 4*4 identity matrix
        a[i][i] = 1.0

# # Flip Y-axis
# def gtFlipY():
#     gtScale(1, -1, 1)
#     gtTranslate(0, -height, 0)
    
    
    
    