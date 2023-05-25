import pygame

pygame.init()

# 設定視窗大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

game_title = "輸入使用者名稱"  # 替換成您自己的遊戲標題
pygame.display.set_caption(game_title)

# 設定字體和文字
font = pygame.font.SysFont("Times new roman", 30)
text = font.render("Please enter username (only English and numbers):", True, (255, 255, 255))

# 取得文字的寬度和高度
text_width, text_height = font.size("Please enter username (only English and numbers):")

# 設定輸入框
input_box = pygame.Rect(250, 300, 300, 50)
input_text = ""
max_length = 10

# 設定顏色

active = True

 # 載入照片
image_path = './image/newlogo.png'
image = pygame.image.load(image_path)

# 調整圖案大小以符合畫布
image = pygame.transform.scale(image, (280, 170))  # 調整為適當的大小

# 取得圖案在畫布中的位置
image_x = 260
image_y = 405

# 將圖案繪製在畫布上
screen.fill((0, 0, 0))  # 填滿黑色背景
screen.blit(image, (image_x, image_y))  # 繪製圖案
pygame.display.flip()


while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isprintable() and len(input_text) < max_length:
                input_text += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                # 按下 Enter 鍵後離開輸入狀態
                # input_box.active = False
                active = False
                
    screen.fill((0, 0, 0))

    # 繪製圖案
    screen.blit(image, (image_x, image_y))

    # 畫出文字和輸入框
    pygame.draw.rect(screen, (255, 255, 255), input_box)
    screen.blit(text, ((screen_width - text_width) // 2, input_box.y - text_height - 20))
    pygame.draw.rect(screen, (255, 255, 255), input_box, 2)

    # 畫出輸入的文字
    text_surface = font.render(input_text, True, (0, 0, 0))
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    # 檢查是否超過字數限制
    if len(input_text) >= max_length:
        text_surface = font.render("Max length reached", True, (255, 0, 0))
        screen.blit(text_surface, (290  , input_box.y + 70))

    pygame.display.update()

    if not active:
        print(input_text)
        pygame.quit()
        exit()














