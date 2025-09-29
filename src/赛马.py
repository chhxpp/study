from pathlib import Path
import pygame
from mod.class_animal import Horse,Lala

filenames = ['草原.bmp', 'h1.png', 'h2.png', 'h3.png', 'h4.png', 'lala1.png', 'lala2.png', 'lala3.png', 'lala4.png']
imgfile = [Path(__file__).parent.parent / 'res' / 'img' / name for name in filenames]
草原, h1, h2, h3, h4, lala1, lala2, lala3, lala4 = imgfile

pygame.init()
screen=pygame.display.set_mode((850,600))
img_bg=pygame.image.load(草原)

h_list=[
        Horse('海洋饼干',5,h1,100),
        Horse('影疾',5,h2,150),
        Horse('黑美人',5,h3,200),
        Horse('赤兔',5,h4,260),
        Lala(lala1,100,480,True),
        Lala(lala2,300,480,),
        Lala(lala3,500,480,True),
        Lala(lala4,700,480,)
        ]

while True:
    screen.blit(img_bg,(0,0))
    for h in h_list:
        screen.blit(h.get_image(), h.get_location())
        h.run()
    pygame.display.update()
    pygame.time.delay(150)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()