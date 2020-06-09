from matplotlib import pyplot as plt
from copy import copy

def show_all_hands(three_players):
    """Shows the hands of three players (all cards facing the camera).

    Args:
        three_players (list of Player): The three players whose hands are to be shown.
    """
        #for now I'll assume 3 players
    fig,ax = plt.subplots(figsize=(16,9))

    cardext = [600,800,0,300]
    all_images = []
    for card in three_players[0].hand.cards:
        all_images.append(ax.imshow(card.image,origin = 'upper',extent = copy(cardext),alpha=1))
        cardext[0] = cardext[0]+50
        cardext[1] = cardext[1]+50
        #input(card.name)
        #print(cardext)
    #[print(card.name) for card in three_players[0].hand.cards]

    cardext = [0,200,700,1000]
    for card in three_players[1].hand.cards:
        all_images.append(ax.imshow(card.image,origin = 'upper',extent = copy(cardext),alpha = 1))
        cardext[0] = cardext[0]+50
        cardext[1] = cardext[1]+50
    #[print(card.name) for card in three_players[1].hand.cards]

    cardext = [1150,1350,700,1000]
    for card in three_players[2].hand.cards:
        all_images.append(ax.imshow(card.image,origin = 'upper',extent = copy(cardext),alpha = 1))
        cardext[0] = cardext[0]+50
        cardext[1] = cardext[1]+50
    #[print(card.name) for card in three_players[2].hand.cards]

    ax.set_xlim(0,2000)
    ax.set_ylim(0,1000)
    plt.show(block=False)
