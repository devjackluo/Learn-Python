import pygame
import time
import random

pygame.init()

# custom variables for width and height
display_width = 400
display_height = 600

# some info on how colors work, RGB
# black = (0,0,0)
# white = (255,255,255)
# red = (255,0,0)


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("A Bit Racey")
clock = pygame.time.Clock()

# load car image
carImg = pygame.image.load('red-race.png')
car_width = 60
cae_height = 80
carImg = pygame.transform.scale(carImg, (car_width, cae_height))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])



# function to create car at a location
def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def crash():
    message_display('You CRASHED!')

def game_loop():

    # create position for car
    x = (display_width/2 - car_width/2)
    y = (display_height*0.8 - car_width/2)

    x_change = 0

    thing_startx = random.randrange(0, display_width-60)
    thing_starty = -600
    thing_speed = 7
    thing_width = 60
    thing_height = 80



    left = False
    right = False
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                elif event.key == pygame.K_RIGHT:
                    right = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                elif event.key == pygame.K_RIGHT:
                    right = False



        if left and right:
            x_change *= 1
        elif left:
            x_change = -5
        elif right:
            x_change = 5
        else:
            x_change = 0

        x += x_change


        # fill screen first to not cover car
        gameDisplay.fill((255,255,255))


        things(thing_startx, thing_starty, thing_width, thing_height, (0,0,0))
        thing_starty += thing_speed

        car(x, y)

        if x  > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = -200
            thing_startx = random.randrange(0, display_width-60)

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()


