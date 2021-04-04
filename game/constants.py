import pygame
import os
pygame.font.init()
pygame.mixer.init()


TITLE = pygame.display.set_caption("Pio Pio Game")
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
LIGHTGREY = (192, 192, 192)
DARKGREY = (128, 128, 128)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)
VEL = 5
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
BULLET_VEL = 7
MAX_BULLETS = 10

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

RED_HEALTH = 10
YELLOW_HEALTH = 10

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
WINNING_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'tada.mp3'))