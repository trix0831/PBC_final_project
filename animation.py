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

# 遊戲介面


class Game:
    def __init__(self, deck):
        self.deck = deck
        self.player_hand = []
        self.dealer_hand = []
        # define player_frame as an instance variable
        self.player_frame = tk.Frame(window)
        # 洗牌
        self.deck.shuffle()

        # 發牌
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())
        self.player_hand.append(self.deck.deal_card())
        self.dealer_hand.append(self.deck.deal_card())

        # 玩家牌區
        player_frame = tk.Frame(window)
        player_frame.pack(side="top")

        player_label = tk.Label(player_frame, text="Player")
        player_label.pack(side="left")

        self.player_card_labels = []
        for card in self.player_hand:
            label_image = ImageTk.PhotoImage(card.image)
            label = tk.Label(player_frame, image=label_image)
            label.image = label_image
            label.pack(side="left")
            self.player_card_labels.append(label)

        # 庄家牌區
        dealer_frame = tk.Frame(window)
        dealer_frame.pack(side="top")

        dealer_label = tk.Label(dealer_frame, text="Dealer")
        dealer_label.pack(side="left")

        self.dealer_card_labels = []
        for card in self.dealer_hand:
            if len(self.dealer_card_labels) == 0:
                label_image = ImageTk.PhotoImage(back_image)
            else:
                label_image = ImageTk.PhotoImage(card.image)
            label = tk.Label(dealer_frame, image=label_image)
            label.image = label_image
            label.pack(side="left")
            self.dealer_card_labels.append(label)

        # 操作區
        button_frame = tk.Frame(window)
        button_frame.pack(side="top")

        hit_button = tk.Button(button_frame, text="Hit", command=self.hit)
        hit_button.pack(side="left")

    def hit(self):
        card = self.deck.deal_card()
        self.player_hand.append(card)
        label_image = ImageTk.PhotoImage(card.image)
        label = tk.Label(self.player_frame, image=label_image)
        label.image = label_image
        label.pack(side="left")
        self.player_card_labels.append(label)


game_deck = Deck()
game = Game(game_deck)
window.mainloop()
