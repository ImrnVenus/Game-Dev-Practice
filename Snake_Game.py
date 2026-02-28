import pygame
import random
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
backgroundColor = (0,0,0)
font = pygame.font.SysFont(None,30)
points = 0
screen.fill(backgroundColor)
Snake = [[width//2,height//2],[(width//2)-1,height//2]]
running = True
fruit = [width//4,height//4]
direction = (-10,0)
while running:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction !=(0,10):
                direction = (0,-10)
            if event.key == pygame.K_a and direction !=(10,0):
                direction = (-10,0)
            if event.key == pygame.K_s and direction !=(0,-10):
                direction = (0,10)
            if event.key == pygame.K_d and direction !=(-10,0):
                direction = (10,0)
    newHead = [Snake[0][0]+direction[0],Snake[0][1]+direction[1]]
    Snake.insert(0,newHead)
    if Snake[0] == fruit:
        fruit = [random.randrange(0, width, 10),random.randrange(0, height, 10)]
        points+=1
    else:
        Snake.pop()
    if Snake[0] in Snake[1:]:
        running = False
    if Snake[0][0]>=width or Snake[0][0]<0 or Snake[0][1]>=height or Snake[0][1]<0:
        running = False
    pygame.draw.rect(screen,(255,0,0),(fruit[0],fruit[1],10,10))
    for x in Snake:
        pygame.draw.rect(screen,(0,255,0),(x[0],x[1],10,10))
    score = font.render(f"score: {points}",True,(255,255,255))
    screen.blit(score,(10,10))
    pygame.display.update()
    clock.tick(20)