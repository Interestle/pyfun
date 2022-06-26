import pygame
import random

def main():
    
    # Boilerplate init crap.
    pygame.init()
    pygame.display.set_caption('Snek')

    clock = pygame.time.Clock()

    screen_size = pygame.Vector2(800, 600)
    screen_color = 0x000000
    screen = pygame.display.set_mode(screen_size)

    # Snake defs.
    snake_size  = 20
    snake_color = 0xFFFFFF

    # Put the snake head somewhere around the center of the screen.
    snake_pos = pygame.Vector2(random.randint(screen_size.x - 100, screen_size.x + 100), \
                               random.randint(screen_size.y - 100, screen_size.y + 100))
    score = 0

    reset_game = False

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]: running = False

        # Draw onto the screen
        screen.fill(screen_color)


        # Draw snake


        pygame.display.update()
        clock.tick(30)
        
    pygame.quit()



if __name__=='__main__':
    main()