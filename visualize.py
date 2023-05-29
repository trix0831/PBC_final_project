import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageDraw, ImageTk
import os


# 定義圖片大小
card_width, card_height = 150, 225

# 定義花色和點數
suits = ["clubs", "diamonds", "hearts", "spades"]
ranks = ["ace", "2", "3", "4", "5", "6", "7",
         "8", "9", "10", "jack", "queen", "king"]

# 載入牌背面圖片
back_image = Image.open("./image/back_red_basic_white.png")

# 載入所有牌的圖片
card_images = []
for rank in ranks:
    for suit in suits:
        card_name = f"./image/{rank}_{suit}_white.png"
        card_image = Image.open(card_name)
        card_images.append(card_image)

# 遊戲視窗
window = tk.Tk()
window.title("Blackjack")
window.geometry("600x400")


bet_amount = None
betornot = False

# 建立牌卡


class Card:
    def __init__(self, rank, suit, image):
        self.rank = rank
        self.suit = suit
        self.image = image


class Deck:
    def __init__(self):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                image_name = f"{rank}_{suit}_white.png"
                image = Image.open(f"./image/{image_name}")
                card = Card(rank, suit, image)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


def card_values(hand):
    # 計算牌的點數
    values = []
    for card in hand:
        if card.rank == "ace":
            values.append(11)
        elif card.rank in ["jack", "queen", "king"]:
            values.append(10)
        else:
            values.append(int(card.rank))
        while sum(values) > 21 and 11 in values:
            values.remove(11)
            values.append(1)
    return values
# 遊戲介面


class Game:
    dealer_1st_image = None  # 新增類別層級的變數

    def __init__(self, deck):
        self.deck = deck
        self.player_hand = []
        self.dealer_hand = []
        self.deck.shuffle()
        self.result_label = []

        # 操作區
        button_frame = tk.Frame(window)
        button_frame.pack(side="top")

        self.hit_button = tk.Button(button_frame, text="加牌", command=self.hit)
        self.hit_button.pack(side="left")

        self.stand_button = tk.Button(
            button_frame, text="停牌", command=self.stand)
        self.stand_button.pack(side="left")

        self.surrender_button = tk.Button(
            button_frame, text="投降", command=self.surrender)
        self.surrender_button.pack(side="left")

        self.restart_button = tk.Button(
            button_frame, text="重新開始", command=self.restart)
        self.restart_button.pack(side="left")

        # 下注區
        bet_frame = tk.Frame(window)
        bet_frame.pack(side="top")

        bet_label = tk.Label(bet_frame, text="注金:")
        bet_label.pack(side="left")

        self.bet_entry = tk.Entry(bet_frame)
        self.bet_entry.pack(side="left")

        self.bet_button = tk.Button(
            bet_frame, text="下注", command=self.bet)
        self.bet_button.pack(side="left")

        self.hit_button.config(state="disabled")
        self.stand_button.config(state="disabled")
        self.surrender_button.config(state="disabled")
        self.restart_button.config(state="disabled")
        self.bet_button.config(state="normal")

        # 顯示籌碼數量
        self.chips = 1000
        self.chips_label = tk.Label(window, text=f"籌碼: {self.chips}")
        self.chips_label.pack(side="top")

    def bet(self):
        self.place_bet()
        # 發牌
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())

        # 玩家牌區
        self.player_frame = tk.Frame(window)
        self.player_frame.place(x=220, y=80)

        self.player_label = []
        player_label = tk.Label(self.player_frame, text="玩家")
        player_label.pack(side="left")
        self.player_label.append(player_label)

        self.player_card_labels = []
        for card in self.player_hand:
            label_image = ImageTk.PhotoImage(card.image)
            label = tk.Label(self.player_frame, image=label_image)
            label.image = label_image
            label.pack(side="left")
            self.player_card_labels.append(label)

        # 庄家牌區
        self.dealer_frame = tk.Frame(window)
        self.dealer_frame.place(x=220, y=170)

        self.dealer_label = []
        dealer_label = tk.Label(self.dealer_frame, text="莊家")
        dealer_label.pack(side="left")
        self.dealer_label.append(dealer_label)

        self.dealer_card_labels = []
        for card in self.dealer_hand:
            if len(self.dealer_card_labels) == 0:
                label_image = ImageTk.PhotoImage(back_image)
                self.dealer_1st_image = ImageTk.PhotoImage(card.image)
            else:
                label_image = ImageTk.PhotoImage(card.image)
            label = tk.Label(self.dealer_frame, image=label_image)
            label.image = label_image
            label.pack(side="left")
            self.dealer_card_labels.append(label)

    def place_bet(self):
        bet_amount = int(self.bet_entry.get())
        self.result_label = []
        if bet_amount > self.chips:
            warn_label = tk.Label(window, text="籌碼不足")
            self.result_label.append(warn_label)
            messagebox.showerror("Invalid Bet", "Insufficient chips!")
        else:
            self.bet_amount = bet_amount
            self.chips -= self.bet_amount
            self.chips_label.config(text=f"籌碼: {self.chips}")

            # 啟用按鈕
            self.hit_button.config(state="normal")
            self.stand_button.config(state="normal")
            self.surrender_button.config(state="normal")
            self.bet_button.config(state="disabled")

    def restart(self):
        if self.chips == 0:
            window.destroy()
        # 重新啟動遊戲，重新生成一副牌並重置遊戲狀態
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []
        self.deck.shuffle()

        # 清空牌區的內容
        for label in self.player_card_labels:
            label.destroy()
        self.player_card_labels.clear()

        for label in self.dealer_card_labels:
            label.destroy()
        self.dealer_card_labels.clear()

        # 清空結果顯示區
        for player_label in self.player_label:
            player_label.destroy()
        self.player_label.clear()

        for dealer_label in self.dealer_label:
            dealer_label.destroy()
        self.dealer_label.clear()

        for label in self.result_label:
            label.destroy()
        self.result_label.clear()

        # 清空下注金額
        self.bet_entry.delete(0, tk.END)

        # 顯示更新後的籌碼數量
        self.chips_label.config(text=f"籌碼: {self.chips}")

        # 啟用按鈕
        self.hit_button.config(state="disabled")  # 禁用Hit按鈕
        self.stand_button.config(state="disabled")  # 禁用Stand按鈕
        self.surrender_button.config(state="disabled")  # 禁用Surrender按鈕
        self.restart_button.config(state="disabled")
        self.bet_button.config(state="normal")

    def clear_result_area(self):
        # 清空結果顯示區
        for child in self.window.winfo_children():
            if child.winfo_class() == "Label" and child.winfo_parent() == self.window:
                child.destroy()

    def hit(self):
        global bet_amount  # 添加global语句
        self.result_label = []
        if len(card_values(self.player_hand)) >= 5:
            result_text = "過五關! 你贏了!"
            self.chips += self.bet_amount*4
        elif sum(card_values(self.player_hand)) < 21:
            card = self.deck.deal_card()
            self.player_hand.append(card)
            # 新增抽到的牌到玩家牌區
            label_image = ImageTk.PhotoImage(card.image)
            label = tk.Label(self.player_frame, image=label_image)
            label.image = label_image
            label.pack(side="left")
            self.player_card_labels.append(label)
        elif sum(card_values(self.player_hand)) > 21:
            # 轉換莊家第一張牌為正面
            self.dealer_card_labels[0].configure(
                image=self.dealer_1st_image)  # 使用dealer_1st_image
            result_text = "玩家爆牌 莊家獲勝"
            # 顯示更新後的籌碼數量
            self.chips_label.config(text=f"籌碼: {self.chips}")
            # 顯示結果
            result_label = tk.Label(window, text=result_text)
            result_label.place(x=250, y=270)
            self.result_label.append(result_label)
            # 啟用按鈕
            self.hit_button.config(state="disabled")  # 禁用Hit按鈕
            self.stand_button.config(state="disabled")  # 禁用Stand按鈕
            self.surrender_button.config(state="disabled")  # 禁用Surrender按鈕
            self.restart_button.config(state="normal")
            self.bet_button.config(state="disabled")
        elif sum(card_values(self.player_hand)) == 21:
            # 轉換莊家第一張牌為正面
            self.dealer_card_labels[0].configure(
                image=self.dealer_1st_image)  # 使用dealer_1st_image
            if sum(card_values(self.dealer_hand)) < 17 and sum(card_values(self.dealer_hand)) < sum(card_values(self.player_hand)):
                card = self.deck.deal_card()
                self.dealer_hand.append(card)
                # 新增抽到的牌到庄家牌區
                label_image = ImageTk.PhotoImage(card.image)
                label = tk.Label(self.dealer_frame, image=label_image)
                label.image = label_image
                label.pack(side="left")
                self.dealer_card_labels.append(label)
            if sum(card_values(self.player_hand)) == 21:
                result_text = "和局"
                self.chips += self.bet_amount
            else:
                result_text = "你贏了!"
                self.chips += self.bet_amount*2
            # 顯示結果
            result_label = tk.Label(window, text=result_text)
            result_label.place(x=250, y=270)
            self.result_label.append(result_label)
            # 顯示更新後的籌碼數量
            self.chips_label.config(text=f"籌碼: {self.chips}")

            self.hit_button.config(state="disabled")  # 禁用Hit按鈕
            self.stand_button.config(state="disabled")  # 禁用Stand按鈕
            self.surrender_button.config(state="disabled")  # 禁用Surrender按鈕
            self.restart_button.config(state="normal")
            self.bet_button.config(state="disabled")

    def stand(self):
        # 轉換莊家第一張牌為正面
        self.dealer_card_labels[0].configure(
            image=self.dealer_1st_image)  # 使用dealer_1st_image
        # 玩家停牌，庄家開始抽牌
        while sum(card_values(self.dealer_hand)) < 17 and sum(card_values(self.dealer_hand)) < sum(card_values(self.player_hand)):
            card = self.deck.deal_card()
            self.dealer_hand.append(card)
            # 新增抽到的牌到庄家牌區
            label_image = ImageTk.PhotoImage(card.image)
            label = tk.Label(self.dealer_frame, image=label_image)
            label.image = label_image
            label.pack(side="left")
            self.dealer_card_labels.append(label)
        # 比較牌的大小
        player_score = sum(card_values(self.player_hand))
        dealer_score = sum(card_values(self.dealer_hand))

        if len(card_values(self.player_hand)) >= 5 and player_score < 21:
            result_text = "過五關! 你贏了!"
            self.chips += self.bet_amount*4
        elif player_score > 21:
            result_text = "玩家爆牌 莊家獲勝"
            self.chips = self.chips
        elif dealer_score > 21:
            result_text = "莊家爆牌! 你贏了!"
            self.chips += self.bet_amount*2
        elif dealer_score > player_score:
            result_text = "莊家獲勝"
            self.chips = self.chips
        elif player_score > dealer_score:
            result_text = "你贏了!"
            self.chips += self.bet_amount*2
        else:
            result_text = "和局!"
            self.chips += self.bet_amount

        # 顯示更新後的籌碼數量
        self.chips_label.config(text=f"籌碼: {self.chips}")
        # 顯示結果
        result_label = tk.Label(window, text=result_text)
        result_label.place(x=250, y=270)
        self.result_label.append(result_label)
        # 啟用按鈕
        self.hit_button.config(state="disabled")  # 禁用Hit按鈕
        self.stand_button.config(state="disabled")  # 禁用Stand按鈕
        self.surrender_button.config(state="disabled")  # 禁用Surrender按鈕
        self.restart_button.config(state="normal")
        self.bet_button.config(state="disabled")

    def surrender(self):
        # 轉換莊家第一張牌為正面
        self.dealer_card_labels[0].configure(
            image=self.dealer_1st_image)  # 使用dealer_1st_image
        # 玩家投降，直接判定為輸
        result_label = tk.Label(window, text="玩家投降 莊家獲勝")
        result_label.place(x=250, y=270)
        self.result_label.append(result_label)
        self.chips += int(self.bet_amount/2)
        self.hit_button.config(state="disabled")  # 禁用Hit按鈕
        self.stand_button.config(state="disabled")  # 禁用Stand按鈕
        self.surrender_button.config(state="disabled")  # 禁用Surrender按鈕
        self.restart_button.config(state="normal")
        self.bet_button.config(state="disabled")


deck = Deck()
game = Game(deck)
window.mainloop()
