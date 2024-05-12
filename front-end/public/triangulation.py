from easy_trilateration.model import *  
from easy_trilateration.least_squares import easy_least_squares  
from easy_trilateration.graph import *  
def drawimage(r1,r2,r3):  
      arr = [Circle(0, 1, r1),  
    Circle(3, 0, r2),  
    Circle(6, 1, r3)]  
      result, meta = easy_least_squares(arr)  
      create_circle(result, target=True)  
      draw(arr)
