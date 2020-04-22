'''
This code is to create a perpendicular to a given line
Author: Mrinal Kanti Dhar
'''

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

def perpendicular(x1, y1, x2, y2):
    '''
    This function creates a perpendicular to a given line.
    input parameter:
        x1, y1, x2, y2 --> co-ordinates of the given line
    output parameter:
        xnew, ynew --> co-ordinates of the new point
        rnew --> length of the new line
    '''

    def cal_cord(x1, y1, r1, thetaRad):
        '''
        This function is used to calculate the co-ordinates of a point which is 
        perpendicular of a given line. 
        input parameter:
            x1, y1 --> co-ordinates of a given point
            r --> hypotenuse
            thetaRad --> theta in radian
        output:
            x2, y2 --> co-ordinates of the new point
        '''
        dx = r1*math.cos(thetaRad)
        x2 = x1 + dx
        dy = r1*math.sin(thetaRad)
        y2 = y1 + dy
        r2 = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        
        return x2, y2, r2
        
    # Calculate slopes 
    m1 = (y2-y1)/(x2-x1)    # slope of the first line
    m2 = -1/m1              # slope of the 2nd line
    
    r1 = np.sqrt((x1-x2)**2 + (y1-y2)**2)   # length of the given line
    
    # Check if the angle between two lines is 90 degree or not
    angle1 = math.atan(m1)*180/3.1416   # angle for the first line
    angle2 = math.atan(m2)*180/3.1416   # angle for the 2nd line
    diff = angle2 - angle1              # diff betn two angles
    
    print('Theta1: {:.3f}, Theta2: {:.3f}, diff: {:.3f}'.format(angle1, angle2, diff))
     
    xnew, ynew, rnew = cal_cord(x1, y1, r1, math.atan(m2))
    
#    plt.figure()
#    plt.plot([x1,x2], [y1,y2])
#    plt.plot([x1,xnew], [y1,ynew])
    
    return xnew, ynew, rnew, math.atan(m2)

# Define two points
x1, y1 = 104.22, 149.79       
x2, y2 = 102.95, 138.04
z1, z2 = 0, 81.73
# Calculate point p3 perpendicular to line([x1,y1], [x2,y2])
x3, y3, r13, angle3 = perpendicular(x1, y1, x2, y2)
print(x3, y3)

# Find point p4 opposite to p3
'''
x4 = x1 - xadd and y4 = y1 - yadd
where, xadd = rcos(theta) and yadd = rsin(theta)
'''
xadd = r13*math.cos(angle3)
yadd = r13*math.sin(angle3)
x4, y4 = x1-xadd, y1-yadd
#plt.plot(x4, y4, 'r*')
#plt.plot([x4, x1], [y4, y1])

r14 = np.sqrt((x1-x4)**2 + (y1-y4)**2)
#%%
# 3D plotting

fig = plt.figure()
ax = plt.axes(projection='3d')
#x = [x1, x2, x3, x4]
#y = [y1, y2, y3, y4]
#z = [0, 0, 0, 0]
z1, z2, z3, z4 = 0, 81.73, 0, 0
# Line12
x12, y12, z12 = [x1,x2,], [y1,y2], [z1,z2]
ax.plot3D(x12, y12, z12)
# Line13
x13, y13, z13 = [x1,x3], [y1,y3], [z1,z3]
ax.plot3D(x13, y13, z13)
# Line14
x14, y14, z14 = [x1,x4], [y1,y4], [z1,z4]
ax.plot3D(x14, y14, z14)
## Line45
#x5, y5, z5 = x4, y4, z4+r13
#x45, y45, z45 = [x4,x5], [y4,y5], [z4, z5]
#ax.plot3D(x45, y45, z45)
## Line46
#x6, y6, z6 = x4, y4, z4-r13
#x46, y46, z46 = [x4,x6], [y4,y6], [z4,z6]
#ax.plot3D(x46,y46,z46)
## Line37
#x7, y7, z7 = x3, y3, z3+r13
#x37, y37, z37 = [x3,x7], [y3,y7], [z3, z7]
#ax.plot3D(x37, y37, z37)
## Line38
#x8, y8, z8 = x3, y3, z3-r13
#x38, y38, z38 = [x3,x8], [y3,y8], [z3, z8]
#ax.plot3D(x38, y38, z38)
## Line57
#x57, y57, z57 = [x5,x7], [y5,y7], [z5,z7]
#ax.plot3D(x57, y57, z57)
## Line68
#x68, y68, z68 = [x6,x8], [y6,y8], [z6,z8]
#ax.plot3D(x68, y68, z68)


#
y5, z5, r15, angle5 = perpendicular(y1, z1, y2, z2)
x5 = x1
x15 = [x1,x1]
y15 = [y1,y5]
z15 = [z1,z5]
ax.plot3D(x15,y15,z15)

yadd2 = r15*math.cos(angle5)
zadd2 = r15*math.sin(angle5)
y6, z6 = y1-yadd2, z1-zadd2
x16 = [x1,x1]
y16 = [y1,y6]
z16 = [z1,z6]

ax.plot3D(x16,y16,z16)

plt.show()
#%%
# Calculate p5












