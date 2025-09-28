import random
import pygame

class Animal:
    def __init__(self, n, s):
        self.name = n
        self.speed = s

class Horse(Animal):
    def __init__(self, n, s, img_file, y):
        super().__init__(n, s)
        self.__image = pygame.image.load(img_file)
        self.__x = 0
        self.__y = y

    def run(self):
        self.__x += round(self.speed * random.random()*10)

    def get_image(self):
        return self.__image

    def get_location(self):
        return (self.__x, self.__y)

class Lala(Animal):
    def __init__(self, img_file, x,y,up=True):
        super().__init__(None, None)
        self.__image = pygame.image.load(img_file)
        self.__x=x
        self.__y=y
        self.__up=up

    def run(self):
        if self.__up:
            self.__y-=30
        else:
            self.__y+=30
        self.__up=not self.__up

    def get_image(self):
        return self.__image

    def get_location(self):
        return (self.__x, self.__y)

class Horse2:
    def __init__(self,n,s,img_file,y):
        self.name=n
        self.speed=s
        self.__image=pygame.image.load(img_file)
        self.__x=0
        self.__y=y

    def run(self):
        self.__x += round(self.speed * random.random()*10)

    def get_image(self):
        return self.__image

    def get_location(self):
        return (self.__x,self.__y)

