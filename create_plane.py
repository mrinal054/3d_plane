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
x1, y1 = -10, 85.3       
x2, y2 = -17.5, 90.2

# Calculate point p3 perpendicular to line([x1,y1], [x2,y2])
x3, y3, r3, angle3 = perpendicular(x1, y1, x2, y2)
print(x3, y3)

# Find point p4 opposite to p3
'''
x4 = x1 - xadd and y4 = y1 - yadd
where, xadd = rcos(theta) and yadd = rsin(theta)
'''
xadd = r3*math.cos(angle3)
yadd = r3*math.sin(angle3)
x4, y4 = x1-xadd, y1-yadd
#plt.plot(x4, y4, 'r*')
#plt.plot([x4, x1], [y4, y1])

# 3D plotting

fig = plt.figure()
ax = plt.axes(projection='3d')
#x = [x1, x2, x3, x4]
#y = [y1, y2, y3, y4]
#z = [0, 0, 0, 0]
x12, y12 = [x1,x2], [y1,y2]
ax.plot3D(x12, y12)
x13, y13 = [x1,x3], [y1,y3]
ax.plot3D(x13, y13)
x14, y14 = [x1,x4], [y1,y4]
ax.plot3D(x14, y14)

plt.show()









