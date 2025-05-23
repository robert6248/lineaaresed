import pygame

pygame.init()

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]

pind = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Maja")
pind.fill(lGreen)

def drawHouse(x, y, width, height, screen, color):
    points = [
        (x, y - (3/4.0) * height),
        (x, y),
        (x + width, y),
        (x + width, y - (3/4.0) * height),
        (x + width / 2.0, y - height),
    ]
    pygame.draw.polygon(screen, color, points, 0)

def drawDoor(x, y, width, height, screen, color):
    door_width = width // 4  
    door_height = height // 2
    door_x = x + (width // 2) - (door_width // 2) 
    door_y = y + height - door_height 
    pygame.draw.rect(screen, color, (door_x, door_y, door_width, door_height))

def drawWindow(x, y, width, height, screen, color):
    window_size = width // 5 
    window_x = x + (width // 4) - (window_size // 2) 
    window_y = y + (height // 3) - (window_size // 2)  
    pygame.draw.rect(screen, color, (window_x, window_y, window_size, window_size))

def drawChimney(x, y, width, height, screen, color):
    chimney_width = 50  
    chimney_height = 150 
    chimney_x = x + (width // 2) - (chimney_width // 2)  
    chimney_y = y - height - chimney_height  
    pygame.draw.rect(screen, color, (chimney_x, chimney_y, chimney_width, chimney_height))

drawHouse(100, 300, 200, 200, pind, red)
drawDoor(100, 300, 200, 200, pind, blue)
drawWindow(100, 300, 200, 200, pind, pink)
drawChimney(100, 300, 200, 200, pind, green)

pygame.display.flip()


pygame.time.wait(50000)

pygame.quit()
