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
    """A conventional playing card.
    """
    def __init__(self,card_id):
        self.id = card_id
        self.image = image_reader('card_images/'+self.id+'.JPG')
        self.rank = deck_info.loc[card_id]['rank']
        self.suit = deck_info.loc[card_id]['suit']
        self.name = rank_dict[str(self.rank)] + ' of ' + suit_dict[self.suit]

class CardGroup():
    """An ordered set of cards.
    """
    def __init__(self):
        self.cards = []
    def add_cards(self,cards_in):
        """Adds cards to the card group.

        Args:
            cards_in (list of Cards): cards to be added to the card group
        """
        [self.cards.append(card_in) for card_in in cards_in]
    def add_card(self,card_in):
        """Adds a single card to the card group.

        Args:
            card_in (Card): card to be added to the card group
        """
        self.cards.append(card_in)
    def is_book(self):
        """Tests if the card group forms a Torpedo book, or "three of a kind."
        """
        if len(self.cards) != 3:
            i_am_book = False
        else:
            i_am_book = (self.cards[0].rank == self.cards[1].rank) and (self.cards[1].rank == self.cards[2].rank)
        return i_am_book
    def is_run(self):
        if len(self.cards) != 4:
            i_am_run = False
        else:
            pass # TODO: Include additional logic here.
        return i_am_run
    def print_cards(self):
        print(self.cards[1].name)
        [print(str(i)+': ' +str(self.cards[i].name)+ '.') for i in range(len(self.cards))]


class Deck(CardGroup):
    """A deck of 52 cards plus jokers, or whatever you've stored in deck_of_cards.xlsx. Also references images
    in the "card_images" directory.
    """
    def __init__(self):
        """A deck of 52 cards plus jokers, or whatever you've stored in deck_of_cards.xlsx. 
        
        Also references images in the "card_images" directory.
        """
        super().__init__()
        self.initialize_full_deck()
    def initialize_full_deck(self):
        """Sets the cards attribute to include all cards in deck_of_cards.xslx.
        """
        self.cards = [Card(card_id) for card_id in deck_info.index]
    def draw_top(self):
        """Returns a card, drawn at random, from the deck, and removes that card from the deck.
        
        Unintuitively, this function does not actually care about card ordering.

        Returns:
            Card: The drawn card.
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
    """An ordered discard pile. The most recent card is drawn first.
    """
    def __init__(self):
        """An ordered discard pile. The most recent card is drawn first.
        """
        super().__init__()
        self.is_dead = False
    def draw_top(self):
        """Draws the most recent card discarded, if any; otherwise, returns nothing.

        This removes the drawn card from the discard pile.

        Returns:
            Card: The most recently discarded card.
        """
        if len(self.cards) == 0:
            print('Sorry, no more cards can be drawn from the discard pile. Returning None.')
            drawn_card = None
        else:
            drawn_card = copy(self.cards[-1])
            self.cards.pop(-1)
        return drawn_card
    def discard_from_player(self,player_in,card_index_in):
        """Transfers card from a player's hand to the discard pile.

        Removes the card from the player's hand and pushes the discarded card to the top of the discard pile.

        Args:
            player_in (Player): The player discarding the card
            card_index_in (int): The index of the discarded card in the player's hand
        """
        card_to_discard = player_in.hand.cards[card_index_in]
        self.discard(card_to_discard)
        player_in.hand.cards.pop(card_index_in)
    def discard(self,card_in):
        """Pushes a card to the top of the discard pile. 
        
        If a player is discarding a card, use instead discard_from_player.

        Args:
            card_in (Card): The card to be discarded
        """
        self.cards.append(card_in)
        #Refresh image here?


class Multideck():
    """A collection of decks -- used in torpedo, a multi-deck game. 

    This class helps avoid complications related to nonunique identifiers between cards from different decks.
    """
    def __init__(self,n_decks):
        """A collection of decks -- used in torpedo, a multi-deck game. 

        This class helps avoid complications related to nonunique identifiers between cards from different decks.
        """
        self.all_decks = [Deck() for i in range(n_decks)]
    def draw_top(self):
        """Draws a random card from the multideck.

        Similar to draw_top from the Deck class. Removes the drawn card from the multideck.

        Returns:
            Card: The drawn card. 
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