import turtle as tr
tr.speed(5)
tr.penup()
tr.goto(-300,0)
tr.pendown()
x=-300
y=0
ay=-2
dt=0.1
for i in range(5):
    Vx=10-2*i
    Vy=20-2*i
    while y>=0:
        tr.goto(x,y)
        x += Vx*dt
        y += Vy*dt + ay*dt**2/2
        Vy += ay*dt
    y=0
tr.done()