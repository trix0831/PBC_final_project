import random
import time

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

# 發牌
def deal_card():
    card = random.choice(cards)
    cards.remove(card)
    return card

# 算總和來決定ace要當成11還是1
def calculate_points(cards):
    points_sum = sum(cards)

    if len(cards) == 2:
        return points_sum

    if points_sum > 21:
        if 11 in cards:
            cards.insert(int(cards.index(11)), 1)
            cards.remove(11)
            points_sum = sum(cards)

    return points_sum

# 玩家總數,最多好像12位可以玩而已
player = int(input())

def game_start():
    all_cards = []

    for _ in range(2 * player + 2):
        all_cards.append(deal_card())

    # 如何對每個用戶端印出:您是玩家n or 改為印出'您' 而非 '玩家n' 之類的?
    for i in range(player):
        print("玩家" + str(i + 1) + "的明牌：" , all_cards[int(2 * i)], sep = '')
        time.sleep(0.2)
    print(f"莊家的明牌：{all_cards[-1]}")
    return all_cards

temp_result = {}

def surrender(n, x, y):
    # 第n個玩家, 第一張牌, 第二張牌
    player_cards = [x, y]
    surrender = ""
    while surrender != 'n':
        surrender = input("輸入y投降,輸入n等待其他玩家決定是否投降:")
        # 投降
        if surrender == "y":
            print("玩家" + str(n + 1) + "已投降,返回其一半籌碼")
            temp_result[str(n + 1)] = "已投降"
            return "已投降"
        elif surrender == "n":
            return 
        else:
            print("請重新輸入!")


# 每個玩家加完牌後才換下一個
def add_cards(n, x, y):
    # 第n個玩家, 第一張牌, 第二張牌
    player_cards = [x, y]
    add_card = ""
    while add_card != "n":
        if len(player_cards) == 5:
            # 過五關
            if player_points <= 21:
                player_points = 21
                add_card = "n"
                # print("玩家" + str(n) + "的牌：", player_cards, "，共" + str(player_points) + "點", sep = '')
                return "過五關"
            else:
                add_card = "n"
                print("玩家" + str(n + 1) + "的牌：", player_cards, "，共" + str(player_points) + "點", sep = '')

        else:
            add_card = input("輸入y加牌、輸入n不進行加牌並等待其他玩家:")

            if add_card == "y":
                player_cards.append(deal_card())
                player_points = calculate_points(player_cards)
                if player_points > 21:
                    add_card = "n"
                    print("玩家" + str(n + 1) + "的牌：", player_cards, "，共" + str(player_points) + "點", sep = '')
                else:
                    print("玩家" + str(n + 1) + "的牌：", player_cards, "，共" + str(player_points) + "點", sep = '')
            elif add_card == "n":
                player_points = calculate_points(player_cards)
                print("玩家" + str(n + 1) + "最終的牌：", player_cards, "，共" + str(player_points) + "點", sep = '')
            else:
                print("請重新輸入!")

    if player_points > 21:
        return "爆"
    else:
        return  str(player_points)


# 主程式，遊戲開始

print("正在發牌,請稍後")
time.sleep(1.5)

all_cards = game_start()

print("進入投降階段")


# 逐一詢問玩家是否投降
for k in range(player):
    print("玩家" + str(k + 1) + "的回合")
    # 希望只出現在該玩家的畫面

    # bj 不用投降
    if  all_cards[int(2 * k)] in [10, 11] and all_cards[int(2 * k + 1)] in [10, 11] and all_cards[int(2 * k)] != all_cards[int(2 * k + 1)]:
        temp_result[str(k + 1)] = "BLACK JACK"
        print("您獲得BLACK JACK,請等待結果")
    else:
        print("您的牌為:" + str(all_cards[int(2 * k)]) + "和" + str(all_cards[int(2 * k + 1)]))
        surrender(k, all_cards[int(2 * k)], all_cards[int(2 * k + 1)])

print("投降階段結束,接下來進入加牌階段")
time.sleep(1)
result = {}

for i in range(player):
    try:
        if temp_result[str(i + 1)] == "BLACK JACK":
            result["玩家" + str(i + 1)] = "BLACK JACK"
        elif temp_result[str(i + 1)] == "已投降":
            result["玩家" + str(i + 1)] = "已投降"
    except:
        print("玩家" + str(i + 1) + "的回合")
        # 希望只出現在該玩家的畫面
        print("您的牌為:" + str(all_cards[int(2 * i)]) + "和" + str(all_cards[int(2 * i + 1)]))

        # bj的話不用進行加牌
        if all_cards[int(2 * i)] in [10, 11] and all_cards[int(2 * i + 1)] in [10, 11] and all_cards[int(2 * i)] != all_cards[int(2 * i + 1)]:
            result["玩家" + str(i + 1)] = "BLACK JACK"
        else:
            result["玩家" + str(i + 1)] = str(add_cards(i, all_cards[int(2 * i)], all_cards[int(2 * i + 1)]))

print("加牌階段結束,接下來進入莊家的回合")

time.sleep(2)

# dealer's cards
dealer_cards = [all_cards[-1], all_cards[-2]]
# dealer_cards = [10, 11]
dealer_points = calculate_points(dealer_cards)
dealer_bj = False
if dealer_cards[0] in [10, 11] and dealer_cards[1] in [10, 11] and dealer_cards[0] != dealer_cards[1]:
    print("莊家的牌：", dealer_cards, ",BLACK JACK")
    dealer_bj = True
else:
    while dealer_points < 17:
        dealer_cards.append(deal_card())
        dealer_points = calculate_points(dealer_cards)
    print("莊家的牌：", dealer_cards, ",共" + str(dealer_points) + "點", sep = '')

# print(result)

time.sleep(0.5)

print("計算結果中,結果即將揭曉")

time.sleep(1.8)

for j in range(player):
    time.sleep(0.2)
    if list(result.values())[j] == "爆":
        print("玩家" + str(j + 1) + "點數爆炸，沒收籌碼")
    elif list(result.values())[j] == "過五關":
        if dealer_points == 21:
            print("玩家" + str(j + 1) + "過五關,但莊家獲得21點,平手,返回全部籌碼")
        else:
            print("玩家" + str(j + 1) + "過五關,返回3倍籌碼")
    elif list(result.values())[j] == "BLACK JACK":
        if dealer_bj:
            print("玩家" + str(j + 1) + "與莊家同時獲得BLACK JACK,平手,返回全部籌碼")
        else:
            print("玩家" + str(j + 1) + "獲得BLACK JACK,返回2.5倍籌碼")
    elif list(result.values())[j] == "已投降":
        print("玩家" + str(j + 1) + "已投降")
    else:
        if dealer_bj:
            print("莊家獲得BLACK JACK,沒收籌碼")
        elif dealer_points > 21:
            print("莊家點數爆炸，返回 玩家" + str(j + 1) + " 的籌碼")
        else:
            if int(list(result.values())[j]) > dealer_points:
                print("玩家" + str(j + 1) + "的點數比莊家大,返回2倍籌碼")
            elif int(list(result.values())[j]) == dealer_points:
                print("玩家" + str(j + 1) + "與莊家平手,返回籌碼")
            else:
                print("玩家" + str(j + 1) + "的點數比莊家小,沒收籌碼")
