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
        if keys_pressed[K_s] and self.rect.y<435:
            self.rect.y+=self.speed
        if keys_pressed[K_w]and self.rect.y >0:
            self.rect.y-=self.speed
    def updater(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y<435:
            self.rect.y+=self.speed
        if keys_pressed[K_UP]and self.rect.y >0:
            self.rect.y-=self.speed
FPS = 60

racket1= Player('racka1.png',0,185,100,160,7)
racket2= Player('racka2.png',600,185,100,160,7)
ball = GameSprite('myach.png',285,185,50,50,5)
#создай окно игры
window = display.set_mode((700,500))
display.set_caption('Ping-pong')
background = transform.scale(image.load('mesto.jpg'),(700,500))
collides = 0
game = True
clock = time.Clock()
score = 0
keys_pressed = key.get_pressed()
finish = False
speed_x=5
speed_y=5
font.init()
font1 = font.Font(None,55)
lose1 = font1.render('PLAYER 1 LOSE!',True,(180,0,0))
lose2 = font1.render('PLAYER 2 LOSE!',True,(180,0,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    if finish!=True:
        window.blit(background,(0,0))
        racket1.reset()
        racket2.reset()
        racket1.updatel()
        racket2.updater()
        ball.reset()
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 50:
            speed_y *= -1
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x*=-1
        if ball.rect.x == 0:
            window.blit(lose1, (200,200))
            finish = True
        if ball.rect.x == 770:
            window.blit(lose2, (200,200))
            finish = True
    clock.tick(FPS)
    display.update()