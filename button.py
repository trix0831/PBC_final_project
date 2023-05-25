import pygame

        
def button_pressed():
    print("button pressed")

class button:
    def __init__(self, width, height, pos, location1, location2, func = button_pressed()) -> None:
        self.width = width
        self.height = height
        self.pos = pos
        self.func = func
        
        self.button_image = []
    
        image_surface = pygame.image.load(location1).convert()
        image_new = pygame.transform.scale(image_surface,(width, height))
        image_1 = pygame.transform.rotozoom(image_new,0,1)

        self.button_image.append(image_1)
        
        image_surface = pygame.image.load(location2).convert()
        image_new = pygame.transform.scale(image_surface,(width, height))
        image_1 = pygame.transform.rotozoom(image_new,0,1)

        self.button_image.append(image_1)
        
