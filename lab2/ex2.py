import turtle as tr
tr.shape('turtle')
tr.speed(5)

tr.penup()
tr.forward(-300)
sqr=50*2**0.5
def draw_num(A):
    tr.pendown()
    for i in range(len(A)):
        alpaka,x,invis=A[i]
        if invis==1:
            tr.penup()
            tr.left(alpaka)
            tr.forward(x)
            tr.pendown()
        else:
            tr.left(alpaka)
            tr.forward(x)
    tr.penup()
    tr.forward(75)

num_0=[(0,50,0), (90,100,0), (90,50,0), (90,100,0), (90,0,0)]
num_1=[(0,50,1), (90,100,0), (135,sqr,0), (45,50,1), (90,0,0)]
num_2=[(0,50,1), (180,50,0), (-135,sqr,0), (45,50,0), (90,50,0), (90,100,1), (90,0,0)]
num_3=[(45,sqr,0), (135,50,0), (-135,sqr,0), (135,50,0), (90,100,1), (90,0,0)]
num_4=[(0,50,1), (90,100,0), (180,50,1), (-90,50,0), (-90,50,0), (180,100,1), (90,0,0)]
num_5=[(0,50,0), (90,50,0), (90,50,0), (-90,50,0), (-90,50,0), (180,50,1), (90,100,1), (90,0,0)]
num_6=[(0,50,0), (90,50,0), (90,50,0), (-135,sqr,0), (135,50,1), (90,50,1), (0,50,0), (90,0,0)]
num_7=[(90,50,0), (-45,sqr,0), (135,50,0), (90,100,1), (90,0,0)]
num_8=[(0,50,0), (90,100,0), (90,50,0), (90,100,0), (90,0,0), (45,sqr,1), (135,50,0), (90,50,1), (90,0,0)]
num_9=[(45,sqr,0), (135,50,0), (-90,50,0), (-90,50,0), (-90,50,0), (-45,sqr,1), (135,0,0)]

draw_num(num_1)
draw_num(num_4)
draw_num(num_1)
draw_num(num_7)
draw_num(num_0)
draw_num(num_0)

tr.done()