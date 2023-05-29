# ---------------------------------------------

import random
import time
chips = 1000
reset = ''

def pve(chips = 1000):
    print("pve")

    print(chips)

    class Player:
        def __init__(self, cards, cards_rank, points_sum, status, chips):
            self.cards = cards
            self.cards_rank = cards_rank
            self.points_sum = points_sum
            self.status = status
            self.chips = chips

    rank_list = []
    for k in range(13):
        rank_list.append(["clubs", "diamonds", "hearts", "spades"])

    cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
    translate = {"J": 10, "Q": 10, "K": 10, "Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
    translate_for_rank = {"J": 10, "Q": 11 , "K": 12, "Ace": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9}
    # 發牌
    def deal_card():
        card = random.choice(cards)
        cards.remove(card)
        rank = random.choice(rank_list[translate_for_rank[card]])
        rank_list[translate_for_rank[card]].remove(rank)
        return [card, rank]

    # 算總和來決定ace要當成11還是1
    def calculate_points(cards):
        translate = {"J": 10, "Q": 10, "K": 10, "Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
        points_sum = 0
        for i in range(len(cards)):
            points_sum += translate[cards[i]]

        # points_sum = sum(cards)

        if len(cards) == 2:
            return points_sum

        if points_sum > 21 and "Ace" in cards:
            translate = {"J": 10, "Q": 10, "K": 10, "Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
            points_sum = 0
            for i in range(len(cards)):
                points_sum += translate[cards[i]]

        return points_sum

    detail = []
    def game_start():
        # 發玩家、莊家的牌
        for i in range(2):
            playing = Player([], [], 0, 0, 0) 
            deal_result = deal_card()
            playing.cards.append(deal_result[0])
            playing.cards_rank.append(deal_result[1])
            deal_result = deal_card()
            playing.cards.append(deal_result[0])
            playing.cards_rank.append(deal_result[1])
            playing.points_sum = calculate_points(playing.cards)
            detail.append(playing)

        # # 如何對每個用戶端印出:您是玩家n or 改為印出'您' 而非 '玩家n' 之類的?
        # for i in range(1):
        #     print("您" + str(i + 1) + "的明牌：" , detail[i].cards[0], sep = '')
        #     time.sleep(0.2)
        print(f"莊家的明牌：{detail[-1].cards[0]}")
        return detail

    def Bet(detail, chips):
        for i in range(1):
            finish = False
            bet = ''
            while not finish:
                try:
                    bet = int(input("輸入您本輪欲下注的金額:"))
                    if bet < 150:
                        print("下注金額不足,請重新下注")
                    elif bet > chips:
                        print("下注金額超過您擁有的籌碼,請重新下注")
                    else:
                        finish = True
                        detail[0].chips = bet
                        chips -= bet
                        return chips
                except:
                    print("投注失敗,請重新下注")

    def Surrender(k, detail):
        surrender = ""
        while surrender != 'n':
            surrender = input("輸入y投降,輸入n繼續:")
            # 投降
            if surrender == "y":
                print("您" + str(k + 1) + "已投降,返回其一半籌碼")
                detail[k].status = "已投降"
                return detail[k]
            elif surrender == "n":
                return detail[k]
            else:
                print("請重新輸入!")


    # 每個玩家加完牌後才換下一個
    def add_cards(i, detail):
        # 第n個玩家, 第一張牌, 第二張牌
        add_card = ""
        while add_card != "n":
            if len(detail[i].cards) == 5:
                # 過五關
                if detail[i].points_sum <= 21:
                    add_card = "n"
                    detail[i].status = "過五關"
                    return detail[i]
                else:
                    add_card = "n"
                    print("您" + str(i + 1) + "的牌：", detail[i].cards, "，共" + str(detail[i].points_sum) + "點", sep = '')

            else:
                add_card = input("輸入y加牌、輸入n停牌:")

                if add_card == "y":
                    deal_result = deal_card()
                    detail[i].cards.append(deal_result[0])
                    detail[i].cards_rank.append(deal_result[1])
                    detail[i].points_sum = calculate_points(detail[i].cards)
                    if detail[i].points_sum > 21:
                        add_card = "n"
                        print("您" + str(i + 1) + "的牌：", detail[i].cards, "，共" + str(detail[i].points_sum) + "點", sep = '')
                    else:
                        print("您" + str(i + 1) + "的牌：", detail[i].cards, "，共" + str(detail[i].points_sum) + "點", sep = '')
                elif add_card == "n":
                    detail[i].points_sum = calculate_points(detail[i].cards)
                    print("您" + str(i + 1) + "最終的牌：", detail[i].cards, "，共" + str(detail[i].points_sum) + "點", sep = '')
                else:
                    print("請重新輸入!")

        if detail[i].points_sum > 21:
            detail[i].status = "爆"
            return detail[i]
        else:
            detail[i].status = 0
            return detail[i]


    # 主程式，遊戲開始

    print("正在發牌,請稍後")
    time.sleep(1)

    detail = game_start()

    chips = Bet(detail, chips)

    print("您目前的籌碼剩餘:" + str(chips))

    for g in range(1):
        print(detail[g].cards, detail[g].points_sum, detail[g].status)
    print("進入投降階段")


    # 逐一詢問玩家是否投降
    for k in range(1):
        print("您的回合")

        # bj 不用投降
        if  translate[str(detail[k].cards[0])] in [10, 11] and translate[str(detail[k].cards[1])] in [10, 11] and\
            translate[str(detail[k].cards[0])] != translate[str(detail[k].cards[1])]:
            detail[k].status = "BLACK JACK"
            print("您獲得BLACK JACK,請等待結果")

        else:
            print("您的牌為:" + str(detail[k].cards[0]) + "和" + str(detail[k].cards[1]))
            detail[k] = Surrender(k, detail)

    print("投降階段結束,接下來進入加牌階段")
    time.sleep(1)

    # for g in range(player):
    #     print(detail[g].cards, detail[g].points_sum, detail[g].status)

    for i in range(1):
        if detail[i].status == "BLACK JACK" or detail[i].status == "已投降":
            pass
        else:
            print("您" + str(i + 1) + "的回合")
            # 希望只出現在該玩家的畫面
            print("您的牌為:" + str(detail[i].cards[0]) + "和" + str(detail[i].cards[1]))
            detail[i] = add_cards(i, detail)

    print("加牌階段結束,接下來進入莊家的回合")

    time.sleep(1)

    # dealer's cards
    if  translate[str(detail[-1].cards[0])] in [10, 11] and translate[str(detail[-1].cards[1])] in [10, 11] and\
        translate[str(detail[-1].cards[0])] != translate[str(detail[-1].cards[1])]:
        detail[-1].status = "BLACK JACK"
        print("莊家的牌：", detail[-1].cards, detail[-1].cards_rank, ",BLACK JACK")
    else:
        while detail[-1].points_sum < 17:
            deal_result = deal_card()
            detail[-1].cards.append(deal_result[0])
            detail[-1].cards_rank.append(deal_result[1])
            detail[-1].points_sum = calculate_points(detail[-1].cards)
        print("莊家的牌：", detail[-1].cards, detail[-1].cards_rank, ",共" + str(detail[-1].points_sum) + "點", sep = '')

    # for g in range(1):
    #     print(detail[g].cards, detail[g].cards_rank, detail[g].points_sum, detail[g].status)
    # print(rank_list)


    print("計算結果中,結果即將揭曉")

    time.sleep(1.8)

    for j in range(1):
        time.sleep(0.2)
        if detail[j].status == "爆":
            print("您點數爆炸，沒收籌碼")
        elif detail[j].status == "過五關":
            if detail[-1].points_sum == 21:
                print("您過五關,但莊家獲得21點,平手,返回全部籌碼")
                chips += detail[j].chips
            else:
                print("您過五關,返回4倍籌碼")
                chips += 4 * detail[j].chips
        elif detail[j].status == "BLACK JACK":
            if detail[-1].status == "BLACK JACK":
                print("您與莊家同時獲得BLACK JACK,平手,返回全部籌碼")
                chips += detail[j].chips
            else:
                print("您獲得BLACK JACK,返回3倍籌碼")
                chips += 3 * detail[j].chips
        elif detail[j].status == "已投降":
            print("您已投降")
        else:
            if detail[-1].status == "BLACK JACK":
                print("莊家獲得BLACK JACK,沒收籌碼")
            elif detail[-1].points_sum > 21:
                print("莊家點數爆炸，返回您的兩倍籌碼")
                chips += 2 * detail[j].chips
            else:
                if detail[j].points_sum > detail[-1].points_sum:
                    print("您的點數比莊家大,返回2倍籌碼")
                    chips += 2 * detail[j].chips
                elif detail[j].points_sum == detail[-1].points_sum:
                    print("您與莊家平手,返回籌碼")
                    chips += detail[j].chips
                else:
                    print("您的點數比莊家小,沒收籌碼")

    reset = ''
    while reset != "gg":
        print(f"您目前的籌碼剩下 {chips}")
        reset = input("輸入 gg 結束遊戲:")
        if reset == 'gg':
            return
        else:
            pve(chips)

# ---------------------------------------------

# player_num = int(input())
player_num = 3
chips_list = []
# for i in range(player_num):
#     if len(chips_list) < player_num:
#         chips_list.append(1000)

def pvp(chips_list = [1000, 1000, 1000]):
    # 玩家總數,最多好像12位可以玩而已

    
    class Player:
        def __init__(self, cards, cards_rank, points_sum, status, chips):
            self.cards = cards
            self.cards_rank = cards_rank
            self.points_sum = points_sum
            self.status = status
            self.chips = chips

    print("pvp")
    print(chips_list)

    cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
    translate = {"J": 10, "Q": 10, "K": 10, "Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
    translate_for_rank = {"J": 10, "Q": 11 , "K": 12, "Ace": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9}
    # 發牌
    rank_list = []
    for k in range(13):
        rank_list.append(["clubs", "diamonds", "hearts", "spades"])

    def deal_card():
        card = random.choice(cards)
        cards.remove(card)
        rank = random.choice(rank_list[translate_for_rank[card]])
        rank_list[translate_for_rank[card]].remove(rank)
        return [card, rank]

    # 算總和來決定ace要當成11還是1
    def calculate_points(cards):
        translate = {"J": 10, "Q": 10, "K": 10, "Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
        points_sum = 0
        for i in range(len(cards)):
            points_sum += translate[cards[i]]

        # points_sum = sum(cards)

        if len(cards) == 2:
            return points_sum

        if points_sum > 21 and "Ace" in cards:
            translate = {"J": 10, "Q": 10, "K": 10, "Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
            points_sum = 0
            for i in range(len(cards)):
                points_sum += translate[cards[i]]

        return points_sum

    detail = []
    def game_start():
        # 發玩家、莊家的牌
        for i in range(player_num + 1):
            playing = Player([], [], 0, 0, 0) 
            deal_result = deal_card()
            playing.cards.append(deal_result[0])
            playing.cards_rank.append(deal_result[1])
            deal_result = deal_card()
            playing.cards.append(deal_result[0])
            playing.cards_rank.append(deal_result[1])
            playing.points_sum = calculate_points(playing.cards)
            detail.append(playing)


        # 如何對每個用戶端印出:您是玩家n or 改為印出'您' 而非 '玩家n' 之類的?
        for i in range(player_num):
            print("玩家" + str(i + 1) + "的明牌：" , detail[i].cards[0], sep = '')
            time.sleep(0.2)
        print(f"莊家的明牌：{detail[-1].cards[0]}")
        return detail

    def Bet(detail, chips_list):
        for i in range(player_num):
            finish = False
            bet = ''
            while not finish:
                try:
                    bet = int(input("輸入您本輪欲下注的金額:"))
                    if bet < 150:
                        print("下注金額不足,請重新下注")
                    elif bet > chips_list[i]:
                        print("下注金額超過您擁有的籌碼,請重新下注")
                    else:
                        finish = True
                        detail[i].chips = bet
                        chips_list[i] -= bet
                except:
                    print("投注失敗,請重新下注")

    def Surrender(k, detail):
        surrender = ""
        while surrender != 'n':
            surrender = input("輸入y投降,輸入n等待其他玩家決定是否投降:")
            # 投降
            if surrender == "y":
                print("玩家" + str(k + 1) + "已投降,返回其一半籌碼")
                detail[k].status = "已投降"
                return detail[k]
            elif surrender == "n":
                return detail[k]
            else:
                print("請重新輸入!")


    # 每個玩家加完牌後才換下一個
    def add_cards(i, detail):
        # 第n個玩家, 第一張牌, 第二張牌
        add_card = ""
        while add_card != "n":
            if len(detail[i].cards) == 5:
                # 過五關
                if detail[i].points_sum <= 21:
                    add_card = "n"
                    detail[i].status = "過五關"
                    return detail[i]
                else:
                    add_card = "n"
                    print("玩家" + str(i + 1) + "的牌：", detail[i].cards, "，共" + str(detail[i].points_sum) + "點", sep = '')

            else:
                add_card = input("輸入y加牌、輸入n不進行加牌並等待其他玩家:")

                if add_card == "y":
                    deal_result = deal_card()
                    detail[i].cards.append(deal_result[0])
                    detail[i].cards_rank.append(deal_result[1])
                    detail[i].points_sum = calculate_points(detail[i].cards)
                    if detail[i].points_sum > 21:
                        add_card = "n"
                        print("玩家" + str(i + 1) + "的牌：", detail[i].cards, "，共" + str(detail[i].points_sum) + "點", sep = '')
                    else:
                        print("玩家" + str(i + 1) + "的牌：", detail[i].cards, "，共" + str(detail[i].points_sum) + "點", sep = '')
                elif add_card == "n":
                    detail[i].points_sum = calculate_points(detail[i].cards)
                    print("玩家" + str(i + 1) + "最終的牌：", detail[i].cards, "，共" + str(detail[i].points_sum) + "點", sep = '')
                else:
                    print("請重新輸入!")

        if detail[i].points_sum > 21:
            detail[i].status = "爆"
            return detail[i]
        else:
            detail[i].status = 0
            return detail[i]


    # 主程式，遊戲開始

    print("正在發牌,請稍後")
    time.sleep(1)

    detail = game_start()

    Bet(detail, chips_list)
    print(chips_list)

    for g in range(player_num):
        print(detail[g].cards, detail[g].points_sum, detail[g].status)
    print("進入投降階段")


    # 逐一詢問玩家是否投降
    for k in range(player_num):
        print("玩家" + str(k + 1) + "的回合")
        # 希望只出現在該玩家的畫面

        # bj 不用投降
        if  translate[str(detail[k].cards[0])] in [10, 11] and translate[str(detail[k].cards[1])] in [10, 11] and\
            translate[str(detail[k].cards[0])] != translate[str(detail[k].cards[1])]:
            detail[k].status = "BLACK JACK"
            print("您獲得BLACK JACK,請等待結果")

        else:
            print("您的牌為:" + str(detail[k].cards[0]) + "和" + str(detail[k].cards[1]))
            detail[k] = Surrender(k, detail)

    print("投降階段結束,接下來進入加牌階段")
    time.sleep(1)

    # for g in range(player):
    #     print(detail[g].cards, detail[g].points_sum, detail[g].status)

    for i in range(player_num):
        if detail[i].status == "BLACK JACK" or detail[i].status == "已投降":
            pass
        else:
            print("玩家" + str(i + 1) + "的回合")
            # 希望只出現在該玩家的畫面
            print("您的牌為:" + str(detail[i].cards[0]) + "和" + str(detail[i].cards[1]))
            detail[i] = add_cards(i, detail)

    print("加牌階段結束,接下來進入莊家的回合")

    time.sleep(1)

    # dealer's cards
    if  translate[str(detail[-1].cards[0])] in [10, 11] and translate[str(detail[-1].cards[1])] in [10, 11] and\
        translate[str(detail[-1].cards[0])] != translate[str(detail[-1].cards[1])]:
        detail[-1].status = "BLACK JACK"
        print("莊家的牌：", detail[-1].cards, ",BLACK JACK")
    else:
        while detail[-1].points_sum < 17:
            deal_result = deal_card()
            detail[-1].cards.append(deal_result[0])
            detail[-1].cards_rank.append(deal_result[1])
            detail[-1].points_sum = calculate_points(detail[-1].cards)
        print("莊家的牌：", detail[-1].cards, ",", detail[-1].cards_rank, ",共" + str(detail[-1].points_sum) + "點", sep = '')

    for g in range(player_num):
        print(detail[g].cards, detail[g].cards_rank, detail[g].points_sum, detail[g].status)


    print("計算結果中,結果即將揭曉")

    time.sleep(1.8)

    for j in range(player_num):
        time.sleep(0.2)
        if detail[j].status == "爆":
            print("玩家" + str(j + 1) + "點數爆炸，沒收籌碼")
        elif detail[j].status == "過五關":
            if detail[-1].points_sum == 21:
                print("玩家" + str(j + 1) + "過五關,但莊家獲得21點,平手,返回全部籌碼")
                chips_list[j] += detail[j].chips
            else:
                print("玩家" + str(j + 1) + "過五關,返回4倍籌碼")
                chips_list[j] += 4 * detail[j].chips
        elif detail[j].status == "BLACK JACK":
            if detail[-1].status == "BLACK JACK":
                print("玩家" + str(j + 1) + "與莊家同時獲得BLACK JACK,平手,返回全部籌碼")
                chips_list[j] += detail[j].chips
            else:
                print("玩家" + str(j + 1) + "獲得BLACK JACK,返回3倍籌碼")
                chips_list[j] += 3 * detail[j].chips
        elif detail[j].status == "已投降":
            print("玩家" + str(j + 1) + "已投降")
        else:
            if detail[-1].status == "BLACK JACK":
                print("莊家獲得BLACK JACK,沒收籌碼")
            elif detail[-1].points_sum > 21:
                print("莊家點數爆炸，返回玩家" + str(j + 1) + " 的籌碼")
                chips_list[j] += detail[j].chips
            else:
                if detail[j].points_sum > detail[-1].points_sum:
                    print("玩家" + str(j + 1) + "的點數比莊家大,返回2倍籌碼")
                    chips_list[j] += 2 * detail[j].chips
                elif detail[j].points_sum == detail[-1].points_sum:
                    print("玩家" + str(j + 1) + "與莊家平手,返回籌碼")
                    chips_list[j] += detail[j].chips
                else:
                    print("玩家" + str(j + 1) + "的點數比莊家小,沒收籌碼")
    reset = ''
    while reset != "gg":
        print("您目前的籌碼剩下" + str(chips_list))
        reset = input("輸入 gg 結束遊戲:")
        if reset == 'gg':
            return
        else:
            chips_list = pvp(chips_list)

    return chips_list






# ---------------------------------------------


# 匯入pygame
import pygame as pg
import button as BT
# import pve
# import pvp

# pygame初始化
pg.init()

scale = 1.5

# 設定視窗
width, height =  590, 410   
button_width, button_height = 200, 100# 遊戲畫面寬和高
screen = pg.display.set_mode((width*scale, height*scale))                      # 依設定顯示視窗
pg.display.set_caption("Welcome to the Black Jack game")           # 設定程式標題

# 建立畫布bg
bg = pg.Surface(screen.get_size())
bg = bg.convert()


image_surface = pg.image.load("./image/openpage.PNG").convert()
image_new = pg.transform.scale(image_surface,(width, height))
image_1 = pg.transform.rotozoom(image_new,0,scale)
screen.blit(image_1,(0,0))

buttons = []

PVE_button = BT.button(button_width, button_height, (400, 350), ".\image\pve_black.jpg", ".\image\pve_black.jpg", True, pve)
buttons.append(PVE_button)

PVP_button = BT.button(button_width, button_height, (640, 350), ".\image\pvp_black.jpg", ".\image\pvp_black.jpg", True, pvp)
buttons.append(PVP_button)

# bet_button = BT.button(button_width, button_height, (640, 350), ".\image\bet_up.png", ".\image\bet_down.png", False, pvp)
# buttons.append(bet_button)

# hit_button = BT.button(button_width, button_height, (640, 350), ".\image\hit_up.png", ".\image\hit_down.png", False, pvp)
# buttons.append(hit_button)



print(buttons)

for button in buttons:
    screen.blit(button.button_image[0], button.pos)

running = True

while running:
    mouse_x, mouse_y = pg.mouse.get_pos()
        
    for button in buttons:
        if button.pos[0] < mouse_x < button.pos[0] + button.width and button.pos[1] < mouse_y < button.pos[1] + button.height:
            screen.blit(button.button_image[0], button.pos)
            
        else:
            screen.blit(button.button_image[0], button.pos)
    
    event = pg.event.wait()
    if event.type == pg.QUIT:
        running = False
            
    elif event.type == pg.MOUSEBUTTONDOWN:
        for button in buttons:
            if button.pos[0] < mouse_x < button.pos[0] + button.width and button.pos[1] < mouse_y < button.pos[1] + button.height:
                screen.blit(button.button_image[1], button.pos)
                button.func()
                    
    for button in buttons:
        screen.blit(button.button_image[0], button.pos)
                
        
    pg.display.update()
            



# if __name__ == '__main__':
#     reset = ''
#     chips_list = pvp(chips_list)
#     while reset != 'gg':
#         print(chips_list)
#         reset = input("輸入 gg 結束遊戲:")
#         if reset == 'gg':
#             break
#         else:
#             reset = ''
#             pvp(chips_list)


            
pg.quit()   
