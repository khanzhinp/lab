from random import randrange as rnd, choice
import tkinter as tk
from tkinter import *
import math

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.title('Пушка')
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball:
    def __init__(self, x=60, y=500):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 6
        self.v_X = 2
        self.v_Y = 2
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.health_points = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        g_sp = -2
        self.x += self.v_X
        self.y -= self.v_Y - 0.5 * g_sp ** 2
        self.v_X += 0
        self.v_Y += g_sp
        self.health_points += -1
        self.set_coords()

        if self.x + self.r <= 0:
            self.v_X = -self.v_X
        if self.x + self.r >= 800:
            self.v_X = -self.v_X
        if self.y + self.r <= 0:
            self.v_Y = -self.v_Y
        if self.y + self.r >= 600:
            self.v_Y = -self.v_Y

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x)**2 + (obj.y - self.y)**2 <= (self.r + obj.r)**2:
            return True
        else:
            return False

    def delete(self):
        canv.delete(self.id)


class Gun:
    def __init__(self):
        self.f2_power = 4
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)
        self.x_1 = 25
        self.y_1 = 535
        self.x_2 = 55
        self.y_2 = 505
        self.down = canv.create_rectangle(self.x_1 - 10, self.y_1, self.x_2 - 5, self.y_1 + 15, fill='red')

    def gun_move_right(self):
        if self.x_2 <= 785:
            self.x_1 += 10
            self.x_2 += 10
            canv.coords(self.id, self.x_1, self.y_1,
                        self.x_1 + max(self.f2_power, 20) * math.cos(self.an),
                        self.y_1 + max(self.f2_power, 20) * math.sin(self.an)
                        )
            canv.coords(self.down, self.x_1 - 10, self.y_1, self.x_2 - 5, self.y_1 + 15)

    def gun_move_left(self):
        if self.x_1 >= 15:
            self.x_1 -= 10
            self.x_2 -= 10
            canv.coords(self.id, self.x_1, self.y_1,
                        self.x_1 + max(self.f2_power, 20) * math.cos(self.an),
                        self.y_1 + max(self.f2_power, 20) * math.sin(self.an)
                        )
            canv.coords(self.down, self.x_1 - 10, self.y_1, self.x_2 - 5, self.y_1 + 15)

    def fire1_start(self):
        self.f2_on = 1

    def fire1_end(self, event):
        global balls, shots
        shots += 1
        new_ball = Ball(self.x_1, self.y_1)
        new_ball.r += 10
        if (event.x - self.x_1) >= 0:
            self.an = math.atan((event.y - self.y_1) / (event.x - self.x_1))
        else:
            self.an = math.pi + math.atan((event.y - self.y_1) / (event.x - self.x_1))
        new_ball.v_X = self.f2_power * math.cos(self.an)
        new_ball.v_Y = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def fire2_start(self, event):
        self.f2_on = 1
        self.x = event.x
        self.y = event.y

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча v_X и v_Y зависят от положения мыши.
        """
        global balls, shots
        shots += 1
        new_ball = Ball()
        new_ball.r += 5
        if (event.x - self.x_1) >= 0:
            self.an = math.atan((event.y - self.y_1) / (event.x - self.x_1))
        else:
            self.an = math.pi + math.atan((event.y - self.y_1) / (event.x - self.x_1))
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.v_X = self.f2_power * math.cos(self.an)
        new_ball.v_Y = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if (event.x - self.x_1) >= 0:
                self.an = math.atan((event.y-self.y_1) / (event.x-self.x_1))
            else:
                self.an = math.pi + math.atan((event.y - self.y_1) / (event.x - self.x_1))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x_1, self.y_1,
                    self.x_1 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y_1 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


def delete(self):
    canv.delete(self.id)


class Target:
    def __init__(self):
        self.health_points = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        col = (['blue'])
        self.new_target(col)
        self.v_X = rnd(1, 10)
        self.v_Y = rnd(1, 10)

    def new_target(self, col):
        """ Инициализация новой цели. """
        self.x = rnd(50, 759)
        self.y = rnd(50, 459)
        self.r = rnd(10, 40)
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=col)

    def new_target1(self, color):
        self.x = rnd(50, 759)
        self.y = rnd(50, 459)
        self.r = rnd(10, 15)
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=color)

    def hit(self):
        """Попадание шарика в цель."""
        global score
        canv.coords(self.id, 0, 0, 0, 0)
        score += 1
    
    def target_move(self):
        x = self.x
        y = self.y
        r = self.r

        self.x += self.v_X
        self.y += self.v_Y
        canv.coords(self.id, x - r, y - r, x + r, y + r)

        if self.x + self.r <= 40:
            self.v_X = -self.v_X
        if self.x + self.r >= 760:
            self.v_X = -self.v_X
        if self.y + self.r <= 40:
            self.v_Y = -self.v_Y
        if self.y + self.r >= 460:
            self.v_Y = -self.v_Y

    def target1_move(self):
        x = self.x
        y = self.y
        r = self.r
        if x + r <= 40:
            x += 10
        if x + r >= 290:
            x += -10
        else:
            x += choice([-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25])
        if y + r <= 99:
            y += 99
        if y + r >= 449:
            y += -99
        else:
            y += choice([-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25])
        canv.coords(self.id, x - r, y - r, x + r, y + r)

    def delete(self):
        canv.delete(self.id)


t_1 = Target()
t_2 = Target()
score = 0
screen = canv.create_text(400, 300, text='', font='28')
id_score = canv.create_text(30, 30, text='', font='28')
g = Gun()
shots = 0
balls = []


def start():
    root.geometry('800x600')
    but.destroy()
    fra.destroy()
    rules.destroy()
    new_game()


fra = Frame(root, width=600, height=600, bg="white")
fra.place(x=0, y=0)

but = Button(text='Старт', width=90, height=6)
but.config(command=start)
but.place(x=0, y=0)

rules = Label(root, text='Нажмите "старт" для начала игры', font="Arial 15", bg="white", fg="blue",
              width=90, height=35)
rules.place(x=0, y=120)


def ending():
    quit()


def new_game():
    global t_1, screen, balls, shots
    t_1.new_target('blue')
    t_2.new_target1('red')
    shots = 0
    balls = []
    
    canv.bind('<Button-1>', g.fire2_start)
    canv.bind('<ButtonRelease-1>', g.fire2_end)
    canv.bind('<Motion>', g.targetting)

    canv.focus_set()
    canv.bind('<Right>', g.gun_move_right)
    canv.bind('<Left>', g.gun_move_left)

    t_1.health_points = 1
    t_2.health_points = 1
    while t_1.health_points or t_2.health_points or balls:
        if t_1.health_points > 0:
            t_1.target_move()
        if t_2.health_points > 0:
            t_2.target1_move()

        for b in balls:
            b.move()
            if b.hittest(t_1) and t_1.health_points:
                t_1.health_points = 0
                t_1.hit()
                canv.itemconfig(id_score, text=str(score))
            if t_1.health_points == 0 and t_2.health_points == 0:
                canv.itemconfig(screen, text='')
                canv.itemconfig(screen, text='Ты уничтожил мишень за ' + str(shots) + ' выстрелов')
        for i in range(len(balls)):
            if balls[i].health_points <= 0:
                balls[i].delete()
                balls[i] = None
        balls = [p for p in balls if p is not None]

        for b in balls:
            b.move()
            if b.hittest(t_2) and t_2.health_points:
                t_2.health_points = 0
                t_2.hit()
                canv.itemconfig(id_score, text=str(score))
            if t_1.health_points == 0 and t_2.health_points == 0:
                canv.itemconfig(screen, text='')
                canv.itemconfig(screen, text='Ты уничтожил мишень за ' + str(shots) + ' выстрелов')
        for i in range(len(balls)):
            if balls[i].health_points <= 0:
                balls[i].delete()
                balls[i] = None
        balls = [p for p in balls if p is not None]

        canv.update()
        g.targetting()
        g.power_up()
    canv.itemconfig(screen, text='')
    canv.delete(Gun)
    root.after(750, new_game)


root.mainloop()
