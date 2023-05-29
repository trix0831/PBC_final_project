import pygame as pg

card_squence = []

def CardRender(detail, sequence_card, sequence_player, screen):
    
    card_image = pg.image.load("./image/"+detail[sequence_player].cards[sequence_card]+'_'+detail[sequence_player].cards_rank[sequence_card]+'_white.png')
    card_image = pg.transform.scale(card_image,(90,126))
    
    if detail[sequence_player] == detail[-1]:
        screen.blit(card_image,(233 + sequence_card*90, 38))
    elif sequence_player == 0: 
        screen.blit(card_image,(233 + sequence_card*90, 398))
    # elif sequence_player == 1: 
    #     card_image = pg.transform.rotozoom(card_image,90,1)
    #     screen.blit(card_image,(495 , 65 + sequence_card*60))
    # elif sequence_player == 2: 
    #     card_image = pg.transform.rotozoom(card_image,90,1)
    #     screen.blit(card_image,(25 , 65 + sequence_card*60))