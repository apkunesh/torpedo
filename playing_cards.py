import pandas as pd
from matplotlib.pyplot import imread as image_reader
from matplotlib import pyplot as plt
from random import randint
from copy import copy

deck_info = pd.read_excel('deck_of_cards.xlsx',index_col=0)
#input(deck_info.loc['2C'])
#input('attempting to access QC')
#input(deck_info.loc['QC'])
#input(deck_info.index)

rank_dict = {'A':'ace','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten','J':'jack','Q':'queen','K':'king','JOK':'joker'}
suit_dict = {'C':'clubs','D':'diamonds','S':'spades','H':'hearts','JOK':'jokers (wut?)'}

class Card():
    """[summary]
    """
    def __init__(self,card_id):
        self.id = card_id
        self.image = image_reader('card_images/'+self.id+'.JPG')
        self.rank = deck_info.loc[card_id]['rank']
        self.suit = deck_info.loc[card_id]['suit']
        self.name = rank_dict[str(self.rank)] + ' of ' + suit_dict[self.suit]

class CardGroup():
    """[summary]
    """
    def __init__(self):
        self.cards = []
    def add_cards(self,cards_in):
        [self.cards.append(card_in) for card_in in cards_in]
    def add_card(self,card_in):
        self.cards.append(card_in)
    def is_book(self):
        if len(self.cards) != 3:
            truth_value = False
        else:
            pass #Include additional logic checkers here
    def is_run(self):
        pass # Include logic checker here, too.
    def print_cards(self):
        print(self.cards[1].name)
        [print(str(i)+': ' +str(self.cards[i].name)+ '.') for i in range(len(self.cards))]


class Deck(CardGroup):
    """[summary]

    Args:
        CardGroup ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self.initialize_full_deck()
    def initialize_full_deck(self):
        """[summary]
        """
        self.cards = [Card(card_id) for card_id in deck_info.index]
    def draw_top(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if len(self.cards) == 0:
            print('Sorry, no more cards can be drawn from this empty deck. Returning None.')
            drawn_card = None
        else:
            drawn_index = randint(0,len(self.cards)-1)
            drawn_card = self.cards[drawn_index]
            self.cards.pop(drawn_index)
        return drawn_card

class DiscardPile(CardGroup):
    """[summary]

    Args:
        CardGroup ([type]): [description]
    """
    def __init__(self):
        super().__init__()
        self.is_dead = False
    def draw_top(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if len(self.cards) == 0:
            print('Sorry, no more cards can be drawn from the discard pile. Returning None.')
            drawn_card = None
        else:
            drawn_card = copy(self.cards[-1])
            self.cards.pop(-1)
        return drawn_card
    def discard_from_player(self,player_in,card_index_in):
        """[summary]

        Args:
            player_in ([type]): [description]
            card_index_in ([type]): [description]
        """
        card_to_discard = player_in.hand.cards[card_index_in]
        self.discard(card_to_discard)
        player_in.hand.cards.pop(card_index_in)
    def discard(self,card_in):
        """[summary]

        Args:
            card_in ([type]): [description]
        """
        self.cards.append(card_in)
        #Refresh image here?


class Multideck():
    def __init__(self,n_decks):
        self.all_decks = [Deck() for i in range(n_decks)]
    def draw_top(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        n_cards_in_decks = [len(deck.cards) for deck in self.all_decks]
        cumulants = [n_cards_in_decks[0]]
        for i in range(len(n_cards_in_decks)-1):
            cumulants.append(cumulants[i]+n_cards_in_decks[i+1])
        total_cards = sum(n_cards_in_decks)
        deck_chooser = randint(1,total_cards)
        deck_index = -1
        deck_found = False
        while deck_found == False:
            deck_index += 1
            deck_found = cumulants[deck_index] >= deck_chooser
        drawn_card = self.all_decks[deck_index].draw_top()
        return drawn_card
'''
my_deck = Multideck(2)
for i in range(108):
    print(my_deck.draw_top().name)
    print(str(sum([len(deck.cards) for deck in my_deck.all_decks])) + ' cards remain.')
'''

#card = Card('QC')
#print(card.rank)
'''
deck = Deck()
card1 = deck.cards[0]
card2 = deck.cards[1]
fig,ax = plt.subplots(figsize=(16,9))
card1ext = (400,600,0,300)
card2ext = (450,650,0,300)
im1 = ax.imshow(card1.image,origin = 'upper',extent = card1ext)
im2 = ax.imshow(card2.image,origin = 'upper',extent = card2ext)
ax.set_xlim(0,2000)
ax.set_ylim(0,1000)
plt.show()
'''