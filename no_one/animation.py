import pygame
import random
from PIL import Image
from io import BytesIO

# 定義圖片大小
card_width, card_height = 150, 225

# 定義花色和點數
suits = ["clubs", "diamonds", "hearts", "spades"]
ranks = ["ace", "2", "3", "4", "5", "6", "7",
         "8", "9", "10", "jack", "queen", "king"]

# 載入牌背面圖片
back_image = pygame.image.load("./image/back_red_basic_white.png")

# 載入所有牌的圖片
card_images = []
for rank in ranks:
    for suit in suits:
        card_name = f"./image/{rank}_{suit}_white.png"
        card_image = pygame.image.load(card_name)
        card_images.append(card_image)


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
                image = pygame.image.load(f"./image/{image_name}")
                card = Card(rank, suit, image)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


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

        pygame.init()
        self.window_width = (card_width + 20) * len(self.player_hand)
        self.window_height = card_height + 40
        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height))
        pygame.display.set_caption("Blackjack")

        self.show_player_hand()
        self.show_dealer_hand()

        # 玩家操作
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            choice = input("Choose an action (hit/stand/surrender): ")
            if choice == "hit":
                self.hit()
                self.show_player_hand()
                player_score = sum(card_values(self.player_hand))
                if player_score > 21:
                    print("Player busts! Dealer wins!")
                    self.stand()
                    return
            elif choice == "stand":
                self.stand()
                return
            elif choice == "surrender":
                self.surrender()
                return
            else:
                print("Invalid choice! Please try again.")

    def show_player_hand(self):
        self.window.fill((0, 0, 0))
        for i, card in enumerate(self.player_hand):
            image_rect = card.image.get_rect()
            image_rect.topleft = ((card_width + 20) * i + 10, 10)
            self.window.blit(card.image, image_rect)
        pygame.display.flip()

    def show_dealer_hand(self):
        self.window.fill((0, 0, 0))
        image_rect = back_image.get_rect()
        image_rect.topleft = (10, 10)
        self.window.blit(back_image, image_rect)
        for i in range(1, len(self.dealer_hand)):
            card = self.dealer_hand[i]
            image_rect = card.image.get_rect()
            image_rect.topleft = ((card_width + 20) * i + 10, 10)
            self.window.blit(card.image, image_rect)
        pygame.display.flip()

    def hit(self):
        card = self.deck.deal_card()
        self.player_hand.append(card)

    def stand(self):
        # 玩家停牌，庄家開始抽牌
        while sum(card_values(self.dealer_hand)) < 17:
            card = self.deck.deal_card()
            self.dealer_hand.append(card)
        # 比較牌的大小
        player_score = sum(card_values(self.player_hand))
        dealer_score = sum(card_values(self.dealer_hand))
        if dealer_score > 21:
            print("Dealer busts! Player wins!")
        elif dealer_score > player_score:
            print("Dealer wins!")
        elif player_score > dealer_score:
            print("Player wins!")
        else:
            print("Push!")

    def surrender(self):
        print("Player surrenders! Dealer wins!")


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


deck = Deck()
game = Game(deck)
