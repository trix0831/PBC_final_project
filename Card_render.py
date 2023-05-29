import pygame as pg


def CardRender(detail, sequence_card, sequence_player):
    card_image = pg.image.load("./image/"+detail[sequence_player].cards[sequence_card]+'_'+detail[sequence_player].cards_rank[sequence_card]+'_white.png')
    card_image = pg.transform.scale(card_image,(60,84))
    if detail[sequence_player] == detail[-1]:
        screen.blit(card_image,(250, 200))
    else: 
        screen.blit(card_image,(250 + 50 * sequence_player, 100))

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

CardRender(("7","club",0,0,0),(5),(2))
