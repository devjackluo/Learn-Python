import pygame

pygame.init()

# custom variables for width and height
display_width = 800
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
carImg = pygame.transform.scale(carImg, (100, 100))


# function to create car at a location
def car(x, y):
    gameDisplay.blit(carImg, (x, y))


# create position for car
x = (display_width/2 - 50)
y = (display_height*0.8 - 50)


crashed = False
while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True

    # fill screen first to not cover car
    gameDisplay.fill((255,255,255))
    car(x, y)

    pygame.display.update()
    # flip book
    # pygame.display.flip()
    clock.tick(60)


pygame.quit()
quit()


