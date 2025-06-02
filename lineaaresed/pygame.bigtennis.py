import pygame
import random
import sys

# --- Initsialiseerimine ---
pygame.init()

# --- Ekraani seaded ---
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mäng: suur tennis ")

# --- värvid ---
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# --- Mängu konstandid ---
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 80
PADDLE_SPEED = 5
BALL_RADIUS = 17
BALL_SPEED = [5, 5]
WIN_SCORE = 5
FPS = 60

# --- Piltide üleslaadimine ---
bg_img = pygame.transform.scale(pygame.image.load("pnga.jpg"), (WIDTH, HEIGHT))
ball_img = pygame.transform.scale(pygame.image.load("mya4.png"), (BALL_RADIUS * 2, BALL_RADIUS * 2))
cup_img = pygame.transform.scale(pygame.image.load("kybok.png"), (60, 60))

# --- Mänguobjektid ---
p1 = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
p2 = pygame.Rect(WIDTH - 25, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)

# --- Olekumuutujad ---
score1 = 0
score2 = 0
ball_dx = random.choice([-BALL_SPEED[0], BALL_SPEED[0]])
ball_dy = random.choice([-BALL_SPEED[1], BALL_SPEED[1]])

# --- Font ja taimer ---
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

# --- Funktsioonid ---
def draw_game():
    WIN.blit(bg_img, (0, 0))
    pygame.draw.rect(WIN, WHITE, p1)
    pygame.draw.rect(WIN, WHITE, p2)
    WIN.blit(ball_img, ball.topleft)

    score_text = font.render(f"{score1} : {score2}", True, BLACK)
    WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))
    pygame.display.flip()

def reset_ball(direction):
    global ball_dx, ball_dy
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_dx = BALL_SPEED[0] * direction
    ball_dy = random.choice([-BALL_SPEED[1], BALL_SPEED[1]])

def show_winner(winner_name):
    WIN.blit(bg_img, (0, 0))
    text = font.render(f"{winner_name} sa oled võitja!", True, GREEN)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    cup_rect = cup_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
    WIN.blit(text, text_rect)
    WIN.blit(cup_img, cup_rect)
    pygame.display.flip()
    pygame.time.wait(4000)

# --- Mängu silmus ---
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Mängija juhtimine ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and p1.top > 0:
        p1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and p1.bottom < HEIGHT:
        p1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and p2.top > 0:
        p2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and p2.bottom < HEIGHT:
        p2.y += PADDLE_SPEED

    # --- Palli liikumine ---
    ball.x += ball_dx
    ball.y += ball_dy

    # --- Kokkupõrked ---
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy = -ball_dy

    if ball.colliderect(p1) and ball_dx < 0 or ball.colliderect(p2) and ball_dx > 0:
        ball_dx = -ball_dx

    # --- punktid ---
    if ball.left <= 0:
        score2 += 1
        reset_ball(direction=1)

    if ball.right >= WIDTH:
        score1 += 1
        reset_ball(direction=-1)

    draw_game()

    # --- Võitja kinnitamine ---
    if score1 == WIN_SCORE or score2 == WIN_SCORE:
        winner = "mängija 1" if score1 == WIN_SCORE else "mängija 2"
        show_winner(winner)
        running = False

pygame.quit()
sys.exit()
