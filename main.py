    # 匯入pygame
import pygame as pg
import button as BT
import pve
import pvp

# pygame初始化
pg.init()

scale = 1.5

# 設定視窗
width, height =  590, 410   
button_width, button_height = 200, 100# 遊戲畫面寬和高
screen = pg.display.set_mode((width*scale, height*scale))                      # 依設定顯示視窗
pg.display.set_caption("Welcome to the Black Jack game")           # 設定程式標題

# 建立畫布bg
bg = pg.Surface(screen.get_size())
bg = bg.convert()


image_surface = pg.image.load("./image/openpage.PNG").convert()
image_new = pg.transform.scale(image_surface,(width, height))
image_1 = pg.transform.rotozoom(image_new,0,scale)
screen.blit(image_1,(0,0))

buttons = []

PVE_button = BT.button(button_width, button_height, (400, 350), ".\image\pve_black.jpg", ".\image\pve_down.png", True, pve.pve)
buttons.append(PVE_button)

PVP_button = BT.button(button_width, button_height, (640, 350), ".\image\pvp_black.jpg", ".\image\pvp_down.png", True, pvp.pvp)
buttons.append(PVP_button)

print(buttons)

for button in buttons:
    screen.blit(button.button_image[0], button.pos)

running = True

excute_index = -1

while running:
    mouse_x, mouse_y = pg.mouse.get_pos()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
        for button in buttons:
            if button.pos[0] < mouse_x < button.pos[0] + button.width and button.pos[1] < mouse_y < button.pos[1] + button.height:
                screen.blit(button.button_image[1], button.pos)
            else:
                screen.blit(button.button_image[0], button.pos)
            
        if event.type == pg.MOUSEBUTTONUP:
            for button_index in range(len(buttons)):
                if buttons[button_index].pos[0] < mouse_x < buttons[button_index].pos[0] + buttons[button_index].width and buttons[button_index].pos[1] < mouse_y < buttons[button_index].pos[1] + buttons[button_index].height:
                    excute_index = button_index
                    running = False
                
        
    pg.display.update()
            
pg.quit()   

buttons[excute_index].func(1000)