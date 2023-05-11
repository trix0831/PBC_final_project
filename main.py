    # 匯入pygame
import pygame as pg
import jjingg as jg

# pygame初始化
pg.init()

scale = 2

# 設定視窗
width, height =  559, 238                                          # 遊戲畫面寬和高
screen = pg.display.set_mode((width*scale, height*scale))                      # 依設定顯示視窗
pg.display.set_caption("Welcome to the Black Jack game")           # 設定程式標題

# 建立畫布bg
bg = pg.Surface(screen.get_size())
bg = bg.convert()


image_surface = pg.image.load("./image/background_new.jpg").convert()
image_new = pg.transform.scale(jg.jjingg1,(width, height))
# 对新生成的图像进行旋转至0度
# 使用rotozoom() 旋转 0 度，将图像缩小2.5倍
image_1 = pg.transform.rotozoom(image_new,0,scale)

# 将最后生成的image_2添加到显示屏幕上
screen.blit(image_1,(0,0))
# pg.display.update()


# 宣告 font 文字物件
head_font = pg.font.SysFont(None, 60)
# 渲染方法會回傳 surface 物件
text_surface = head_font.render('Welcome to the Black Jack game !', True, (0, 255, 255))
# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
screen.blit(text_surface, (10, 10))

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pg.display.update()



running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                running = False
pg.quit()   
