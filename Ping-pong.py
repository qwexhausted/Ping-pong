from random import randint
from pygame import *
from time import time as timer
import sys

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    
class Player(GameSprite):
    def updatel(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y >0:
            self.rect.y-=self.speed
        if keys_pressed[K_w]and self.rect.x<435:
            self.rect.y+=self.speed
    def updater(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y >0:
            self.rect.y-=self.speed
        if keys_pressed[K_UP]and self.rect.y<435:
            self.rect.y+=self.speed
FPS = 60

racketl= Player('racka.png',100,185,65,100,5)
racketr= Player('racka.png',600,185,65,100,5)
myach = GameSprite('myach.png',285,185,30,30,5)
#создай окно игры
window = display.set_mode((700,500))
display.set_caption('Ping-pong')
background = transform.scale(image.load('mesto.jpg'),(700,500))
collides = 0
game = True
clock = time.Clock()
score = 0
keys_pressed = key.get_pressed()



while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
   
    clock.tick(FPS)
    display.update()