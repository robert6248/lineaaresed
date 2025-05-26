import pygame, random
pygame.init()


red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
lilla = [153, 255, 255]
pink = [255, 153, 255]
white = [255, 255, 255]

# Размеры экрана
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Surface")

clock = pygame.time.Clock()
posX, posY = 100, 100
speedX = 3
speedY = 3.4


player = pygame.Rect(posX, posY, 120, 120)
playerImage = pygame.image.load("dada.jpg")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])


enemies = []
enemyImage = pygame.image.load("pall.png")
enemyImage = pygame.transform.scale(enemyImage, [60, 73])

enemyCounter = 0
totalEnemies = 20
score = 0

gameOver = False
while not gameOver:
    clock.tick(60)

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True


    posX += speedX
    posY += speedY


    if posX + player.width >= screenX or posX <= 0:
        speedX = -speedX
    if posY + player.height >= screenY or posY <= 0:
        speedY = -speedY

    player = pygame.Rect(posX, posY, 120, 120)

    # Создание врагов
    if enemyCounter < totalEnemies:
        enemy = pygame.Rect(random.randint(0, screenX - 60), random.randint(0, screenY - 73), 60, 73)
        enemies.append(enemy)
        enemyCounter += 1

    # Проверка столкновений
    for enemy in enemies[:]:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            score += 1

    # Отрисовка
    screen.fill(blue)
    screen.blit(playerImage, player)

    for enemy in enemies:
        screen.blit(enemyImage, enemy)

    pygame.display.flip()

    # Победа
    if score >= 20:
        gameOver = True

pygame.quit()
