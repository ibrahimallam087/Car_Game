import pygame
from utils import scale_image, blit_rotate_centre
import math
import time

GRASS = scale_image(pygame.image.load("D:/Programming/projects/Car_Game/imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("D:/Programming/projects/Car_Game/imgs/track.png"), 0.6)
TRACK_BORDER = scale_image(pygame.image.load("D:/Programming/projects/Car_Game/imgs/track-border.png"), 0.6)
RED_CAR = scale_image(pygame.image.load("D:/Programming/projects/Car_Game/imgs/red-car.png"), 0.6)
GREEN_CAR = pygame.image.load("D:/Programming/projects/Car_Game/imgs/green-car.png")
FINISH = pygame.image.load("D:/Programming/projects/Car_Game/imgs/finish.png")
width, height = TRACK.get_width(), TRACK.get_height()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("CAR_RACING")
FPS = 60;
clock = pygame.time.Clock()

run = True


class AbstractCar:
    def __init__(self, max_vel, rotational_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.rotational_vel = rotational_vel
        self.vel = 0
        self.angle = 0
        self.x, self.y = self.START_POSITION

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotational_vel
        elif right:
            self.angle -= self.rotational_vel

    def draw(self, win):
        blit_rotate_centre(win, self.img, (self.x, self.y), self.angle)


class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POSITION = (180, 200)


def Draw_(win_, images_):
    for image, pos in images_:
        win_.blit(image, pos)
    player_car.draw(win_)
    pygame.display.update()


images = [(GRASS, (0, 0)), (TRACK, (0, 0)), (FINISH, (0, 0))]
player_car = PlayerCar(4, 4)

while run:
    clock.tick(FPS)
    Draw_(win, images)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
