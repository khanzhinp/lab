import turtle as tr
tr.shape('turtle')
tr.speed(200)
def circle1(n):
	pv=360/n
	for i in range(n):
		tr.forward(1)
		tr.right(pv)
def circle2(n):
	pv=360/n
	for i in range(n):
		tr.forward(1)
		tr.right(-pv)
p=360
for i in range(8):
    circle1(p)
    circle2(p)
    p+=90
tr.done()
