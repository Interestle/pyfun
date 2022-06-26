import pygame
import random

def main():
    
    # Boilerplate init crap.
    pygame.init()
    pygame.display.set_caption('Snek')

    clock = pygame.time.Clock()

    screen_size = pygame.Vector2(800, 600)
    screen_half = screen_size / 2
    screen_quarter = screen_size / 4
    screen_color = 0x000000
    screen = pygame.display.set_mode(screen_size)

    # Snake defs.
    snake_size   = 10
    snake_color  = 0xFFFFFF
    snake_parts   = [] # This is called a list in Python. It's a dynamic array. In C++, they're called vectors.
    snake_speed  = 5    

    # Put the snake head somewhere around the center of the screen. (somewhere from 1/4 to 3/4 around the screen)
    snake_pos = pygame.Vector2(random.randint(screen_quarter.x, screen_quarter.x * 3), \
                               random.randint(screen_quarter.y, screen_quarter.y * 3))

    # Have the snake shoot off in a random direction with constant speed
    snake_direction = pygame.Vector2(1,0) #pygame.Vector2.normalize(pygame.Vector2(random.uniform(-1, 1), random.uniform(-1,1)))
    snake_direction *= snake_speed


    # Pellet
    pellet_size = 10
    pellet_color = 0xFF0000
    pellet_pos = pygame.Vector2(random.randint(screen_quarter.x / 2, screen_quarter.x / 2 * 7), \
                                random.randint(screen_quarter.y / 2, screen_quarter.y / 2 * 7))


    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
                break

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]: 
            running = False
            break
        

        # Draw onto the screen
        screen.fill(screen_color)
        
        # Draw Pellet
        pygame.draw.circle(screen, pellet_color, pellet_pos, pellet_size)

        # Draw snake
        snake_pos += snake_direction
        pygame.draw.circle(screen, snake_color, snake_pos, snake_size)


        pygame.display.update()
        clock.tick(30)
        
    pygame.quit()



if __name__=='__main__':
    main()