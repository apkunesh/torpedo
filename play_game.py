import pandas as pd
from matplotlib.pyplot import imread as image_reader
from matplotlib import pyplot as plt
from playing_cards import Deck, Card, CardGroup, Multideck, DiscardPile
from numpy.random import randint
from turn_management import player_turn, Player
from visualization import show_all_hands, show_table_omniscient
from time import sleep

n_players = 3


n_decks = 2
rounds = ['Two Books','Two Runs','Two Runs And A Book','Two Books And A Run','Three Books','Three Runs']


def establish_players(n_players):
    """Gets player information for display and reference. 

    Eventually should include getting the players' IP addresses etc
    for online connectivity

    Args:
        n_players (int): The number of players to place in the game

    Returns:
        dict: A dictionary of user information, such as username
    """
    usernames_out = [input('Please input a username for player ' +str(i)) for i in range(n_players)]
    return {'username':usernames_out}

def refresh_all_players(all_players):
    """Sets all players to the "default" state before a round begins.

    Args:
        all_players (list of Player): The players in your game of Torpedo
    """
    for player in all_players:
        player.locked_actions = player.available_actions
        player.available_actions = []
        player.hand = CardGroup()
        player.is_down = False
        player.buy_count = 0
        #update screens here to show the locking.

def deal(list_of_Player, Multideck,dealer_index):
    """Deals 9 cards to each player.

    Args:
        list_of_Player (list of Player): The players of your game of Torpedo
        Multideck (Multideck): The central "drawing" deck
        dealer_index (int): The index of the round's dealer, used to establish player order.

    Returns:
        int: The index of the next dealer.
    """
    for i in range(9):
        [player.hand.cards.append(Multideck.draw_top()) for player in list_of_Player]
    dealer_index = (dealer_index+1) % len(list_of_Player)
    return dealer_index


#def player_turn(whose_turn):

def is_round_over():
    """Check, to be used at the end of each player turn, to see if the round is complete.

    True if the most recent player discarded their final card and now has 0 cards.
    False otherwise (allowing for the game to continue even if the player has 0 cards).

    Returns:
        Bool: Confirms or denies the end of the round.
    """
    return False

def assign_points(players):
    """Penalizes players with points after the end of a round.

    Args:
        players (list of Player): The players of your game of Torpedo.
    """
    pass

def display_results():
    """Displays the scores and congratulates the winner.
    """
    pass

players_info = establish_players(n_players)
players = [Player(usernameboi) for usernameboi in players_info['username']]
all_points = []
dealer_index = 0
fig,ax = plt.subplots(figsize=(16,9))

fig.canvas.draw_idle()
for round_descriptor in rounds:
    discard_pile = DiscardPile()
    refresh_all_players(players)
    round_over = False
    full_deck = Multideck(n_decks)
    whose_turn = (dealer_index+1) % len(players)
    dealer_index = deal(players, full_deck,dealer_index)
    print(round_descriptor)
    print('You have 15 seconds to organize your hand.')
    sleep(1) #Change to 15 eventually
    discard_pile.discard(full_deck.draw_top())
    while round_over == False:
        show_table_omniscient(players,discard_pile,full_deck,fig,ax)
        #input(players[0].hand.cards[0].name)
        #show_all_hands(players)
        player_turn(whose_turn,players,full_deck,round_descriptor,discard_pile)
        round_over = is_round_over()
        whose_turn = (whose_turn+1) % len(players) 
    assign_points()
display_results()



'''
my_deck = Deck()
[print(card.name) for card in my_deck.cards]
'''