# Here's a simple Pong clone written in Python using pygame.
# Feel free to study it, change it, and have fun with it as you see fit.
# Initially to control player 1, it is 'W' to move up and 'S' to move down
# Initially to control player 2, it is 'UP'to ove up and 'DOWN' to move down (arrow keys)
# To quit, press the escape key, or close the window normally(ALT+F4, press the X, SIGINT, SIGKILL, ...)
# If you have any questions, feel free to ask me about them.
#
# This is far from the most optimized way to do things, but I feel this is written
# in a way that isn't too hard to understand (I hope?)
# Make a copy of this, and fiddle with the numbers and see what happens, that's
# half of how all of computer science was founded.

# A natural progression after Pong is to try and make a Breakout clone
# After that, try things like Frogger, Tetris, any old atari, colecovision, etc.
# will probably be great starting points.

# If you're looking for inspiration, I really like this guy's Youtube videos, he
# writes a bunch of games in C++. The language doesn't really matter, it's the concepts
# he teaches.
# https://www.youtube.com/c/javidx9

# For math, there's 3Blue1Brown:
# https://www.youtube.com/c/3blue1brown

# This guy delves deep into old NES games and talks about the code. It gets
# pretty advance, so it can be intimidating, but it's really cool:
# https://www.youtube.com/c/DisplacedGamers

# I've got tons of other recommendations too if you're interested. If they talk about
# something you want to know more about, just lemme know.

# Important libraries we're using
import pygame
import random

# Starting point of code
def main():
    # Define pygame and main screen
    pygame.init()
    pygame.display.set_caption('PONG!!')

    clock = pygame.time.Clock()

    # I could define everything with x and y coordinates, but the Vector class in
    # pygame already does that for me. All I have to do is call it, then I can
    # use the nice functions for easy math. It does make it harder to understand
    # for a noobie. Sorry.
    screen_size = pygame.Vector2(800, 600)
    screen = pygame.display.set_mode(screen_size)

    # Let's define a few colors. Try combining these colors and seeing what you get.
    # For example, Cyan (I think): green + blue: 0x00FFFF. You can also just import
    # HTML color codes for all 2^24 (16.8 million colors).
    black = 0x000000
    red   = 0xFF0000
    green = 0x00FF00
    blue  = 0x0000FF
    white = 0xFFFFFF

    screen_color = black

    # Text on screen
    # You can probably use a font more interesting than the default if you'd like,
    # just look at the documentation for Pygame TODO: Use a cool retro font
    game_font = pygame.font.Font(pygame.font.get_default_font(), 64)

    # Ball paramaters
    ball_size = 20
    ball_color = white
    ball_pos = pygame.Vector2(screen_size / 2) # Put the ball in the center of the screen
    ball_vel = pygame.Vector2(10, 10)

    # Randomize the initial direction of the ball (Hacker Dark Magic--I don't know an 'easier' way to do it)
    ball_vel.x *= int((-1)**random.getrandbits(1))
    ball_vel.y *= int((-1)**random.getrandbits(1))

    # Player Parameters
    player_vel = 20
    player_width = 20
    player_height = 200

    # I initially define these squares to be at the top left. The reason is because
    # after you create it, you can define the positions of the rectangles by their
    # centers.
    p1 = pygame.Rect((0,0), (player_width, player_height))
    p1.center = (50, screen_size.y / 2)

    p2 = pygame.Rect((0,0), (player_width, player_height))
    p2.center = (screen_size.x - 50, screen_size.y / 2)

    p1_score = 0
    p2_score = 0

    # You have to render the font every time you update the text. You can also
    # optimize how the text is rendered as shown below.
    p1_score_txt = game_font.render(str(p1_score), True, ball_color, screen_color)
    p2_score_txt = game_font.render(str(p2_score), True, ball_color, screen_color)

    # Misc Variables
    reset_game = False

    # Game Loop
    while True:
        # Variables we want to update each frame
        p1_vel = 0
        p2_vel = 0

        # Get inputs and events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: break

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]: break # Bail

        if key[pygame.K_w]: p1_vel -= player_vel # P1 goes up
        if key[pygame.K_s]: p1_vel += player_vel # P1 goes down

        if key[pygame.K_UP]:   p2_vel -= player_vel # P2 goes up
        if key[pygame.K_DOWN]: p2_vel += player_vel # P2 goes down

        # Fill Background
        screen.fill(screen_color)

        # Draw Center Line TODO: Make it a dashed line like in old-school Pong?
        pygame.draw.line(screen, white, (screen_size.x/2, 0), (screen_size.x/2, screen_size.y))

        # TODO: Draw Field?

        # Draw Scores... This was a pain in the ass to get centered the way I like it.
        p1_txt_center = pygame.Vector2(p1_score_txt.get_size()) / 2
        p2_txt_center = pygame.Vector2(p2_score_txt.get_size()) / 2
        screen.blit(p1_score_txt, ((screen_size.x/2) - p1_txt_center.x - 50, 10 + p1_txt_center.y))
        screen.blit(p2_score_txt, ((screen_size.x/2) - p2_txt_center.x + 50, 10 + p2_txt_center.y))

        # Update and draw players
        p1.y += p1_vel
        if p1.top <= 0: # Prevent P1 from going to heaven (too far up)
            p1.top = 0
        if p1.bottom >= screen_size.y:
            p1.bottom = screen_size.y # Prevent P1 from going to hell (too far down)

        pygame.draw.rect(screen, ball_color, p1)

        p2.y += p2_vel
        if p2.top <= 0:
            p2.top = 0
        if p2.bottom >= screen_size.y:
            p2.bottom = screen_size.y

        pygame.draw.rect(screen, ball_color, p2)

        # Update and draw ball
        # Handle normal collision
        ball_touching_p1 = p1.collidepoint(ball_pos)
        ball_touching_p2 = p2.collidepoint(ball_pos)

        # Here's where if the ball hits a player's paddle, it will bounce off to the other side.
        # Here's a couple of ideas I was having with this:
        #   Maybe have the direction of the ball go off of the half of the paddle that was hit?
        #   Maybe have the ball have some spin if the paddle has velocity? (like in real ping pong)
        #   Maybe have the ball get slightly faster on each successive hit?
        #   Maybe have the ball change sizes (and/or speed?) on each successive hit?
        #   Have fun however you see fit?
        if ball_touching_p1 or ball_touching_p2:
            ball_vel.x = -ball_vel.x

        if ball_pos.y > screen_size.y or ball_pos.y < 0:
            ball_vel.y = -ball_vel.y

        ball_pos += ball_vel
        pygame.draw.circle(screen, ball_color, ball_pos, ball_size)

        # Now let's check for win conditions
        if ball_pos.x < 0:
            p2_score += 1
            reset_game = True
        if ball_pos.x > screen_size.x:
            p1_score += 1
            reset_game = True

        if reset_game:
            # Reset ball's position and randomize direction.
            ball_pos.update(screen_size / 2)
            ball_vel.x *= int((-1)**random.getrandbits(1))
            ball_vel.y *= int((-1)**random.getrandbits(1))

            # Update scores
            p1_score_txt = game_font.render(str(p1_score), True, ball_color, screen_color)
            p2_score_txt = game_font.render(str(p2_score), True, ball_color, screen_color)

            # Now that the game is reset, let's get it up and going again, but
            # let's give everyone a breather for a second to think.
            reset_game = False
            pygame.time.wait(2000) # Stop everything for 2 seconds (2000 milliseconds)

        # Update rest of game
        pygame.display.update()
        clock.tick(30)

    # End of while loop. Hard part about Python is scope can be hard to see.
    # Gracefully exit pygame and program.
    pygame.quit()

# Because python is a scripting language, there's this funky thing at the bottom.
# This is actually where the code starts... The bottom!
if __name__=='__main__':
    main()
