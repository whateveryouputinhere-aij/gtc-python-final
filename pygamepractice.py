import pygame

# AttributeError: partially initialized module 'pygame' has no attribute 'init' (most likely due to a circular import)
    # you CANNOT name the py file "pygame.py"
    # When you run "import pygame", Python looks in your current folder first. It finds your file (pygame.py), thinks that is the actual library, and starts importing it. Because your file is still in the middle of loading, it’s "partially initialized" and doesn't have the .init() function yet.

# Terms and Definitions:
# surfaces: basically an image in memory
# events:

pygame.init()

screen = pygame.display.set_mode((640, 640))
# creates a surface

epstein = pygame.image.load('/Users/johnsontran/Desktop/epstein.png').convert()
# converts an image file on your computer into a pygame surface (loads new image from a file)
# image in memory is basically surface
# convert() changes the pixel format of a surface
# surfaces can have different pixel formats associated with them
epstein = pygame.transform.scale(epstein, (epstein.get_width() * 2, epstein.get_height() * 2))


x = 0
clock = pygame.time.Clock()
# creates an object to help track time

delta_time = 0.1

running = True
while running:
    screen.fill((255, 255, 255))

    # note that when a pygame script runs all the way through, everything will close
    # so you need to make a game loop.

    screen.blit(epstein, (x, 30))
    # blit() draws another surface onto this one
    # pygame coordinate system has +x going right, +y going down. origin is at the top left of screen

    x += 50 * delta_time
    # measures the time between frames and multiply time dependent math by the duration of the last frame to make mation consistent even with varying frame rates


    for event in pygame.event.get():
        # pygame.event.get() gives you a list of all the events that occurred since the last time it was called
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    # updates the full display surface to the screen

    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))
    # updates the clock; the parameter represents the framerate (higher refresh rate = faster; lag = slower)
    # clock.tick() returns the time in milliseconds
    # locking game to 60 fps is okay, but standard solution is to use delta_time (making motion consistent even with varying frame)



pygame.quit()

