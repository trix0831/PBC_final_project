import tkinter as tk
from PIL import Image, ImageTk

# 背景圖片路徑
background_image_path = "./image/game_background.png"


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


# 創建主窗口
window = tk.Tk()
window.title("Blackjack")


# 創建Canvas元件
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# 設定背景圖片
background_image = Image.open(background_image_path)
background_photo = ImageTk.PhotoImage(background_image)
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# 載入圖片並創建下注按鈕
bet_image = Image.open("./image/bet.png")
bet_image = bet_image.resize((150, 50))  # 調整按鈕大小
bet_photo = ImageTk.PhotoImage(bet_image)
bet_button = tk.Button(window, image=bet_photo, command=bet, relief=tk.RAISED)
bet_button.pack(pady=10)
bet_button.bind("<ButtonPress-1>", lambda event: on_button_press(bet_button))
bet_button.bind("<ButtonRelease-1>",
                lambda event: on_button_release(bet_button))

# 載入圖片並創建要牌按鈕
hit_image = Image.open("./image/hit.png")
hit_image = hit_image.resize((150, 50))  # 調整按鈕大小
hit_photo = ImageTk.PhotoImage(hit_image)
hit_button = tk.Button(window, image=hit_photo, command=hit, relief=tk.RAISED)
hit_button.pack(pady=10)
hit_button.bind("<ButtonPress-1>", lambda event: on_button_press(hit_button))
hit_button.bind("<ButtonRelease-1>",
                lambda event: on_button_release(hit_button))

# 載入圖片並創建停牌按鈕
stand_image = Image.open("./image/stand.png")
stand_image = stand_image.resize((150, 50))  # 調整按鈕大小
stand_photo = ImageTk.PhotoImage(stand_image)
stand_button = tk.Button(window, image=stand_photo,
                         command=stand, relief=tk.RAISED)
stand_button.pack(side=tk.BOTTOM, pady=10)  # 將按鈕放置在底部
stand_button.bind("<ButtonPress-1>",
                  lambda event: on_button_press(stand_button))
stand_button.bind("<ButtonRelease-1>",
                  lambda event: on_button_release(stand_button))

# 載入圖片並創建投降按鈕
surrender_image = Image.open("./image/surrender.png")
surrender_image = surrender_image.resize((150, 50))  # 調整按鈕大小
surrender_photo = ImageTk.PhotoImage(surrender_image)
surrender_button = tk.Button(
    window, image=surrender_photo, command=surrender, relief=tk.RAISED)
surrender_button.pack(side=tk.BOTTOM, pady=10)  # 將按鈕放置在底部
surrender_button.bind(
    "<ButtonPress-1>", lambda event: on_button_press(surrender_button))
surrender_button.bind("<ButtonRelease-1>",
                      lambda event: on_button_release(surrender_button))

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
