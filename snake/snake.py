import random
import pygame


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
    snake_parts  = [] # This is called a list in Python. It's a dynamic array. In C++, they're called vectors.
    snake_speed  = 5    

    # Put the snake head somewhere around the center of the screen. (somewhere from 1/4 to 3/4 around the screen)
    snake_parts.append(pygame.Vector2(random.randint(screen_quarter.x, screen_quarter.x * 3), \
                               random.randint(screen_quarter.y, screen_quarter.y * 3)))

    snake_parts.append(pygame.Vector2(100,100))
    snake_parts.append(pygame.Vector2(200,200))
    snake_parts.append(pygame.Vector2(300,300))
    snake_parts.append(pygame.Vector2(400,400))
    snake_parts.append(pygame.Vector2(500,500))
    snake_parts.append(pygame.Vector2(600,600))
    
    # Have the snake shoot off in a random direction with constant speed
    snake_direction = pygame.Vector2.normalize(pygame.Vector2(random.uniform(-1, 1), random.uniform(-1,1)))
    snake_direction *= snake_speed

    # Pellet
    pellet_size = 10
    pellet_color = 0xFF0000
    pellet_pos = pygame.Vector2(random.randint(screen_quarter.x / 2, screen_quarter.x / 2 * 7), \
                                random.randint(screen_quarter.y / 2, screen_quarter.y / 2 * 7))

    score = 0

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
                break

        # Update logic
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]: 
            running = False
            break
        if key[pygame.K_LEFT]:
            snake_direction = snake_direction.rotate(-10)
        if key[pygame.K_RIGHT]:
            snake_direction = snake_direction.rotate(10)

        if key[pygame.K_SPACE]:
            pygame.time.wait(5000)
            

        
        # Snake logic
        if snake_parts[0].x > screen_size.x or snake_parts[0].x < 0 or snake_parts[0].y > screen_size.y or snake_parts[0].y < 0:
            #TODO: end game, give score...
            running = False
        
        # Update snake part positions
        # in C/C++:
        # for (int i = snake_parts.length()-1; i > 0; i--) {
        #     snake_parts[i] = snake_parts[i-1]
        # }
        print("")
        for i in range(len(snake_parts)-1,0,-1):
            print(i,': ',  snake_parts[i], ' -> ', snake_parts[i-1])
            #print('\t', )
            snake_parts[i].x = snake_parts[i-1].x
            snake_parts[i].y = snake_parts[i-1].y
            
        snake_parts[0] += snake_direction               

        # Pellet logic
        if snake_parts[0].distance_to(pellet_pos) < 20:
            score += 1
            pellet_pos = pygame.Vector2(random.randint(screen_quarter.x / 2, screen_quarter.x / 2 * 7), \
                                random.randint(screen_quarter.y / 2, screen_quarter.y / 2 * 7))
            print("HIT!")
            snake_parts.append(snake_parts[-1])

        # Draw onto the screen
        screen.fill(screen_color)
        
        # Draw Pellet
        pygame.draw.circle(screen, pellet_color, pellet_pos, pellet_size)

        # Draw snake        
        # Draw body
        for part in snake_parts:
            pygame.draw.circle(screen, snake_color, part, snake_size)

        pygame.display.update()
        clock.tick(30)
        
    pygame.quit()



if __name__=='__main__':
    main()
