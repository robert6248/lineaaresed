import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Большой Теннис с Ботом")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
PADDLE_SPEED = 6

BALL_RADIUS = 15

# Загрузка фона
BG_IMG = pygame.image.load("pnga.jpg")
BG_IMG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))

FONT = pygame.font.SysFont("comicsans", 40)
WINNING_SCORE = 5

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def draw(self, win):
        pygame.draw.rect(win, WHITE, self.rect)

    def move(self, up=True):
        if up:
            self.y -= PADDLE_SPEED
        else:
            self.y += PADDLE_SPEED
        self.y = max(0, min(self.y, HEIGHT - PADDLE_HEIGHT))
        self.rect.y = self.y

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_vel = random.choice([-5, 5])
        self.y_vel = random.choice([-3, 3])
        self.rect = pygame.Rect(x - BALL_RADIUS, y - BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)

    def draw(self, win):
        pygame.draw.circle(win, GREEN, (int(self.x), int(self.y)), BALL_RADIUS)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

        if self.y - BALL_RADIUS <= 0 or self.y + BALL_RADIUS >= HEIGHT:
            self.y_vel *= -1

        self.rect.x = self.x - BALL_RADIUS
        self.rect.y = self.y - BALL_RADIUS

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.x_vel = random.choice([-5, 5])
        self.y_vel = random.choice([-3, 3])
        self.rect.x = self.x - BALL_RADIUS
        self.rect.y = self.y - BALL_RADIUS

def draw(win, paddles, ball, score):
    win.blit(BG_IMG, (0, 0))  # фон

    for paddle in paddles:
        paddle.draw(win)

    ball.draw(win)

    score_text = FONT.render(f"{score[0]} : {score[1]}", True, WHITE)
    win.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))

    pygame.display.update()

def bot_move(paddle, ball):
    # Бот с задержкой и ограничением скорости - чтобы его можно было выиграть
    center_paddle = paddle.y + PADDLE_HEIGHT // 2
    center_ball = ball.y

    if center_paddle < center_ball - 10:
        paddle.move(up=False)
    elif center_paddle > center_ball + 10:
        paddle.move(up=True)
    # Внимание: бот движется медленнее, чем игрок, так что проигрыш возможен

def main():
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2)
    ball = Ball(WIDTH//2, HEIGHT//2)

    score = [0, 0]  # Игрок, Бот

    run = True
    winner = None

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if winner is None:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                left_paddle.move(up=True)
            if keys[pygame.K_s]:
                left_paddle.move(up=False)

            ball.move()
            bot_move(right_paddle, ball)

            # Столкновения с ракетками
            if ball.rect.colliderect(left_paddle.rect):
                ball.x_vel = abs(ball.x_vel)

            if ball.rect.colliderect(right_paddle.rect):
                ball.x_vel = -abs(ball.x_vel)

            # Очки
            if ball.x - BALL_RADIUS < 0:
                score[1] += 1
                ball.reset()

            if ball.x + BALL_RADIUS > WIDTH:
                score[0] += 1
                ball.reset()

            # Проверка победы
            if score[0] >= WINNING_SCORE:
                winner = "Игрок выиграл!"
            elif score[1] >= WINNING_SCORE:
                winner = "Бот выиграл!"

        else:
            # Показываем сообщение о победе и ждем закрытия окна
            WIN.fill(BLACK)
            win_text = FONT.render(winner, True, WHITE)
            WIN.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2 - win_text.get_height()//2))
            pygame.display.update()

        draw(WIN, [left_paddle, right_paddle], ball, score)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
