import pandas as pd
from matplotlib.pyplot import imread as image_reader
from matplotlib import pyplot as plt
from playing_cards import Deck, Card, CardGroup, Multideck
from numpy.random import randint
from turn_management import player_turn, Player
from visualization import show_all_hands

n_players = 3


n_decks = 2
rounds = ['Two Books','Two Runs','Two Runs And A Book','Two Books And A Run','Three Books','Three Runs']


def establish_players(n_players):
    usernames_out = [input('Please input a username for player ' +str(i)) for i in range(n_players)]
    return {'username':usernames_out}

def refresh_all_players(all_players):
    for player in all_players:
        player.locked_actions = player.available_actions
        player.available_actions = []
        player.hand = CardGroup()
        player.is_down = False
        player.buy_count = 0
        #update screens here to show the locking.

def deal(list_of_Player, Multideck,dealer_index):
    for i in range(9):
        [player.hand.cards.append(Multideck.draw_top()) for player in list_of_Player]
    dealer_index = (dealer_index+1) % len(list_of_Player)
    return dealer_index

#def player_turn(whose_turn):

def is_round_over():
    return False

def assign_points():
    pass

def display_results():
    pass

players_info = establish_players(n_players)
players = [Player(usernameboi) for usernameboi in players_info['username']]
all_points = []
dealer_index = 0
for round_descriptor in rounds:
    refresh_all_players(players)
    round_over = False
    full_deck = Multideck(n_decks)
    whose_turn = (dealer_index+1) % len(players)
    dealer_index = deal(players, full_deck,dealer_index)
    print(round_descriptor)
    while round_over == False:
        #input(players[0].hand.cards[0].name)
        show_all_hands(players)
        player_turn(whose_turn,players,full_deck,round_descriptor,None)
        round_over = is_round_over()
        whose_turn = (whose_turn+1) % len(players) 

    assign_points()
display_results()





'''
my_deck = Deck()
[print(card.name) for card in my_deck.cards]
'''