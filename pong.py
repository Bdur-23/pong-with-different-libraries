import pygame
import random
import numpy as np

class PongAI:
    def __init__(self, observation_space, action_space):
        self.observation_space = observation_space
        self.action_space = action_space
        
    def get_action(self, obs):
        # Get the position of the ball and the paddle
        ball_x, ball_y = obs[0]
        paddle_y = obs[1][1]
        
        # Determine whether the ball is moving towards the paddle
        if ball_x < 0:
            ball_dx, ball_dy = obs[2]
            towards_paddle = ball_dx < 0
        else:
            towards_paddle = False
        
        # Move the paddle towards the ball
        if towards_paddle:
            if paddle_y < ball_y:
                action = 2 # move paddle up
            elif paddle_y > ball_y:
                action = 3 # move paddle down
            else:
                action = 0 # do nothing
        else:
            action = np.random.choice(self.action_space.n)
        
        return action

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong')

# Set up the clock
clock = pygame.time.Clock()

# Set up game objects
paddle_width = 10
paddle_height = 80
paddle_speed = 5

paddle_left = pygame.Rect(50, HEIGHT/2 - paddle_height/2, paddle_width, paddle_height)
paddle_right = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT/2 - paddle_height/2, paddle_width, paddle_height)

ball = pygame.Rect(WIDTH/2, HEIGHT/2, 20, 20)
ball_speed = [5, 5]

score_left = 0
score_right = 0

# Set up fonts
font = pygame.font.Font(None, 50)

# Set up AI
def move_ai_paddle():
    if ball.top < paddle_left.top + paddle_height/2:
        paddle_left.top -= paddle_speed
    if ball.bottom > paddle_left.bottom + paddle_height/2:
        paddle_left.top += paddle_speed

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    # Move paddles with arrow keys and AI
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle_right.top -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle_right.top += paddle_speed
    move_ai_paddle()

    # Update ball position
    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    # Check for collisions with walls
    if ball.left < 0:
        ball.left = 0
        ball_speed[0] *= -1
        score_right += 1
    if ball.right > WIDTH:
        ball.right = WIDTH
        ball_speed[0] *= -1
        score_left += 1
    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_speed[1] *= -1

    # Check for collisions with paddles
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        ball_speed[0] *= -1

    # Draw objects on screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle_left)
    pygame.draw.rect(screen, (255, 255, 255), paddle_right)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    score_text = font.render(str(score_left) + ' - ' + str(score_right), True, (255, 255, 255))
    screen.blit(score_text, (WIDTH/2 - score_text.get_width()/2, 20))
    pygame.display.flip()

    # Set up next frame
    clock.tick(60)














"""
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong')

# Set up the clock
clock = pygame.time.Clock()

# Set up game objects
paddle_width = 10
paddle_height = 80
paddle_speed = 5

paddle_left = pygame.Rect(50, HEIGHT/2 - paddle_height/2, paddle_width, paddle_height)
paddle_right = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT/2 - paddle_height/2, paddle_width, paddle_height)

ball = pygame.Rect(WIDTH/2, HEIGHT/2, 20, 20)
ball_speed = [5, 5]

score_left = 0
score_right = 0

# Set up fonts
font = pygame.font.Font(None, 50)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    # Move paddles with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle_right.top -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle_right.top += paddle_speed
    if keys[pygame.K_w]:
        paddle_left.top -= paddle_speed
    if keys[pygame.K_s]:
        paddle_left.top += paddle_speed

    # Update ball position
    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    # Check for collisions with walls
    if ball.left < 0:
        ball.left = 0
        ball_speed[0] *= -1
        score_right += 1
    if ball.right > WIDTH:
        ball.right = WIDTH
        ball_speed[0] *= -1
        score_left += 1
    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_speed[1] *= -1

    # Check for collisions with paddles
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        ball_speed[0] *= -1

    # Draw objects on screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle_left)
    pygame.draw.rect(screen, (255, 255, 255), paddle_right)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    score_text = font.render(str(score_left) + ' - ' + str(score_right), True, (255, 255, 255))
    screen.blit(score_text, (WIDTH/2 - score_text.get_width()/2, 20))
    pygame.display.flip()

    # Set up next frame
    clock.tick(60)
"""

