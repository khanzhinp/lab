import turtle as tr
import numpy as np
tr.shape('turtle')
k=50
def polygons(a,x):
    tr.penup()
    tr.forward(a)
    tr.pendown()
    tr.right(90*(x+2)/x)
    for i in range(x):
        tr.forward(a*2*np.sin(np.pi/x))
        tr.right(360/x)
    tr.right(90*(x-2)/x)
    tr.penup()
    tr.forward(a)
    tr.pendown()
for i in range(3,13):
    polygons(k,i)
    k+=20
tr.done()
