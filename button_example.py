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
button_image = []


image_surface = pygame.image.load("./image/bet.png").convert()
image_new = pygame.transform.scale(image_surface,(button_width, button_height))
image_1 = pygame.transform.rotozoom(image_new,0,1)

button_image.append(image_1)

image_surface = pygame.image.load("./image/hit.png").convert()
image_new = pygame.transform.scale(image_surface,(button_width, button_height))
image_1 = pygame.transform.rotozoom(image_new,0,1)

button_image.append(image_1)

print(button_image)

# image_surface = pygame.image.load("./image/background_new.jpg").convert()
# image_new = pygame.transform.scale(image_surface,(button_width, button_height))
# image_1 = pygame.transform.rotozoom(image_new,0,0.5)

# button_image.append(image_1)



# Function to be executed when the button is clicked
def button_action():
    print("Button clicked!")
    
screen.fill(WHITE)

# Main game loop
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
        # pygame.draw.rect(screen, BLACK, (button_x, button_y, button_width, button_height))
        screen.blit(button_image[0],(button_x, button_y))
    else:
        # pygame.draw.rect(screen, GREEN, (button_x, button_y, button_width, button_height))
        screen.blit(button_image[1],(button_x, button_y))

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
