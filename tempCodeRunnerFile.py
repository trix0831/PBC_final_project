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