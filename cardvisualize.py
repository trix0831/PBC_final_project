import random
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk


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
    def __init__(self, deck):
        self.deck = deck
        self.player_hand = []
        self.dealer_hand = []
        self.deck.shuffle()

        # 發牌
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())

        # 玩家牌區
        self.player_frame = tk.Frame(window)
        self.player_frame.pack(side="top")

        player_label = tk.Label(self.player_frame, text="Player")
        player_label.pack(side="left")

        self.player_card_labels = []
        for card in self.player_hand:
            label_image = ImageTk.PhotoImage(card.image)
            label = tk.Label(self.player_frame, image=label_image)
            label.image = label_image
            label.pack(side="left")
            self.player_card_labels.append(label)

        # 庄家牌區
        self.dealer_frame = tk.Frame(window)
        self.dealer_frame.pack(side="top")

        dealer_label = tk.Label(self.dealer_frame, text="Dealer")
        dealer_label.pack(side="left")

        self.dealer_card_labels = []
        for card in self.dealer_hand:
            if len(self.dealer_card_labels) == 0:
                label_image = ImageTk.PhotoImage(back_image)
            else:
                label_image = ImageTk.PhotoImage(card.image)
            label = tk.Label(self.dealer_frame, image=label_image)
            label.image = label_image
            label.pack(side="left")
            self.dealer_card_labels.append(label)

        # 操作區
        button_frame = tk.Frame(window)
        button_frame.pack(side="top")

        self.hit_button = tk.Button(button_frame, text="Hit", command=self.hit)
        self.hit_button.pack(side="left")

        self.stand_button = tk.Button(
            button_frame, text="Stand", command=self.stand)
        self.stand_button.pack(side="left")

        self.surrender_button = tk.Button(
            button_frame, text="Surrender", command=self.surrender)
        self.surrender_button.pack(side="left")

        self.restart_button = tk.Button(
            button_frame, text="Restart", command=self.restart)
        self.restart_button.pack(side="left")

    def restart(self):
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

        # 發牌
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())

        # 重新建立牌區的內容
        for card in self.player_hand:
            label_image = ImageTk.PhotoImage(card.image)
            label = tk.Label(self.player_frame, image=label_image)
            label.image = label_image
            label.pack(side="left")
            self.player_card_labels.append(label)

        for i, card in enumerate(self.dealer_hand):
            if i == 0:
                label_image = ImageTk.PhotoImage(back_image)
            else:
                label_image = ImageTk.PhotoImage(card.image)
            label = tk.Label(self.dealer_frame, image=label_image)
            label.image = label_image
            label.pack(side="left")
            self.dealer_card_labels.append(label)

        # 清空結果顯示區
        self.clear_result_area()

        # 啟用按鈕
        self.hit_button.config(state="normal")
        self.stand_button.config(state="normal")
        self.surrender_button.config(state="normal")

    def clear_result_area(self):
        # 清空結果顯示區
        for child in window.winfo_children():
            if child.winfo_class() == "Label" and child.winfo_parent() == window:
                child.pack_forget()

    def hit(self):
        if sum(card_values(self.player_hand)) < 21:
            card = self.deck.deal_card()
            self.player_hand.append(card)
            # 新增抽到的牌到玩家牌區
            label_image = ImageTk.PhotoImage(card.image)
            label = tk.Label(self.player_frame, image=label_image)
            label.image = label_image
            label.pack(side="left")
            self.player_card_labels.append(label)
        if sum(card_values(self.player_hand)) >= 21:
            result_text = "Player busts! Dealer wins!"
            # 顯示結果
            result_label = tk.Label(window, text=result_text)
            result_label.pack(side="top")

            self.hit_button.config(state="disabled")  # 禁用Hit按鈕
            self.stand_button.config(state="disabled")  # 禁用Stand按鈕
            self.surrender_button.config(state="disabled")  # 禁用Surrender按鈕

    def stand(self):
        # 玩家停牌，庄家開始抽牌
        while sum(card_values(self.dealer_hand)) < 17:
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

        if player_score > 21:
            result_text = "Player busts! Dealer wins!"
        elif dealer_score > 21:
            result_text = "Dealer busts! Player wins!"
        elif dealer_score > player_score:
            result_text = "Dealer wins!"
        elif player_score > dealer_score:
            result_text = "Player wins!"
        else:
            result_text = "Push!"

        # 顯示結果
        result_label = tk.Label(window, text=result_text)
        result_label.pack(side="top")

    def surrender(self):
        # 玩家投降，直接判定為輸
        result_label = tk.Label(window, text="Player surrenders! Dealer wins!")
        result_label.pack(side="top")


deck = Deck()
game = Game(deck)
window.mainloop()
