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

    # if not active:
        # print(input_text)
        # pygame.quit()
        # exit()
        
pygame.quit()
pygame.init()

# 設定畫布大小
width, height = 700, 700
canvas_size = (width, height)

# 建立畫布
canvas = pygame.display.set_mode(canvas_size)

game_title = "刺激二十一點"  # 替換成您自己的遊戲標題
pygame.display.set_caption(game_title)

font = pygame.font.SysFont("simhei", 24)
text = font.render("Welcome to 刺激二十一點", True,  (255, 255, 255), (0, 100, 0))
canvas.blit(text, (60,60))

# 載入照片
image_path = r'C:\PBC_final_project\image\openpage.PNG'
image = pygame.image.load(image_path)

# 調整圖案大小以符合畫布
image = pygame.transform.scale(image, (600, 400))  # 調整為適當的大小

# 取得圖案在畫布中的位置
image_x = 50
image_y = 120

# 將圖案繪製在畫布上
canvas.fill((0, 0, 0))  # 填滿黑色背景
canvas.blit(image, (image_x, image_y))  # 繪製圖案
pygame.display.flip()

# 載入第一張圖片
image1_path = r'C:\PBC_final_project\image\pve_black.jpg'  # 替換成第一張圖片的路徑
image1 = pygame.image.load(image1_path)

# 調整第一張圖片大小
image1 = pygame.transform.scale(image1, (180, 100))

# 設定第一張圖片的位置（左下角）
image1_x = 150
image1_y = 550

# 將第一張圖片繪製在畫布上
canvas.blit(image1, (image1_x, image1_y))

# 載入第二張圖片
image2_path = r'C:\PBC_final_project\image\pvp_black.jpg'  # 替換成第二張圖片的路徑
image2 = pygame.image.load(image2_path)

# 調整第二張圖片大小
image2 = pygame.transform.scale(image2, (180, 100))

# 設定第二張圖片的位置（右下角）
image2_x = 400
image2_y = 550

# 將第二張圖片繪製在畫布上
canvas.blit(image2, (image2_x, image2_y))

# 更新畫面顯示
pygame.display.flip()

# 主迴圈
running = True
while running:
    # 檢查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False














