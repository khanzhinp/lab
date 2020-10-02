import turtle as tr
tr.shape('turtle')
tr.penup()
tr.speed(5)

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

def numer(hoh):
	for i in hoh:
		draw_num(numbers_dict[i])

with open('ex2.txt') as file:
	n_0 = eval(file.readline())
	n_1 = eval(file.readline())
	n_2 = eval(file.readline())
	n_3 = eval(file.readline())
	n_4 = eval(file.readline())
	n_5 = eval(file.readline())
	n_6 = eval(file.readline())
	n_7 = eval(file.readline())
	n_8 = eval(file.readline())
	n_9 = eval(file.readline())
numbers_dict = {0: n_0, 1: n_1, 2: n_2, 3: n_3, 4: n_4, 5: n_5, 6: n_6, 7: n_7, 8: n_8, 9: n_9}
numer([1,4,1,7,0,0])
tr.done()