"""
Final Project: Snake Game
This game is an imitation of the classic Snake game which came with the NOKIA handsets
The objective of this game is to eat as many food packs as possible while avoididng the walls and
the snake's continuously growing body
"""

# pygame (the library) is a Free and Open Source python programming language
# library for making multimedia applications like games.
import pygame
import time
import random

# Initializing the pygame library
pygame.init()

# Defining the colours needed in the program
white = (255, 255, 255)
yellow = (255, 215, 0)
black = (0, 0, 0)
red = (238, 44, 44)
green = (34, 139, 34)
blue = (0, 0, 205)

# Defining the width and height of the display on which the game will be played
dis_width = 600
dis_height = 400

# Creating the display and naming the window
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Creating an object to help track time
clock = pygame.time.Clock()

# Defining the dimensions of the squares of which the snake is made up of
snake_block = 10
snake_speed = 15

# Formatting the font to be used in displaying the score
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 15)


# Displaying your score on the screen
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [dis_width - 110, 0])


# Drawing the snake using the values stored in snake_list
def our_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, white, [i[0], i[1], snake_block, snake_block])


# Display a WaterMark on the screen
def watermark(mark):
    value = score_font.render(str(mark), True, blue)
    dis.blit(value, [dis_width - 200, dis_height - 25])


# Display a message on the screen when the game is over
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6.5, dis_height / 3])


# Main function which runs the game of snake
def gameLoop():
    # Presetting the boolean values to correctly start the game
    game_over = False
    game_close = False

    # Setting the values of (x,y) coordinates for the initial position of the snake
    x = dis_width / 2
    y = dis_height / 2

    # Defining variables to capture the change in (x,y) coordinates of the snake head
    dx = 0
    dy = 0

    # Creating empty list to store values
    snake_List = []
    Length_of_snake = 1

    # Generating random (x,y) coordinates for the top left corner of the rectangle considered as food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        # When the game is over this loop wlil be executed
        while game_close:
            # Display a message and the score when game is over
            dis.fill(black)
            message("GAME OVER! Press 'P-PLAY AGAIN' or 'Q-QUIT'", red)
            watermark('Created by Ayush Srivastav')
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # Continue according to the key pressed after GAME OVER
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # If Q is pressed you quit the game
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    # If P is pressed the game resets
                    if event.key == pygame.K_p:
                        gameLoop()

        # Loop which allows you to play the game
        for event in pygame.event.get():
            # If X is pressed between the game you will exit the game
            if event.type == pygame.QUIT:
                game_over = True
            # Controlling the snake with the arrow keys
            if event.type == pygame.KEYDOWN:
                # Pressing any arrow key will bring simultaneous change in its (x,y) coordinates
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        # If the snake head touches the boundary of the display you loose
        if x >= dis_width or x < 0 or y >= dis_height or y < 0:
            game_close = True

        # Changing the (x,y) coordinates of the snake
        x += dx
        y += dy

        # Drawing food of the size of a snake block
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Storing the (x,y) coordinates of the food in a list
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)

        # Passing the eaten food locations to increase the length of the snake
        snake_List.append(snake_Head)

        # Resetting the snake list to store future values
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # If the snake touches itself the game is over
        for elem in snake_List[:-1]:
            if elem == snake_Head:
                game_close = True

        # Drawing the snake and calculating your score continuously
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        # Increasing the length of snake per food it eats
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Return to the loop after eating one food to create the next food and eat it
gameLoop()
