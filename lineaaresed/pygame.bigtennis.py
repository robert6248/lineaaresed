import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Теннис 2 игрока")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 15
PADDLE_SPEED = 6
BALL_SPEED_X = 5
BALL_SPEED_Y = 3

# Фон
BG_IMG = pygame.image.load("pnga.jpg")
BG_IMG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 50)

def draw(paddle1, paddle2, ball, score1, score2):
    WIN.blit(BG_IMG, (0, 0))
    pygame.draw.rect(WIN, WHITE, paddle1)
    pygame.draw.rect(WIN, WHITE, paddle2)
    pygame.draw.circle(WIN, GREEN, (ball.x, ball.y), BALL_RADIUS)
    score_text = font.render(f"{score1} : {score2}", True, WHITE)
    WIN.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))
    pygame.display.flip()

def main():
    paddle1 = pygame.Rect(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH//2 - BALL_RADIUS, HEIGHT//2 - BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)

    ball_speed_x = random.choice([-BALL_SPEED_X, BALL_SPEED_X])
    ball_speed_y = random.choice([-BALL_SPEED_Y, BALL_SPEED_Y])

    score1, score2 = 0, 0
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        # Управление левой ракеткой (W/S)
        if keys[pygame.K_w] and paddle1.top > 0:
            paddle1.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
            paddle1.y += PADDLE_SPEED
        # Управление правой ракеткой (стрелки)
        if keys[pygame.K_UP] and paddle2.top > 0:
            paddle2.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
            paddle2.y += PADDLE_SPEED

        # Движение мяча
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Отскок от верхнего и нижнего краёв
        if ball.top <= 0 or ball.bottom >= HEIGHT: 
            ball_speed_y = -ball_speed_y

        # Столкновение с ракетками
        if ball.colliderect(paddle1) and ball_speed_x < 0:
            ball_speed_x = -ball_speed_x
        if ball.colliderect(paddle2) and ball_speed_x > 0:
            ball_speed_x = -ball_speed_x

        # Голы и подсчёт очков
        if ball.left <= 0:
            score2 += 1
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_speed_x = BALL_SPEED_X
            ball_speed_y = random.choice([-BALL_SPEED_Y, BALL_SPEED_Y])

        if ball.right >= WIDTH:
            score1 += 1
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_speed_x = -BALL_SPEED_X
            ball_speed_y = random.choice([-BALL_SPEED_Y, BALL_SPEED_Y])

        draw(paddle1, paddle2, ball, score1, score2)

if __name__ == "__main__":
    main()
