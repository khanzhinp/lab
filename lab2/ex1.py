import turtle as tr
from random import *
tr.shape('turtle')
tr.speed(20)
for i in range(300):
    tr.forward(randint(1,50))
    tr.right(randint(-180,180))
tr.done()
 