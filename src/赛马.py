import pygame
from animal_class import Horse,Lala

pygame.init()
screen=pygame.display.set_mode((850,600))
img_bg=pygame.image.load('草原.bmp')

h_list=[
        Horse('海洋饼干',5,'h1.png',100),
        Horse('影疾',5,'h2.png',150),
        Horse('黑美人',5,'h3.png',200),
        Horse('赤兔',5,'h4.png',260),
        Lala('lala1.png',100,480,True),
        Lala('lala2.png',300,480,),
        Lala('lala3.png',500,480,True),
        Lala('lala4.png',700,480,)
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
