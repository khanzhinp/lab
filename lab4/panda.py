import pygame
from pygame.draw import *



# ====================| Константы |=======================
#   Цвета.
peach = 245, 175, 127
black = 0, 0, 0
white = 255, 255, 255
green = 44, 105, 56
red = 255, 0, 0

#   Константы приложения.
FPS = 30
pi = 3.14

# ========================================================

# Класс рисует панду в нужной позиции экрана.
class PandaDrawer:

    def __init__(self, sc):
        self.sc = sc

    def left_leg(self, x, y, w, h):
        polygon(self.sc, black, [[x, y],
                        [x + int(0.1 * w), y],
                        [x + int(0.15 * w), y + int(1.2 * h)],
                        [x + int(0.05 * w), y + int(1.3 * h)],
                        [x - int(0.05 * w), y + int(1.1 * h)]])
        circle(self.sc, black, (x + int(0.05 * w), y + int(1.2 * h)), int(h / 5))

    def right_leg(self, x, y, w, h):

        ellipse(self.sc, black, (x + int(0.85 * w), y + int(0.45 * h), int(0.2 * w), int(0.9 * h)))
        ellipse(self.sc, black, (x + int(0.8 * w), y + h, int(0.2 * w), int(0.4 * h)))

    def middle_leg(self, x, y, w, h):

        ellipse(self.sc, black, (x + int(0.25 * w), y + int(1.25 * h), int(0.3 * w), int(0.3 * h)))
        ellipse(self.sc, black, (x + int(0.28 * w), y + int(1.28 * h), int(0.25 * w), int(0.3 * h)))
        ellipse(self.sc, black, (x + int(0.20 * w), y + int(1.30 * h), int(0.3 * w), int(0.30 * h)))

        polygon(self.sc, black, [[x + int(0.35 * w), y],
                            [x + int(0.5 * w), y],
                            [x + int(0.5 * w), y + h],
                            [x + int(0.35 * w), y + h]])
        polygon(self.sc, black, [[x + int(0.3 * w), y + int(1.5 * h)],
                            [x + int(0.55 * w), y + int(1.4 * h)],
                            [x + int(0.5 * w), y + h],
                            [x + int(0.35 * w), y + h]])

    def head(self, x, y, w, h):
        circle(self.sc, black, (x, y - int(0.1 * h)), int(0.2 * h))

        circle(self.sc, white, (x + int(0.2 * w), y + int(0.3 * h)), int(0.55 * h))
        circle(self.sc, black, (x + int(0.2 * w), y + int(0.3 * h)), int(0.55 * h), 2)

        circle(self.sc, black, (x + int(0.3 * w), y - int(0.1 * h)), int(0.2 * h))

        circle(self.sc, black, (x, y + int(0.3 * h)), int(0.1 * h))
        circle(self.sc, black, (x + int(0.15 * w), y + int(0.3 * h)), int(0.1 * h))

        circle(self.sc, black, (x + int(0.04 * w), y + int(0.6 * h)), int(0.07 * h))

    def draw_panda(self, x, y, w, h):
        ellipse(self.sc, white, (x, y, w, h))
        ellipse(self.sc, black, (x, y, w, h), 2)

        self.left_leg(x, y, w, h)
        self.right_leg(x,y, w, h)
        self.middle_leg(x, y, w, h)
        self.head(x, y, w, h)

# Класс рисует дерево в нужной позиции экрана.
class BambooDrawer:

    def __init__(self, sc):
        self.sc = sc

    def branch_left(self, x, y, w, h):
        arc(self.sc, green, (x, y, w, h), 0, pi / 2 + pi / 10, 3)

    def branch_right(self, x, y, w, h):
        arc(self.sc, green, (x, y, w, h), pi / 2, pi, 3)


    def branches(self, w, h):
        self.branch_left(int(0.6 * w), int(2.55 * h), 6 * w, 3 * h)
        self.branch_left(int(1.45 * w), int(0.88 * h), int(5.5 * w), 2 * h)
        self.branch_right(int(7.8 * w), int(2.95 * h), 6 * w, 3 * h)
        self.branch_right(int(7.7 * w), int(1.6 * h), 8 * w, 2 * h)

    def leaf(self, x, y, w, h, angle):
       surf = pygame.Surface((int(3 * w), h))
       surf.fill(peach)
       ellipse(surf, green, (0, 0, w, h))
       surf.set_colorkey(peach)
       surface2 = pygame.transform.rotate(surf, angle)
       surface2.set_alpha(255)
       self.sc.blit(surface2, (x, y))

    def leaves(self, w, h):
        self.leaf(3 * w, int(0.9 * h), int(0.3 * w), int(0.7 * h), 170)
        self.leaf(int(3.6 * w), int(0.9 * h), int(0.3 * w), int(0.7 * h), 170)
        self.leaf(int(4.2 * w), h, int(0.3 * w), int(0.7 * h), 170)
        self.leaf(int(4.8 * w), int(h * 1.1), int(0.3 * w), int(0.7 * h), 170)

        self.leaf(int(2.8 * w), int(2.55 * h), int(0.3 * w), int(0.7 * h), 170)
        self.leaf(int(3.4 * w), int(2.6 * h), int(0.3 * w), int(0.7 * h), 170)
        self.leaf(4 * w, int(2.8 * h), int(0.3 * w), int(0.7 * h), 170)
        self.leaf(int(4.5 * w), int(2.95 * h), int(0.3 * w), int(0.7 * h), 170)

        self.leaf(int(9.5 * w), int(3.05 * h), int(0.3 * w), int(0.7 * h), 190)
        self.leaf(int(8.9 * w), int(3.1 * h), int(0.3 * w), int(0.7 * h), 190)
        self.leaf(int(8.3 * w), int(3.3 * h), int(0.3 * w), int(0.7 * h), 190)

        self.leaf(int(10.3 * w), int(1.65 * h), int(0.3 * w), int(0.7 * h), 190)
        self.leaf(int(9.5 * w), int(1.7 * h), int(0.3 * w), int(0.7 * h), 190)
        self.leaf(int(8.9 * w), int(1.75 * h), int(0.3 * w), int(0.7 * h), 190)
        self.leaf(int(8.3 * w), int(1.9 * h), int(0.3 * w), int(0.7 * h), 190)

    def draw_bamboo(self, x, y, w, h):
        polygon(self.sc, green, [[x, y - h], [x + w, y - h], [x + w, y], [x, y]])
        polygon(self.sc, green, [[x, int(y - 1.1 * h)], [x, int(y - 1.975 * h)],
                            [x + w, int(y - 1.975 * h)], [x + w, y - 1.1 * h]])
        polygon(self.sc, green, [[int(x + w / 2), int(y - 2 * h)],
                            [int(x + w), int(y - 2.9 * h)],
                            [int(x + w / 2), int(y - 3 * h)],
                            [int(x), int(y - 2.1 * h)]])
        polygon(self.sc, green, [[int(x + w), int(y - 3.05 * h)],
                            [int(x + 3 * w / 2), int(y - 3.95 * h)],
                            [int(x + w), int(y - 4.05 * h)],
                            [int(x + w / 2), int(y - 3.15 * h)]])

        self.branches(w, h)
        self.leaves(w, h)

# Класс управляет отрисовкой всего приложения.
class Manager:
    # Установка разрешения экрана и закрашивание заднего фона.
    def start(self, width, heigth):
        pygame.init()
        self.sc = pygame.display.set_mode((width, heigth))
        self.sc.fill(peach)

    # Отрисовка панды.
    def draw_panda(self, x, y, w, h):
        panda = PandaDrawer(self.sc)
        panda.draw_panda(x, y, w, h)

    # Отрисовка бамбукового дерева.
    def draw_bamboo(self, x, y, w, h):
        bamboo = BambooDrawer(self.sc)
        bamboo.draw_bamboo(x, y, w, h)

    # Закрытие программы.
    def close(self):
        pygame.quit()

def main():

    manager = Manager()

    manager.start(1024, 640)

    manager.draw_panda(600, 200, 400, 200)
    manager.draw_panda(300,400, 100, 50)
    manager.draw_panda(500, 100, 100, 50)
    manager.draw_bamboo(200, 500, 30, 100)

    # Обновление монитора.
    pygame.display.update()
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                manager.close()
                return
main()
