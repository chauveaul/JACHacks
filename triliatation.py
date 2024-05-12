import numpy as np
import math
def trilateration(P1, P2, P3, r1, r2, r3):

  p1 = np.array([0, 0])
  p2 = np.array([P2[0] - P1[0], P2[1] - P1[1]])
  p3 = np.array([P3[0] - P1[0], P3[1] - P1[1]])
  v1 = p2 - p1
  v2 = p3 - p1

  Xn = (v1)/np.linalg.norm(v1)

  tmp = np.cross(v1, v2)

  Zn = (tmp)/np.linalg.norm(tmp)

  Yn = np.cross(Xn, Zn)

  i = np.dot(Xn, v2)
  d = np.dot(Xn, v1)
  j = np.dot(Yn, v2)

  X = ((r1**2)-(r2**2)+(d**2))/(2*d)
  Y = (((r1**2)-(r3**2)+(i**2)+(j**2))/(2*j))-((i/j)*(X))

  K1 = P1 + X * Xn + Y * Yn 
  K2 = P1 + X * Xn + Y * Yn 
  return K1,K2
print(trilateration())
def trila(x1,x2,x3,y1,y2,y3,r1,r2,r3):
  exx=(x2-x1)/math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
  exy=(y2-y1)/math.sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1))
  