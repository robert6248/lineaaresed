import pygame
import sys
import random
pygame.init()

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
black = [0, 0, 0]
white = [255, 255, 255]
grey = [170, 170, 170]
brown = [130, 60, 0]


pind = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Maja")
pind.fill(brown)

def draw_house(x, y, width, height, screen, color):
    #дом
    points = [(x, y - ((3/4.0) * height)), (x, y), (x + width, y), (x + width, y - (3/4.0) * height),
              (x, y - ((3/4.0) * height)), (x + width / 2.0, y - height), (x + width, y - (3/4.0) * height)]
    line_thickness = 3
    pygame.draw.lines(screen, color, False, points, line_thickness)

def draw_door(x, y, width, height, screen):
    #дверь
    pygame.draw.rect(screen, black, [x, y, width, height])

def draw_window(x, y, width, height, screen):
    #окно
    pygame.draw.rect(screen, white, [x, y, width, height])

def draw_chimney(x, y, width, height, screen):
    #дымоход
    pygame.draw.rect(screen, grey, [x, y, width, height])

def main():
    draw_house(100, 400, 300, 400, pind, red)


    door_width = 80
    door_height = 120
    door_x = 100 + (300 // 2) - (door_width // 2)
    door_y = 400 - door_height
    draw_door(door_x, door_y, door_width, door_height, pind)


    window_width = 50
    window_height = 65
    window_x = door_x + door_width + 10
    window_y = door_y + (door_height // 6)
    draw_window(window_x, window_y, window_width, window_height, pind)


    chimney_width = 40
    chimney_height = 80
    chimney_x = 10 + (300 // 2) - (chimney_width // 2)
    chimney_y = 390 - (3 / 4.0) * 400 - chimney_height
    draw_chimney(chimney_x, chimney_y, chimney_width, chimney_height, pind)

    pygame.display.flip()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

    pygame.quit()


main()
