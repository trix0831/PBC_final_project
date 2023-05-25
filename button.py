import pygame

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button Example")

# Set up the button
button_width, button_height = 200, 100
button_x, button_y = (screen_width - button_width) // 2, (screen_height - button_height) // 2

# Function to be executed when the button is clicked
def button_action():
    print("Button clicked!")
    
screen.fill(WHITE)

# Main game loop
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
        pygame.draw.rect(screen, BLACK, (button_x, button_y, button_width, button_height))
    else:
        pygame.draw.rect(screen, GREEN, (button_x, button_y, button_width, button_height))

    # Update the display
    # pygame.display.flip()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
                button_action()
                

    # # Clear the screen


    # Draw the button

    # Update the display
    pygame.display.flip()

# Quit the program
pygame.quit()
