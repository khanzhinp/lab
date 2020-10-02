import turtle as tr
import numpy as np
tr.shape('turtle')
tr.speed(3)
def stars(n):
    for i in range(n):
        tr.forward(100)
        tr.right(180-180/n)

stars(5)
tr.penup()
tr.forward(180)
tr.pendown()
stars(11) 

tr.done()