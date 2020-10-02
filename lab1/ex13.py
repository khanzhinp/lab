import turtle as tr
import numpy as np
tr.shape('turtle')
tr.speed(200)
def circle(n):
	pv=360/n
	for i in range(n):
		tr.forward(1)
		tr.right(pv)
def hfcircle(n):
	pv=360/n
	for i in range(n//2):
		tr.forward(1)
		tr.right(pv)


tr.left(90)
tr.color('black', 'yellow')
tr.begin_fill()
circle(720)
tr.end_fill()
tr.penup()

d=1/np.sin(np.pi/720)
tr.goto(d/5,d/4)
tr.color('black', 'blue')
tr.pendown()
tr.begin_fill()
circle(120)
tr.end_fill()
tr.penup()

d_g=1/np.sin(np.pi/120)
tr.goto(4*d/5-d_g,d/4)
tr.pendown()
tr.begin_fill()
circle(120)
tr.end_fill()
tr.penup()

tr.goto(d/2,d/6)
tr.pendown()
tr.width(10)
tr.goto(d/2,-d/6)
tr.penup()

tr.goto(5*d/6,0)
smile=int(np.pi/np.arcsin(3/(2*d)))
tr.left(180)
tr.color('red')
tr.pendown()
hfcircle(smile)

tr.done()

