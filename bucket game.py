import pygame 
import random 

font_initiol = pygame.font.init()
initiol = pygame.display.init()
screen = pygame.display.set_mode((1000,600))
caption = pygame.display.set_caption("my game")
background = pygame.transform.scale(pygame.image.load("css/abstract-simple-grass-texture-seamless-pattern-vector-43074878 (1).png"),(1000,600))
block = pygame.transform.scale(pygame.image.load("css/boxes.jpeg"),(80,80))
ground =pygame.transform.rotate(pygame.transform.scale(pygame.image.load("css/boxes_pick-removebg.png"),(775,1400)),90)
bucket = pygame.transform.scale(pygame.image.load("css/bucket-removebg-preview.png"),(200,100))
block_y= 0
score = 0
score_board = pygame.font.SysFont("comicsans",40)
run = True 
clock = pygame.time.Clock()
block_x = 20
box2_x = 400
over_display = pygame.font.SysFont("comicsans",40)
over_render = over_display.render("PRESS SPACE TO RETRY",True,(44, 4, 179))
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
    screen.blit(background,(0,0))
    box = pygame.draw.rect(screen,(255,0,0),(block_x,block_y,80,80))
    screen.blit(block,(block_x,block_y))
    block_y+= 2
    box2 = pygame.draw.rect(screen,(255,0,0),(box2_x+55,500,90,70))
    screen.blit(bucket,(box2_x,490))
    score_render = score_board.render(f"SCORE:{score}",True,(44, 4, 179))
    screen.blit(score_render,(20,20))
    screen.blit(ground,(0,50))
    keys = pygame.key.get_pressed()
    if block_y>500:
       screen.blit(over_render,(250,250))

    if keys[pygame.K_RIGHT]:box2_x+= 7
    if keys[pygame.K_LEFT]:box2_x-= 7
    if box2_x<0:box2_x = 0
    if box2_x>860:box2_x = 860
    if keys[pygame.K_SPACE]:
        block_y = 0
        score = 0

    if box.colliderect(box2):
        score+=1
        block_y = 0
        rand = random.randint(1,950)
        block_x = rand

    pygame.display.update()
    clock.tick(100)