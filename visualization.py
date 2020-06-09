from matplotlib import pyplot as plt
from copy import copy
from time import sleep

def show_table_omniscient(three_players,discard_pile,full_deck,fig,ax):
    ax.clear()
    first_card_positions = [[600,800,0,300],[0,200,700,1000],[1150,1350,700,1000]] 
    username_positions= [[600,310],[20,670],[1150,670]]
    # TODO: Extend previous lines to work with arbitrary number of players.
    ax.set_xlim(0,2000)
    ax.set_ylim(0,1000)
    plt.show(block=False)
    #Showing player cards
    for initial_position,player in zip(first_card_positions,three_players):
        cardext = copy(initial_position)
        all_images = []
        for card in player.hand.cards:
            all_images.append(ax.imshow(card.image,origin = 'upper',extent = copy(cardext),alpha=1))
            cardext[0] = cardext[0]+50
            cardext[1] = cardext[1]+50
    #Including player usernames
    for user_spot,username in zip(username_positions,[player.id for player in three_players]):
        ax.text(user_spot[0],user_spot[1],username)
    #Including discard top card
    ax.imshow(discard_pile.cards[-1].image,origin = 'upper',extent = [1000,1100,400,550])
    ax.text(1000,570,'Discard')
    ax.text(750,500,'Live Deck')
    fig.canvas.draw()


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
