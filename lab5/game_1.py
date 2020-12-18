import pygame
from random import randint
import time
import sys
import re


with open('records_new.txt', 'r') as file:
    tr = file.read()
    tr = re.split(r'\n', tr)
    d = open('records.txt', 'w')
    for o in range(5):
        d.write(f'{tr[o]}\n')
    d.close()

USERNAME = 'Player'

size = width, height = 1920, 1080
score = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

global r1, r2, r3, r4, r5, r6
global circle1_x, circle2_x, circle3_x, circle4_x, circle5_x
global circle1_y, circle2_y, circle3_y, circle4_y, circle5_y


def main():
    pygame.init()

    game_over = False

    global score, r1, r2, r3, r4, r5, r6
    global circle1_x, circle2_x, circle3_x, circle4_x, circle5_x
    global circle1_y, circle2_y, circle3_y, circle4_y, circle5_y

    screen = pygame.display.set_mode(size)

    # Задание параметров кругов
    r1 = randint(30, 60)
    circle1_x = randint(r1, width-r1)
    circle1_y = randint(r1, height-r1)
    a1 = randint(1, 5)
    b1 = randint(1, 5)
    r2 = randint(30, 60)
    circle2_x = randint(r2, width-r2)
    circle2_y = randint(r2, height-r2)
    a2 = randint(1, 5)
    b2 = randint(1, 5)
    r3 = randint(30, 60)
    circle3_x = randint(r3, width-r3)
    circle3_y = randint(r3, height-r3)
    a3 = randint(1, 5)
    b3 = randint(1, 5)
    r4 = randint(30, 60)
    circle4_x = randint(r4, width-r4)
    circle4_y = randint(r4, height-r4)
    a4 = randint(1, 5)
    b4 = randint(1, 5)

    # Следующий объект - элипс с меньшим размером и большей скоростью
    r5 = randint(10, 20)
    r6 = randint(20, 40)
    circle5_x = randint(r5, width-r5)
    circle5_y = randint(r5, height-r5)
    a5 = randint(10, 15)
    b5 = randint(10, 15)

    # Задание вектора скорости
    dx = 1
    dy = 1
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill(BLACK)
        circle1_x += a1 * dx
        circle1_y += b1 * dy
        circle2_x -= a2 * dx
        circle2_y -= b2 * dy
        circle3_x += a3 * dx
        circle3_y -= b3 * dy
        circle4_x -= a4 * dx
        circle4_y += b4 * dy
        circle5_x += a5 * dx
        circle5_y += b5 * dy

        # Изменение вектора скорости при взаимодействии со стенкой
        if circle1_y > height-r1 or circle1_y < r1:
            b1 *= -1
        if circle1_x > width - r1 or circle1_x < r1:
            a1 *= -1
        if circle2_y > height-r2 or circle2_y < r2:
            b2 *= -1
        if circle2_x > width - r2 or circle2_x < r2:
            a2 *= -1
        if circle3_y > height-r3 or circle3_y < r3:
            b3 *= -1
        if circle3_x > width - r3 or circle3_x < r3:
            a3 *= -1
        if circle4_y > height-r4 or circle4_y < r4:
            b4 *= -1
        if circle4_x > width - r4 or circle4_x < r4:
            a4 *= -1
        if circle5_y > height - r6 or circle5_y < r6:
            b5 *= -1
        if circle5_x > width - r5 or circle5_x < r5:
            a5 *= -1

        pygame.draw.circle(screen, COLORS[1], (circle1_x, circle1_y), r1)
        pygame.draw.circle(screen, COLORS[2], (circle2_x, circle2_y), r2)
        pygame.draw.circle(screen, COLORS[3], (circle3_x, circle3_y), r3)
        pygame.draw.circle(screen, COLORS[4], (circle4_x, circle4_y), r4)
        pygame.draw.ellipse(screen, COLORS[5], (circle5_x, circle5_y, r5, r6))
        pygame.display.flip()
        pygame.time.wait(10)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(event)
# Составление лидерборда
        if (time.time() - start_time) >= 5:
            with open("records.txt", "r") as file:
                get = file.read()
                get_2 = re.split(r'\n', get)
                get_1 = re.findall(r'\d{1,3}', get)
                print(get_1)
            for i in range(len(get_1)):
                if score >= int(get_1[i]):
                    for j in range(4, i, -1):
                        get_2[j] = get_2[j-1]
                    get_2[i] = f'{USERNAME} : {score}'
                print(get_2)
                f = open('records_new.txt', 'w')
                for m in range(5):
                    f.write(f'{get_2[m]}\n')
                f.close()
                sys.exit()


# Проверка попаданий кликами
def click(eve):
    global score, r1, r2, r3, r4, r6
    global circle1_x, circle2_x, circle3_x, circle4_x, circle5_x
    global circle1_y, circle2_y, circle3_y, circle4_y, circle5_y
    xt, yt = eve.pos
    if ((xt-circle1_x)**2 + (yt-circle1_y)**2)**(1/2) <= r1:
        score += 1
    if ((xt-circle2_x)**2 + (yt-circle2_y)**2)**(1/2) <= r2:
        score += 1
    if ((xt-circle3_x)**2 + (yt-circle3_y)**2)**(1/2) <= r3:
        score += 1
    if ((xt-circle4_x)**2 + (yt-circle4_y)**2)**(1/2) <= r4:
        score += 1
    if ((xt-circle5_x)**2 + (yt-circle5_y)**2)**(1/2) <= r6:
        score += 3



if __name__ == '__main__':
    start_time = time.time()
    main()
    pygame.quit()
