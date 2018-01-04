import pygame

# first thing to do always
pygame.init()
# create display with size
gameDisplay = pygame.display.set_mode((800, 600))
# create title
pygame.display.set_caption("A Bit Racey")
# set a game clock
clock = pygame.time.Clock()

crashed = False

# count game ticks
# count = 0

while not crashed:

    # list of events per second
    for event in pygame.event.get():

        # if they hit the X
        if event.type == pygame.QUIT:
            crashed = True

        #print(event)

    # can put parameters into update to update only those thing
    pygame.display.update()
    # move 1/x of a second each while-loop cycle. (game ticks per second)
    # count += 1
    clock.tick(60)


# print(count)

# quit game
pygame.quit()
# quit python
quit()


