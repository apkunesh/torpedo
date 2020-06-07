from playing_cards import CardGroup
from time import sleep
from copy import copy


player_actions = ['Draw from Discard','Draw from Deck','Discard','Buy','Allow Buy','Lay Down','Play from Hand','Exchange Joker']

def print_action(player):
    """[summary]

    Args:
        player ([type]): [description]
    """
    [print(str(i)+': '+player.available_actions[i]) for i in range(len(player.available_actions))]


def get_action(player):
    """[summary]

    Args:
        player ([type]): [description]

    Returns:
        [type]: [description]
    """
    print_action(player)
    chosen_action_index = int(input('Please indicate your selection from the following list by inputting the number: '))
    return player.available_actions[chosen_action_index]

def set_predraw_player_actions(whose_turn,players):
    """[summary]

    Args:
        whose_turn ([type]): [description]
        players ([type]): [description]

    Returns:
        [type]: [description]
    """
    active_player = players[whose_turn]
    active_player.available_actions = ['Draw from Discard','Draw from Deck','Allow Buy']
    players[whose_turn-1].available_actions = []
    i = (whose_turn-1) % len(players)
    inactive_players = players[0:i:1]+players[i+2:]
    if i == len(players)-1:
        inactive_players = inactive_players[1:]
    for player in inactive_players:
        player.available_actions = ['Buy']
    return inactive_players

class Player():
    """[summary]
    """
    def __init__(self,username):
        self.id = username
        self.hand = CardGroup()
        self.is_down = False
        self.available_actions = player_actions
        self.locked_actions = []
        self.buy_count = 0

def draw_or_allow_buy(whose_turn,players,full_deck,discard_pile):
    """[summary]

    Args:
        whose_turn ([type]): [description]
        players ([type]): [description]
        full_deck ([type]): [description]
        discard_pile ([type]): [description]
    """
    active_player = players[whose_turn]
    print(active_player.id + ' is up!')
    inactive_players = set_predraw_player_actions(whose_turn,players)
    #[print(player.id) for player in inactive_players]
    # TODO: instantiate buy listener
    chosen_action = get_action(active_player)
    if chosen_action == 'Draw from Deck':
        active_player.hand.cards.append(full_deck.draw_top())
    elif chosen_action == 'Draw from Discard':
        active_player.hand.cards.append(discard_pile.draw_top())
    elif chosen_action == 'Allow Buy':
        pass #TODO: include Buy logic
    else: 
        print('ERROR in draw_allow_or_buy in turn_management')

def set_postdraw_player_actions(whose_turn,players):
    """[summary]

    Args:
        whose_turn ([type]): [description]
        players ([type]): [description]
    """
    active_player = players[whose_turn]
    for player in players:
        if player != active_player:
            player.available_actions = []
        else:
            pass
    if active_player.is_down == False:
        active_player.available_actions = ['Discard','Lay Down','Exchange Joker']
    else:
        active_player.available_actions = ['Discard','Play from Hand','Exchange Joker']

def indicate_discard_card(whose_turn,players):
    """[summary]

    Args:
        whose_turn ([type]): [description]
        players ([type]): [description]

    Returns:
        [type]: [description]
    """
    cards_to_choose_from = players[whose_turn].hand.cards
    players[whose_turn].hand.print_cards()
    chosen_to_discard = int(input('Select a card to discard. Type a number. '))
    return chosen_to_discard

def lay_down_or_discard_or_exchange_joker(whose_turn,players,full_deck,discard_pile):
    """[summary]

    Args:
        whose_turn ([type]): [description]
        players ([type]): [description]
        full_deck ([type]): [description]
        discard_pile ([type]): [description]
    """
    active_player = players[whose_turn]
    set_postdraw_player_actions(whose_turn,players)
    chosen_action = get_action(active_player)
    if chosen_action == 'Discard':
        discard_index = indicate_discard_card(whose_turn,players)
        discard_pile.discard_from_player(active_player,discard_index)
    elif chosen_action == 'Lay Down':
        pass
    elif chosen_action == 'Exchange Joker':
        pass
    else:
        print('ERROR: impossible chosen action in lay_down_or_discard_or_exchange_joker')


def play_hand_or_discard_or_exchange_joker(whose_turn,players,full_deck,discard_pile):
    """[summary]

    Args:
        whose_turn ([type]): [description]
        players ([type]): [description]
        full_deck ([type]): [description]
        discard_pile ([type]): [description]
    """
    pass

def player_turn(whose_turn,players,full_deck,round_descriptor,discard_pile):
    """[summary]

    Args:
        whose_turn ([type]): [description]
        players ([type]): [description]
        full_deck ([type]): [description]
        round_descriptor ([type]): [description]
        discard_pile ([type]): [description]
    """
    sleep(1) #allowing players to examine cards to decide if they want to buy.
    draw_or_allow_buy(whose_turn,players,full_deck,discard_pile)
    if players[whose_turn].is_down == False:
        lay_down_or_discard_or_exchange_joker(whose_turn,players,full_deck,discard_pile)
    else:
        play_hand_or_discard_or_exchange_joker(whose_turn,players,full_deck,discard_pile)

