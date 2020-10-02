from random import randint
import turtle as tr


number_of_turtles = 20
steps_of_time_number = 100

A = []
i=0

pool = [tr.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.goto(randint(-350, 350), randint(-350, 350))
    A.append(randint(-180, 180))
    unit.right(A[i])
    unit.speed(10)
    i+=1

for i in range(steps_of_time_number):
    j=0
    for unit in pool:
        unit.forward(5)
        if (unit.ycor()>=350 or unit.ycor()<=-350):
          unit.left(2*A[j]) 
        if (unit.xcor()>=350 or unit.xcor()<=-350):
          unit.right(2*A[j])
        j+=1
tr.done()