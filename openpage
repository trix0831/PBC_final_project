import pygame

# 初始化pygame
pygame.init()

# 設定畫布大小
width, height = 700, 700
canvas_size = (width, height)

# 建立畫布
canvas = pygame.display.set_mode(canvas_size)

game_title = "刺激二十一點"  # 替換成您自己的遊戲標題
pygame.display.set_caption(game_title)


# 載入照片
image_path = r'C:\PBC_final_project\image\logo pic.png'
image = pygame.image.load(image_path)

# 調整圖案大小以符合畫布
image = pygame.transform.scale(image, (600, 400))  # 調整為適當的大小

# 取得圖案在畫布中的位置
image_x = (width - image.get_width()) // 2
image_y = (height - image.get_height()) // 4  # 將圖案置於畫布中上方

# 將圖案繪製在畫布上
canvas.fill((0, 0, 0))  # 填滿黑色背景
canvas.blit(image, (image_x, image_y))  # 繪製圖案

# 載入第一張圖片
image1_path = r'C:\PBC_final_project\image\pve_black.jpg'  # 替換成第一張圖片的路徑
image1 = pygame.image.load(image1_path)

# 調整第一張圖片大小
image1 = pygame.transform.scale(image1, (180, 100))

# 設定第一張圖片的位置（左下角）
image1_x = 150
image1_y = 500

# 將第一張圖片繪製在畫布上
canvas.blit(image1, (image1_x, image1_y))

# 載入第二張圖片
image2_path = r'C:\PBC_final_project\image\pvp_black.jpg'  # 替換成第二張圖片的路徑
image2 = pygame.image.load(image2_path)

# 調整第二張圖片大小
image2 = pygame.transform.scale(image2, (180, 100))

# 設定第二張圖片的位置（右下角）
image2_x = 400
image2_y = 500

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

# 關閉pygame
pygame.quit()