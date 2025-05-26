import pygame
import sys
import random

pygame.init()

# Цвета
white = [255, 255, 255]
flower_color = [100, 255, 100]
flower_hit_color = [255, 100, 100]

WIDTH, HEIGHT = 800, 600
pind = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Aken")

# Загружаем и масштабируем изображение пчелы
bee_image = pygame.image.load("pilt.png") 
bee_image = pygame.transform.scale(bee_image, (50, 50))  # сделал поменьше

# Пчела стартует в случайном углу
corners = [(0, 0), (WIDTH - 50, 0), (0, HEIGHT - 50), (WIDTH - 50, HEIGHT - 50)]
bee_x, bee_y = random.choice(corners)

# Функции движения (по 3 вариантам)
def move_counterclockwise(x, y):
    return x - 3, y - 3

def move_clockwise(x, y):
    return x + 3, y + 3

def move_diagonal(x, y):
    return x - 3, y + 3

moves = [move_counterclockwise, move_clockwise, move_diagonal]
current_move = random.choice(moves)

# Создаем 5 цветов (каждый - словарь с координатами и состоянием)
flowers = []
for _ in range(5):
    fx = random.randint(50, WIDTH - 50)
    fy = random.randint(50, HEIGHT - 50)
    flowers.append({"x": fx, "y": fy, "color": flower_color.copy()})

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Двигаем пчелу
    bee_x, bee_y = current_move(bee_x, bee_y)

    # Проверяем границы и меняем направление
    if bee_x < 0:
        bee_x = 0
        current_move = random.choice(moves)
    if bee_x > WIDTH - 50:
        bee_x = WIDTH - 50
        current_move = random.choice(moves)
    if bee_y < 0:
        bee_y = 0
        current_move = random.choice(moves)
    if bee_y > HEIGHT - 50:
        bee_y = HEIGHT - 50
        current_move = random.choice(moves)

    pind.fill(white)

    # Прямоугольник пчелы для столкновения
    bee_rect = pygame.Rect(bee_x, bee_y, 50, 50)

    # Рисуем цветы и проверяем столкновения
    for flower in flowers:
        flower_rect = pygame.Rect(flower["x"] - 15, flower["y"] - 15, 30, 30)
        if bee_rect.colliderect(flower_rect):
            flower["color"] = flower_hit_color
        pygame.draw.circle(pind, flower["color"], (flower["x"], flower["y"]), 15)

    # Рисуем пчелу
    pind.blit(bee_image, (bee_x, bee_y))

    pygame.display.update()
    clock.tick(60)
