import turtle as tr
tr.shape('turtle')
tr.speed(200)
def circle(n):
	pv=360/n
	for i in range(n//2):
		tr.forward(1)
		tr.right(pv)
rb=180
rm=30
p=5
tr.left(90)
for i in range(p):
    circle(rb)
    circle(rm)
tr.done()