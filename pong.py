#setup
import pygame
import random
import sys

Width, Height = 1280, 720
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Pong') 
running = True

#Players 
player1 = pygame.Rect(Width-110, Height/2-50, 10, 100)
player2 = pygame.Rect(110, Height/2-50, 10, 100)
player1_score, player2_score = 0, 0

#Ball
ball = pygame.Rect(Width/2-10, Height/2-10, 20, 20)
x_speed, y_speed = 1, 1

#Game Logic
if ball.y >= Height:
    y_speed = -1
if ball.y <= 0:
    y_speed = 1

if ball.x <= 0:
    player1_score += 1
    ball.center = (Width/2, Height/2)
    x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])

if ball.x >= Width:
    player2_score += 1
    ball.center = (Width/2, Height/2)
    x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])

if player1.x - ball.width <= ball.x <= player1.x and ball.y in range(player1.top-ball.width, player1.bottom+ball.width):
    x_speed = -1
if player2.x - ball.width <= ball.x <= player2.x and ball.y in range(player2.top-ball.width, player2.bottom+ball.width):
    x_speed = 1


#game loop
while running:
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_UP]:
        if player1.top > 0:
            player1.top -= 2

    if keys_pressed[pygame.K_DOWN]:
        if player1.bottom > Height:
            player1.bottom += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.x += x_speed * 2
    ball.y += y_speed * 2

    if player2.y < ball.y:
        player2.top += 1
    if player2.bottom > ball.y:
        player2.bottom -= 1

screen.fill("black")

#Color of the Paddles and Ball
pygame.draw.rect(screen, "white", player1)
pygame.draw.rect(screen, "white", player2)
pygame.draw.rect(screen, "white", ball)

#Updating the window
pygame.display.flip()
pygame.display.update()
clock = pygame.time.Clock()
clock.tick(60)

sys.exit()