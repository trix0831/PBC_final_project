import pygame as pg

pg.init()
scale = 2

width, height =  559, 238                                          # 遊戲畫面寬和高
screen = pg.display.set_mode((width*scale, height*scale))                      # 依設定顯示視窗
pg.display.set_caption("Welcome to the Black Jack game")           # 設定程式標題

# 建立畫布bg
bg = pg.Surface(screen.get_size())
bg = bg.convert()

jjingg1 = pg.image.load("./image/IMG_5903.jpeg").convert()