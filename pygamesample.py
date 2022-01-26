import pgzrun
import random
import math

WIDTH = 800
HEIGHT = 600

circleX = 0
circleY = 0
starlist = []


class Star:
    def __init__(self):
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.speed = 1
        self.angle = random.uniform(0,math.pi*2)
        self.size = 0.5

    def move(self):
        self.x = self.x + math.cos(self.angle) * self.speed
        self.y = self.y + math.sin(self.angle) * self.speed
        self.speed = self.speed + 0.1
        self.size = self.size * 1.025
        if self.x < 0 or self.x > WIDTH:
            starlist.remove(self)
        elif self.y < 0 or self.y > HEIGHT:
            starlist.remove(self)
    
    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.size, 'white')
        

def update():
    global starlist
    starlist.append(Star())
    for star in starlist:
        star.move()


def draw():
    screen.clear()
    for star in starlist:
        star.draw()



pgzrun.go()