import pygame as pg


def CardRender(screen, detail, sequence_card, sequence_player):
    card_image = pg.image.load("./image/"+detail[sequence_player].cards[sequence_card]+'_'+detail[sequence_player].cards_rank[sequence_card]+'_white.png')
    card_image = pg.transform.scale(card_image,(60,84))
    if detail[sequence_player] == detail[-1]:
        screen.blit(card_image,(250, 200))
    else: 
        screen.blit(card_image,(250 + 50 * sequence_player, 100))