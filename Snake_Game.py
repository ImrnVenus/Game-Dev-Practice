import pygame
import random
#initialize pygame
pygame.init()
#define height and set up screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
#initialize a clock for fps
clock = pygame.time.Clock()
#background color is black
backgroundColor = (0,0,0)
#creating a font to track points
font = pygame.font.SysFont(None,30)
points = 0
screen.fill(backgroundColor)
#setting the snake and fruit initial position
Snake = [[width//2,height//2],[(width//2)-1,height//2]]
running = True
fruit = [width//4,height//4]
#starting direction
direction = (-10,0)
#game loop
while running:
    #updates the screen so that only the snakes current position is rendered
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #changes directions based on key and won't allow you to go opposite direction
            if event.key == pygame.K_w and direction !=(0,10):
                direction = (0,-10)
            if event.key == pygame.K_a and direction !=(10,0):
                direction = (-10,0)
            if event.key == pygame.K_s and direction !=(0,-10):
                direction = (0,10)
            if event.key == pygame.K_d and direction !=(-10,0):
                direction = (10,0)
    #creates a new head and pops from the tail if a fruit isn't consumed to make it look like it's moving
    newHead = [Snake[0][0]+direction[0],Snake[0][1]+direction[1]]
    Snake.insert(0,newHead)
    if Snake[0] == fruit:
        fruit = [random.randrange(0, width, 10),random.randrange(0, height, 10)]
        points+=1
    else:
        Snake.pop()
    #checks if snake runs into itself
    if Snake[0] in Snake[1:]:
        running = False
    #checks if snake goes off screen
    if Snake[0][0]>=width or Snake[0][0]<0 or Snake[0][1]>=height or Snake[0][1]<0:
        running = False
    #draws fruit
    pygame.draw.rect(screen,(255,0,0),(fruit[0],fruit[1],10,10))
    #draws each segment of snake
    for x in Snake:
        pygame.draw.rect(screen,(0,255,0),(x[0],x[1],10,10))
    #writes score to screen
    score = font.render(f"score: {points}",True,(255,255,255))
    screen.blit(score,(10,10))
    #update screen
    pygame.display.update()
    #sets up fps
    clock.tick(20)

pygame.quit()
