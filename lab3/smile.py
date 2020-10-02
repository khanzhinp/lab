import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))
#white display
rect(screen, (255, 255, 255), (0, 0, 400, 400))
#yellow face
circle(screen, (255, 255, 0), (200, 175), 100)

#left eye
circle(screen, (255, 0, 0), (150, 140), 20)
#left pupil
circle(screen, (0, 0, 0), (150, 140), 6)
#right eye
circle(screen, (255, 0, 0), (245, 140), 15)
#right pupil
circle(screen, (0, 0, 0), (245, 140), 6)

#mouth
rect(screen, (0, 0, 0), (150, 200, 100, 10))
#left eyebrow
polygon(screen, (0, 0, 0), [(180,135), (183,125),(113,115), (110,125)])
#right eyebrow
polygon(screen, (0, 0, 0), [(215,140), (275,120),(273,110), (213,130)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()