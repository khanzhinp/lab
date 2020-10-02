import turtle as tr
tr.shape('turtle')
tr.speed(20)
def circle(x):
	k=360/x
	for i in range(x):
		tr.forward(1)
		tr.right(k)
a=360
n=3
for i in range(n):
    circle(a)
    tr.right(180)
    circle(a)
    tr.right(180/n)
tr.done()