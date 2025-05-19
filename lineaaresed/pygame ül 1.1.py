import pygame
import sys
import math

pygame.init()

LAIUS, KÕRGUS = 800, 600
ekraan = pygame.display.set_mode((LAIUS, KÕRGUS))
pygame.display.set_caption("windows")
font = pygame.font.SysFont("arial", 50, bold=True)

SININE = (0, 0, 200)
ROHELINE = (0, 255, 0)
KOLLANE = (255, 255, 0)
HALL = (100, 100, 100)
ROOSA = (255, 0, 255)
TUMEROHELINE = (0, 100, 0)
VALGE = (255, 255, 255)

try:
    bee_image = pygame.image.load("pilt.png")
    bee_image = pygame.transform.scale(bee_image, (200, 220))
    bee_loaded = True
except:
    print("Viga pildi laadimisel:", )
    bee_loaded = False

def joonista_päike():
    keskpunkt = (0, 0)
    raadius = 150
    pygame.draw.circle(ekraan, KOLLANE, keskpunkt, raadius)
    for nurk in range(0, 90, 10):
        x = 0 + 200 * math.cos(math.radians(nurk))
        y = 0 + 200 * math.sin(math.radians(nurk))
        pygame.draw.line(ekraan, KOLLANE, keskpunkt, (x, y), 3)

def joonista_pilv():
    pygame.draw.circle(ekraan, HALL, (600, 100), 40)
    pygame.draw.circle(ekraan, HALL, (640, 80), 50)
    pygame.draw.circle(ekraan, HALL, (690, 100), 40)
    pygame.draw.circle(ekraan, HALL, (660, 120), 35)


def joonista_lill():
    keskpunkt = (400, 350)
    pygame.draw.rect(ekraan, TUMEROHELINE, (keskpunkt[0] - 8, keskpunkt[1], 16, 250))
    pygame.draw.circle(ekraan, ROOSA, keskpunkt, 60)

def joonista_tekst():
    tekst = font.render("Tere tulemast!", True, VALGE)
    ekraan.blit(tekst, (270, 30))

while True:
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ekraan.fill(SININE)
    pygame.draw.rect(ekraan, ROHELINE, (0, KÕRGUS // 2, LAIUS, KÕRGUS // 2))

    joonista_päike()
    joonista_lill()
    joonista_tekst()
    joonista_pilv()

    if bee_loaded:
        ekraan.blit(bee_image, (340, 100))
    else:
        pygame.draw.rect(ekraan, VALGE, (340, 100, 100, 100))

    pygame.display.flip()
