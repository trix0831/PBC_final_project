import button as BT

Hit_button = BT.button(button_width, button_height, (180, 533), ".\image\hit_up.png", ".\image\hit_down.png", True, hit)
buttons.append(Hit_button)

Stand_button = BT.button(button_width, button_height, (180, 668), ".\image\stand_up.png", ".\image\stand_down.png", True, stand)
buttons.append(Stand_button)

Surrender_button = BT.button(button_width, button_height, (180, 803), ".\image\surrender_up.png", ".\image\surrender_down.png", True, surrender)
buttons.append(Surrender_button)

End_button = BT.button(button_width, button_height, (180, 938), ".\image\surrender_up.png", ".\image\surrender_down.png", True, end)
buttons.append(End_button)

Continue_button = BT.button(button_width, button_height, (180, 1073), ".\image\surrender_up.png", ".\image\surrender_down.png", True, Continue)
buttons.append(Continue_button)

