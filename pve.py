# 匯入pygame
import pygame as pg
import button as BT
import random
import time
import sys
import Card_render as CR

pg.init()

font = pg.font.SysFont("Times new roman", 30)

global screen
global width
global height
global detail


chips = 1000
reset = ''
width, height =  600, 420


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

cards = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"] * 4
translate = {"jack": 10, "queen": 10, "king": 10, "ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
translate_for_rank = {"jack": 10, "queen": 11 , "king": 12, "ace": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9}

# 發牌
def deal_card():
    card = random.choice(cards)
    cards.remove(card)
    rank = random.choice(rank_list[translate_for_rank[card]])
    rank_list[translate_for_rank[card]].remove(rank)
    return [card, rank]

# 算總和來決定ace要當成11還是1
def calculate_points(cards):
    translate = {"jack": 10, "queen": 10, "king": 10, "ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
    points_sum = 0
    for i in range(len(cards)):
        points_sum += translate[cards[i]]

    # points_sum = sum(cards)

    if len(cards) == 2:
        return points_sum

    if points_sum > 21 and "Ace" in cards:
        translate = {"jack": 10, "queen": 10, "king": 10, "ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
        points_sum = 0
        for i in range(len(cards)):
            points_sum += translate[cards[i]]

    return points_sum

# 發牌
def game_start():
    global screen
    detail = []
    
    # 發玩家、莊家的牌
    for i in range(2):
        playing = Player([], [], 0, "0", 0) 
        playing.status = "0"
        
        deal_result = deal_card()
        
        playing.cards.append(deal_result[0])
        playing.cards_rank.append(deal_result[1])
        
        deal_result = deal_card()
        
        playing.cards.append(deal_result[0])
        playing.cards_rank.append(deal_result[1])
        playing.points_sum = calculate_points(playing.cards)
        
        detail.append(playing)

    return detail

# 下注
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

def table():
    global detail
    
    screen.fill((13, 96, 0))
    
    print(len(detail[0].cards), len(detail[1].cards))
    
    for i_sp_1 in range(2):
        for i_sc_1 in range(len(detail[i_sp_1].cards)):            
            CR.CardRender(detail, i_sc_1, i_sp_1, screen)
            
    pg.display.update()
    

# 投降
def Surrender():
    global detail
    global buttons
    
    table()
    renderText("Surrender already, gg", (250, 250))
    pg.display.update()
    detail[0].points_sum = calculate_points(detail[0].cards)
    
    detail[0].status = "已投降"
    
    buttons = []
    
    return detail[0]


# 每個玩家加完牌後才換下一個
def add_cards(jjingg):
    global detail
    global screen
    
    # 第n個玩家, 第一張牌, 第二張牌
    if len(detail[jjingg].cards) == 5:
        # 過五關
        if detail[jjingg].points_sum <= 21:
            detail[jjingg].status = "過五關"
            
            renderText("過五關", (300, 300))
            time.sleep(1)
            
            end()
            # return detail
        
        else:
            renderText("U have " + str(detail[jjingg].cards) + "points.", (300, 250))
            
    else:
        deal_result = deal_card()
        print('shit')
        
        detail[jjingg].cards.append(deal_result[0])
        detail[jjingg].cards_rank.append(deal_result[1])   
        
        CR.CardRender(detail, len(detail[jjingg].cards) - 1, 0, screen)
        print(detail[jjingg].cards)
        
        # detail[jjingg].points_sum = calculate_points(detail[jjingg].cards)
        
        if calculate_points(detail[jjingg].cards) > 21:
            detail[jjingg].status = "爆"
            
            renderText("boooooooom", (300, 300))
            time.sleep(1)
            
            end()
            return detail
        else:
            pass


def execute_loop_buttons():
    global buttons
    
    excute_index = -1
    
    running = True
    
    while running:
        mouse_x, mouse_y = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            try:
                for button in buttons:
                    if button.pos[0] < mouse_x < button.pos[0] + button.width and button.pos[1] < mouse_y < button.pos[1] + button.height:
                        screen.blit(button.button_image[1], button.pos)
                    else:
                        screen.blit(button.button_image[0], button.pos)
                    
                if event.type == pg.MOUSEBUTTONUP:
                    for button_index in range(len(buttons)):
                        if buttons[button_index].pos[0] < mouse_x < buttons[button_index].pos[0] + buttons[button_index].width and buttons[button_index].pos[1] < mouse_y < buttons[button_index].pos[1] + buttons[button_index].height:
                            excute_index = button_index
                            running = False
                            
            except:
                pass
                        
            pg.display.update()
            
    return excute_index

def execute_loop_input(aaa):
    # 設定字體和文字
    font = pg.font.SysFont("Times new roman", 30)
    text = font.render(aaa, True, (255, 255, 255))

    # 設定輸入框
    input_box = pg.Rect(250, 300, 300, 50)
    input_text = ""
    max_length = 10

    running = True


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
            elif event.type == pg.KEYDOWN:
                if event.unicode.isprintable() and len(input_text) < max_length:
                    input_text += event.unicode
                
                elif event.key == pg.K_BACKSPACE:
                    input_text = input_text[:-1]
                
                elif event.key == pg.K_RETURN:
                    running = False

        # 畫出文字和輸入框
        pg.draw.rect(screen, (255, 255, 255), input_box)
        text_width, text_height = font.size("Please enter username (only English and numbers):")
        screen.blit(text, ((width - text_width) // 2 + 100, input_box.y - text_height - 20))
        pg.draw.rect(screen, (255, 255, 255), input_box, 2)

        # 畫出輸入的文字
        text_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        # 檢查是否超過字數限制
        if len(input_text) >= max_length:
            text_surface = font.render("Max length reached", True, (255, 0, 0))
            screen.blit(text_surface, (290  , input_box.y + 70))

        pg.display.update()
        
    return input_text

def renderText(str, pos):
    global screen
    
    text = font.render(str, True, (255, 255, 255))
    screen.blit(text, pos)
    pg.display.update()
    
def mega_add():
    global detail
    global buttons
    
    for i in range(1):
        detail[i] = add_cards(i)
        
        running = True

        while running:
            mouse_x, mouse_y = pg.mouse.get_pos()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
                try:
                    for button in buttons:
                        if button.pos[0] < mouse_x < button.pos[0] + button.width and button.pos[1] < mouse_y < button.pos[1] + button.height:
                            screen.blit(button.button_image[1], button.pos)
                        else:
                            screen.blit(button.button_image[0], button.pos)
                    
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if buttons[0].pos[0] < mouse_x < buttons[0].pos[0] + buttons[0].width and buttons[0].pos[1] < mouse_y < buttons[0].pos[1] + buttons[0].height:
                            detail = add_cards(i)
                            
                        if buttons[1].pos[0] < mouse_x < buttons[1].pos[0] + buttons[1].width and buttons[1].pos[1] < mouse_y < buttons[1].pos[1] + buttons[1].height:
                            running = False
                                
                except:
                    pass
                            
                pg.display.update()
                
            # print(detail[i].status)
            
            # if detail[i].status == "爆" or detail[i].status == "過五關":
            #     running = False
            
    
def mega_not_add():
    global detail
    global buttons
    
    table()
    for i_sp_1 in range(2):
        for i_sc_1 in range(2):
            CR.CardRender(detail, i_sp_1, i_sc_1, screen)
    pg.display.update()
    detail[0].points_sum = calculate_points(detail[0].cards)
    
    buttons = []
    
    
def end():
    global detail
    
    running = True
    print(detail[0].cards, detail[1].cards)
    
    table()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                
    pg.quit()
    sys.exit()

# 主程式，遊戲開始
def pve(chips = 1000):
    global screen
    global buttons
    global width
    global height
    global detail
    
    buttons = []
    excute_func = -1

    # pygame初始化
    pg.init()
    scale = 1.5

    # 設定視窗   
    screen = pg.display.set_mode((width*scale, height*scale))  # 依設定顯示視窗
    pg.display.set_caption("Welcome to the Black Jack game")  # 設定程式標題


    image_surface = pg.image.load("./image/game_background.PNG").convert() ##
    image_new = pg.transform.scale(image_surface,(width, height))
    image_1 = pg.transform.rotozoom(image_new,0,scale)
    screen.blit(image_1,(0,0))

    print("pve")
    detail = []


    
    print("正在發牌,請稍後")
    renderText("WAIT!!! IDIOT", (100,50))
    time.sleep(0.5)

    screen.fill((13,96, 0))
    pg.display.update()

    detail = game_start()
    
    for person in detail:
        person.status = "0"
    
    t = execute_loop_input("Please enter username (only English and numbers):")
    print(t)
    
    screen.blit(image_1,(0,0))
    # excute_func = excute_loop_buttons()
    
    # if excute_func != -1:
    #     buttons[excute_func].func()
    
    


    # chips = Bet(detail, chips)
    # screen.blit(image_1,(0,0))
    screen.fill((13,96, 0))
    pg.display.update()

    time.sleep(0.5)

    conti = True
    while conti:
        try:
            bet_num = int(execute_loop_input("Please enter ur bet:"))
            if bet_num > chips:
                renderText("Wrong!!!", (300, 300))
            else:
                chips -= bet_num
                conti = False
        except:
            renderText("Wrong!!!", (150, 50))


    screen.fill((13,96, 0))
    pg.display.update()
    
    renderText("Your chips left:" + str(chips), (500, 40))
    print("您目前的籌碼剩餘:" + str(chips))

    print("進入投降階段")
    renderText("Surrender Phase Let's Go", (500, 10))

    for i_sp_1 in range(2):
        for i_sc_1 in range(2):
            CR.CardRender(detail, i_sp_1, i_sc_1, screen)

    # 逐一詢問玩家是否投降
    for k in range(1):
        print("您的回合")
        renderText("Your turn!!!", (50, 200))

        # bj 不用投降
        if  translate[str(detail[k].cards[0])] in [10, 11] and translate[str(detail[k].cards[1])] in [10, 11] and\
            translate[str(detail[k].cards[0])] != translate[str(detail[k].cards[1])]:
            detail[k].status = "BLACK JACK"
            print("您獲得BLACK JACK,請等待結果")
            renderText("U got a BJ!!!", (350, 200))

        else:
            print("您的牌為:" + str(detail[k].cards[0]) + "和" + str(detail[k].cards[1]))
            # detail[k] = Surrender()

    print("投降階段結束,接下來進入加牌階段")
    renderText("End of surrounding phase, now adding phase!!!", (350, 200))
    time.sleep(0.5)


    table()

    button_width, button_height = 200, 100
    Hit_button = BT.button(button_width, button_height, (180, 533), ".\image\hit_up.png", ".\image\hit_down.png", True, mega_add)
    buttons.append(Hit_button)

    Stand_button = BT.button(button_width, button_height, (390, 533), ".\image\stand_up.png", ".\image\stand_down.png", True, mega_not_add)
    buttons.append(Stand_button)

    Surrender_button = BT.button(button_width, button_height, (600, 533), ".\image\surrender_up.png", ".\image\surrender_down.png", True, Surrender)
    buttons.append(Surrender_button)
    
    for button in buttons:
        screen.blit(button.button_image[0], button.pos)
            
    pg.display.update()
    
    excute_func = execute_loop_buttons()
    
    if excute_func != -1:
        buttons[excute_func].func()


    print("加牌階段結束,接下來進入莊家的回合")
    renderText("End of adding's phase, dealer's turn.", (350, 200))

    time.sleep(1)

    # dealer's cards
    if  translate[str(detail[-1].cards[0])] in [10, 11] and translate[str(detail[-1].cards[1])] in [10, 11] and\
        translate[str(detail[-1].cards[0])] != translate[str(detail[-1].cards[1])]:
        detail[-1].status = "BLACK JACK"
        renderText("Dealer got a BJ!!!", (300, 150))
        print("莊家的牌：", detail[-1].cards, detail[-1].cards_rank, ",BLACK JACK")
    else:
        while detail[-1].points_sum < 17:
            deal_result = deal_card()
            detail[-1].cards.append(deal_result[0])
            detail[-1].cards_rank.append(deal_result[1])
            detail[-1].points_sum = calculate_points(detail[-1].cards)
        renderText("Dealer got " + str(detail[-1].cards) + "points.", (300, 150))
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

    # reset = ''
    # while reset != "gg":
    #     print(f"您目前的籌碼剩下 {chips}")
    #     reset = input("輸入 gg 結束遊戲:")
    #     if reset == 'gg':
    #         return
    #     else:
    #         pve(chips)
    end()


if __name__ == '__main__' and reset != 'gg':
    pve(chips)