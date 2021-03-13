''' coordinate chess practice  '''
import random
import pygame
def wait():
    ''' stores event and returns only if mouse is pressed '''
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()
    elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
        return
    else:
        wait()
green = (0, 255, 0)
blue = (0, 0, 128)
pygame.init()
surface = pygame.display.set_mode((1224, 776))
pygame.display.set_caption("Board")
image = pygame.image.load('board.jpg')
font = pygame.font.Font('freesansbold.ttf', 32)
while True:
    surface.fill(blue, (1024, 0, 200, 776))
    surface.blit(image, (0, 0))
    a = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    b = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    text = font.render('%c %d'%(a, b), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (1124, 388)
    surface.blit(text, textRect)
    pygame.display.update()
    wait()
    z = pygame.mouse.get_pos()
    (x, y) = (z[0], z[1])
    if (chr(65+x//128), (776-y)//97+1) != (a, b):
        text = font.render('No', True, green, blue)
        textRect.center = (1124, 600)
        surface.blit(text, textRect)
    else:
        text = font.render('Yes', True, green, blue)
        textRect.center = (1124, 600)
        surface.blit(text, textRect)
    pygame.display.update()
    pygame.time.delay(250)
    