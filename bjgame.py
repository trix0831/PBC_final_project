import random
import time
import player


cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
translate = {"J": 10, "Q": 10, "K": 10, "Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}

# 發牌
def deal_card():
    card = random.choice(cards)
    cards.remove(card)
    return card

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

# 玩家總數,最多好像12位可以玩而已
player_num = int(input())

detail = []
def game_start():
    # 發玩家、莊家的牌
    for i in range(player_num + 1):
        playing = player.Player([], 0, 0) 
        playing.cards.append(deal_card())
        playing.cards.append(deal_card())
        playing.points_sum = calculate_points(playing.cards)
        detail.append(playing)


    # 如何對每個用戶端印出:您是玩家n or 改為印出'您' 而非 '玩家n' 之類的?
    for i in range(player_num):
        print("玩家" + str(i + 1) + "的明牌：" , detail[i].cards[0], sep = '')
        time.sleep(0.2)
    print(f"莊家的明牌：{detail[-1].cards[0]}")
    return detail

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
                detail[i].cards.append(deal_card())
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
        detail[-1].cards.append(deal_card())
        detail[-1].points_sum = calculate_points(detail[-1].cards)
    print("莊家的牌：", detail[-1].cards, ",共" + str(detail[-1].points_sum) + "點", sep = '')

# for g in range(player):
#     print(detail[g].cards, detail[g].points_sum, detail[g].status)


print("計算結果中,結果即將揭曉")

time.sleep(1.8)

for j in range(player_num):
    time.sleep(0.2)
    if detail[j].status == "爆":
        print("玩家" + str(j + 1) + "點數爆炸，沒收籌碼")
    elif detail[j].status == "過五關":
        if detail[-1].points_sum == 21:
            print("玩家" + str(j + 1) + "過五關,但莊家獲得21點,平手,返回全部籌碼")
        else:
            print("玩家" + str(j + 1) + "過五關,返回3倍籌碼")
    elif detail[j].status == "BLACK JACK":
        if detail[-1].status == "BLACK JACK":
            print("玩家" + str(j + 1) + "與莊家同時獲得BLACK JACK,平手,返回全部籌碼")
        else:
            print("玩家" + str(j + 1) + "獲得BLACK JACK,返回2.5倍籌碼")
    elif detail[j].status == "已投降":
        print("玩家" + str(j + 1) + "已投降")
    else:
        if detail[-1].status == "BLACK JACK":
            print("莊家獲得BLACK JACK,沒收籌碼")
        elif detail[-1].points_sum > 21:
            print("莊家點數爆炸，返回 玩家" + str(j + 1) + " 的籌碼")
        else:
            if detail[j].points_sum > detail[-1].points_sum:
                print("玩家" + str(j + 1) + "的點數比莊家大,返回2倍籌碼")
            elif detail[j].points_sum == detail[-1].points_sum:
                print("玩家" + str(j + 1) + "與莊家平手,返回籌碼")
            else:
                print("玩家" + str(j + 1) + "的點數比莊家小,沒收籌碼")


# print(cards)

