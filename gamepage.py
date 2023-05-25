import tkinter as tk
from PIL import Image, ImageTk


def bet():
    # 在這裡寫下注的邏輯
    print("下注")


def hit():
    # 在這裡寫要牌的邏輯
    print("要牌")


def stand():
    # 在這裡寫停牌的邏輯
    print("停牌")


def surrender():
    # 在這裡寫投降的邏輯
    print("投降")


def on_button_press(button):
    button.config(relief=tk.SUNKEN)


def on_button_release(button):
    button.config(relief=tk.RAISED)

# 創建給所有按鈕的class 屬性依序為(按鈕名稱, 圖片路徑, 按鈕功能的function, x座標, y座標, 圖片寬度, 圖片高度)
class created_button:
    def __init__(self, name, image_path, function, location_x, location_y, width, height):
        self.raw_image = Image.open(image_path)
        self.image = self.raw_image.resize((width, height))  # 調整按鈕大小
        self.photo = ImageTk.PhotoImage(self.image)
        self.button = tk.Button(window, image=self.photo, command=function, relief=tk.RAISED)
        self.button.place(x=location_x, y=location_y)
        self.button.bind("ButtonPress"+name, lambda event: on_button_press(self.button))
        self.button.bind("ButtonRelease"+name, lambda event: on_button_release(self.button))


# 創建主窗口
window = tk.Tk()
window.title("Blackjack")

# 創建下注按鈕
bet_button = created_button("bet", "./image/bet.png", bet, 150, 150, 150, 50)
# 創建要牌按鈕
hit_button = created_button("hit", "./image/hit.png", hit, 120, 120, 150, 50)
# 創建停牌按鈕
stand_button = created_button("stand", "./image/stand.png", stand, 10, 20, 150, 50)
# 創建投降按鈕
surrender_button = created_button("surrender", "./image/surrender.png", surrender, 190, 270, 150, 50)


# 調整窗口大小
window.geometry("400x300")

# 獲取螢幕的寬度和高度
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# 計算窗口的x和y位置，使其置中
x = int((screen_width / 2) - (400 / 2))
y = int((screen_height / 2) - (300 / 2))

# 設置窗口位置
window.geometry(f"400x300+{x}+{y}")

# 開始運行主迴圈
window.mainloop()
