import pygame
from pygame.locals import *
import string

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

keys1 = [False, False, False, False]
keys2 = [False, False, False, False]


player1Pos=[10,400]
player2Pos=[560, 400]

# 3 - Load images
player1 = pygame.image.load("resources/images/Blastoise.png")
player2 = pygame.image.load("resources/images/Nidoking.png")


def getTragectoryY(angle, velocity, initY, currentX):
    g = 9.81  # m/s**2

    from math import pi, tan, cos
    # Convert v0 to m/s and theta to radians
    v0 = velocity / 3.6
    theta = angle * pi / 180

    currentY = currentX * tan(theta) - 1 / (2 * v0 ** 2) * g * currentX ** 2 / ((cos(theta)) ** 2) + initY
    return int(currentY)

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()


def launchMissilePlayer1(angle, speed, ypos):
    for x in range(0, 630):
        y = getTragectoryY(angle, speed, ypos, x)
        if ( y < 0):
            break
        pygame.draw.circle(screen, (255, 0, 0), (x, 480 - y), 4)
        pygame.display.update()

def launchMissilePlayer2(angle, speed, ypos):
    for x in range(0, 630):
        y = getTragectoryY(angle, speed, ypos, x)
        if ( y < 0 or y > 480):
            break
        pygame.draw.circle(screen, (255, 0, 0), (630 - x, 480 - y), 4)
        pygame.display.update()


# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
#    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player1, player1Pos)
    screen.blit(player2, player2Pos)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                screen.fill(0)
                keys1[0] = True
            elif event.key == K_a:
                screen.fill(0)
                keys1[1] = True
            elif event.key == K_s:
                screen.fill(0)
                keys1[2] = True
            elif event.key == K_d:
                screen.fill(0)
                keys1[3] = True
            elif event.key == K_i:
                screen.fill(0)
                keys2[0] = True
            elif event.key == K_j:
                screen.fill(0)
                keys2[1] = True
            elif event.key == K_k:
                screen.fill(0)
                keys2[2] = True
            elif event.key == K_l:
                screen.fill(0)
                keys2[3] = True
            elif event.key == K_z:
                current_string = []
                while 1:
                    if event.key == K_BACKSPACE:
                        current_string = current_string[0:-1]
                    elif event.key == K_RETURN:
                        break
                    elif event.key <= 127:
                        current_string.append(chr(event.key))
                    display_box(screen, "what is the velocity" + ": " + string.join(current_string, ""))
                    string.join(current_string, "")
                launchMissilePlayer1(60, 300, 0)
            elif event.key == pygame.K_m:
                launchMissilePlayer2(60, 300, 0)
            elif event.key == K_c:
                screen.fill(0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys1[0] = False
            elif event.key == pygame.K_a:
                keys1[1] = False
            elif event.key == pygame.K_s:
                keys1[2] = False
            elif event.key == pygame.K_d:
                keys1[3] = False
            elif event.key == pygame.K_i:
                keys2[0] = False
            elif event.key == pygame.K_j:
                keys2[1] = False
            elif event.key == pygame.K_k:
                keys2[2] = False
            elif event.key == pygame.K_l:
                keys2[3] = False

        if keys1[0]:
            player1Pos[1] -= 5
        elif keys1[2]:
            player1Pos[1] += 5
        if keys1[1]:
            player1Pos[0] -= 5
        elif keys1[3]:
            player1Pos[0] += 5

        if keys2[0]:
            player2Pos[1] -= 5
        elif keys2[2]:
            player2Pos[1] += 5
        if keys2[1]:
            player2Pos[0] -= 5
        elif keys2[3]:
            player2Pos[0] += 5
