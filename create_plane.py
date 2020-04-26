'''
This code is to create a plane perpendicular to a given line
Author: Mrinal Kanti Dhar
'''

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

def perpendicular(x1, y1, x2, y2, scale_factor):
    '''
    This function creates a perpendicular to a given line.
    input parameter:
        x1, y1, x2, y2 --> co-ordinates of the given line
        scale_factor --> determines how far the new point will be from the origin
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
     
    xnew, ynew, rnew = cal_cord(x1, y1, scale_factor*r1, math.atan(m2))
    
    return xnew, ynew, rnew, math.atan(m2)

# Define two points
x1, y1 = 104.22, 149.79       
x2, y2 = 102.95, 138.04
z1, z2 = 0, 81.73

scale_factor = 0.5  # It defines how far the new point will be from the origin

# Calculate point p3 perpendicular to line([x1,y1], [x2,y2])
x3, y3, r13, angle3 = perpendicular(x1, y1, x2, y2, scale_factor)

# Find point p4 opposite to p3
'''
x4 = x1 - xadd and y4 = y1 - yadd
where, xadd = rcos(theta) and yadd = rsin(theta)
'''
xadd = r13*math.cos(angle3)
yadd = r13*math.sin(angle3)
x4, y4 = x1-xadd, y1-yadd

r14 = np.sqrt((x1-x4)**2 + (y1-y4)**2)
#%% 3D plotting
fig = plt.figure()
ax = plt.axes(projection='3d')

z1, z2 = 0, 81.73
z3, z4 = z1, z1     # p1, p3, and p4 are at the same height
# Line12
x12, y12, z12 = [x1,x2,], [y1,y2], [z1,z2]
ax.plot3D(x12, y12, z12)
# Line13
x13, y13, z13 = [x1,x3], [y1,y3], [z1,z3]
ax.plot3D(x13, y13, z13, 'r')
# Line14
x14, y14, z14 = [x1,x4], [y1,y4], [z1,z4]
ax.plot3D(x14, y14, z14, 'r')

# Line 15 and 16
y5, z5, r15, angle5 = perpendicular(y1, z1, y2, z2, scale_factor)
x5 = x1
x15, y15, z15 = [x1,x1], [y1,y5], [z1,z5]
ax.plot3D(x15,y15,z15, 'r')

yadd6 = r15*math.cos(angle5)
zadd6 = r15*math.sin(angle5)
y6, z6 = y1-yadd6, z1-zadd6
x16, y16, z16 = [x1,x1], [y1,y6], [z1,z6]

ax.plot3D(x16,y16,z16, 'r')

# Line 37 and 38
y7, z7, r17, angle7 = perpendicular(y3, z3, y2, z2, scale_factor)
x7 = x1
x37, y37, z37 = [x3,x3], [y1,y7], [z1,z7]
ax.plot3D(x37,y37,z37, 'r')

yadd8 = r15*math.cos(angle7)
zadd8 = r15*math.sin(angle7)
y8, z8 = y1-yadd8, z1-zadd8
x38, y38, z38 = [x3,x3], [y1,y8], [z1,z8]

ax.plot3D(x38,y38,z38, 'r')

# Line 47 and 48
x47, y47, z47 = [x4,x4], [y1,y7], [z1,z7]
ax.plot3D(x47,y47,z47, 'r')

x48, y48, z48 = [x4,x4], [y1,y8], [z1,z8]
ax.plot3D(x48,y48,z48, 'r')

# Parallels to Line 34
x34, y77, z77 = [x3,x4], [y7,y7], [z7,z7]
ax.plot3D(x34, y77, z77, 'r')

x34, y88, z88 = [x3,x4], [y8,y8], [z8,z8]
ax.plot3D(x34, y88, z88, 'r')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

#%% Print
print('max x-cor: {}\nmin x-cor: {}\n\
max y-cor: {}\nmin y-cor: {}\n\
max z-cor: {}\nmin z-cor: {}\n'
.format(x3,x4,y5,y6,z5,z6))


