import numpy as np
import math

# all values SI, rad
# body: [m, mu, matrix of base hull corners (origin on base directly below CofM)]
# force: [position vector, force vector]

g=9.81

def myhyp (components):
    if len (components)==1:
        return components[0]
    return myhyp ([math.hypot(components[1],components[2])+components[2:]])

def slipp (body,force):
    return force[1][1]>body[1]*(body[0]*g-math.hypot(force[1][0],force[1][2]))

def topplerange (body,force):
    return (math.hypot(force[0][0],force[0][2])*force[1][1]+force[0][1]*math.hypot(force[1][0],force[1][2]))/(body[0]*g-force[1][1])

def mindist (body):
    dists=[]
    for i in range(0,len(body[2])):
            i.append(abs(body[2][i][0]*body[2][i-1][1]-body[2][i][1]*body[2][i-1][0])/math.hypot(body[2][i][0]-body[2][i-1][0],body[2][i][1]-body[2][i-1][1]))
    return min(dists)

def topplep (body, force):
    return topplerange(body,force)>mindist(body)




print(topplep ([10,1,0],[0,[1,2,30]]))


