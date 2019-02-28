#CS3451 Project 1B
#Hyungsuk Do
#hdo31

# In the routine below, you should draw your initials in perspective

from matlib import *
from drawlib import *


def persp_initials():
    
    gtInitialize()

    
    gtPerspective (80, -100, 100)
    gtTranslate(0, 0, -100)
    gtRotateX(-27)
    
    # HD <- my initials
    gtBeginShape ()

    gtVertex (-50, -50, 0)
    gtVertex (-50, 50, 0)
    
    gtVertex (5, 50, 0)
    gtVertex (20, 50, 0)

    gtVertex (-5, 50, 0)
    gtVertex (-5, -50, 0)
    
    gtVertex (5, -50, 0)
    gtVertex (5, 50, 0)

    gtVertex (-50, 0, 0)
    gtVertex (-5, 0, 0)
    

    gtVertex (5, -50, 0)
    gtVertex (20, -50, 0)
    
    gtVertex (20, 50, 0)
    gtVertex (35, 47, 0)
    
    gtVertex (35, 47, 0)
    gtVertex (45, 44, 0)

    gtVertex (45, 44, 0)
    gtVertex (50, 38, 0)
    
    gtVertex (50, 38, 0)
    gtVertex (53, 30, 0)
    
    gtVertex (53, 30, 0)
    gtVertex (54, 20, 0)
    
    gtVertex (54, 20, 0)
    gtVertex (54.5, 0, 0)
    
    gtVertex (54.5, 0, 0)
    gtVertex (54, -20, 0)

    gtVertex (54, -20, 0)
    gtVertex (53, -30, 0)
    
    gtVertex (20, -50, 0)
    gtVertex (35, -47, 0)
    
    gtVertex (35, -47, 0)
    gtVertex (45, -44, 0)

    gtVertex (45, -44, 0)
    gtVertex (50, -38, 0)
    
    gtVertex (50, -38, 0)
    gtVertex (53, -30, 0)
    
    
    gtEndShape()
    