# Welcome to Torpedo! 

A game known by few and loved by fewer! This is a six-round, two-stage, turn-based, hand-seeking game played with two decks of 54 standard playing cards (including Jokers). The goal of each round is to minimize the number of "points" in your hand by either "laying down" or discarding high-point cards.

Torpedo, also known as "That Damned Women's Game," was introduced to the Walljasper family at least 3 generations ago. It continues to be played at tables spanning the US, North-to-South and East-to-West.

As the family has expanded to ever-further distances, it has become hard to play the game regularly. This project attempts to bridge the gap with online functionality and a not-too-clunky GUI.



# The Rules

Torpedo is fundamentally about "building hands." There are six hands, each of which is made up of two fundamental elements: "Book" and "Run." A book is a three-of-a-kind, pure and simple. Examples include AAA, 333, JJJ, QQQ of any suit. A run is a straight-flush of length four. Examples include AS 2S 3S 4S, 3D 4D 5D 6D, 10C JC QC KC. Notably, Aces can be high or low in a run, but you cannot "wrap around," as in QS KS AS 2S. Another quick note: Jokers are wild, meaning that they can fill the role of any card. A book could be composed of A A JOK. A run could look like 10C JOK QC KC.

The six rounds are: Two Books; Two Runs; Two Books and a Run; Two Runs and a Book; Three Books; and Three Runs.

## The Setup

To begin, shuffle two decks together, including jokers. The first dealer, typically, is the one who suggested the game. Deal 9 cards to each player. Place the deck facedown in the center of the table. Once everyone has adjusted their cards, the player to the left of the dealer flips the top card from the deck face-up and begins the discard pile.

## A Useful Construct

First, an essential dichotomy. There are two "phases" in any of the six rounds of Torpedo. 

Players in the "caterpillar" phase:
* Attempt to form the hand, in order to "lay down" (see "Taking Turns")
* Attempt to wildly throw cards if players in the second phase are on the verge of emptying their hand

Players in the "butterfly" phase:
* Have laid down
* Can extend the laid elements (books, runs) of other butterflies
* Seek to end the game by emptying their hand with a discard

All players start out as "caterpillars." There is no way to win in the caterpillar phase; players stuck in the caterpillar phase at the end of the game will almost certainly be stuck with the most points. (This is called "getting caught with a mitfull.")

## Taking Turns

The first player to take a turn is always to the left of the dealer. Play passes to the left, as does the deal.

The beginning of any turn is symbolized by the drawing of a card. This card can be drawn from the "live" (facedown) deck, or from the discard pile (with stipulations -- see "buying").

Once a card has been drawn, a player's options are determined by their phase and hand. 

Caterpillars may:
* Discard -- Place one card from their hand onto the discard pile, ending the turn.
* Exchange for a Joker -- Exchange an appropriate card from their hand with a Joker in a Butterfly's laid cards.
* Lay Down -- Place the appropriate number of Books and Runs down, transitioning to the Butterfly phase.

In addition to Discarding and Exchanging for Joker, Butterflies may: 
* Play on Others -- Play one or several cards from their hand to extend the books and runs of another Butterfly.
* End the Round -- Though actionably indistiguishable from discarding, a Butterfly who discards their last card into the discard pile ends the round immediately.

**NOTICE** that, distinct from other forms of Rummy, a player **CANNOT LAY** any greater or fewer books/runs than specified by the round. You lay down *once*, only.

Should the live deck run out of cards, all cards except the most recent discard should be shuffled and set as the live deck. The most recent discard remains as the foundation of the new discard pile.

## Buying

Once a turn has ended by player discard, any player may "buy" that fresh discard, allowing them to pick up that card and place it in their hand. Buying can only occur *between turns*; that is, you must buy after a discard but before the next player draws from *either pile*.

To Buy, a player must audibly say/shout "BUY!" In the event of multiple Buys, the first player to finish the exclamation is given priority.

At that point, the buy can either be accepted or denied by the player who is set to draw and begin their turn (at-bat). 
* If the at-bat player accepts the buy, the buying player takes the bought card and an additional "penalty" card from the live deck. The at-bat player then *must* draw from the live deck -- the unburied discard is still "dead." Indeed, any card, once buried under another card in the discard, may not be drawn unless reshuffled.
* If the at-bat player denies the buy, the at-bat player must draw the contested card from the discard into their own hand and begin their turn. The buying player(s) receive no benefit nor penalty.

A maximum of 3 Buys are allowed for each player, per round. As a result, no player should ever have more than 16 cards in their hand at any time (15 passively held + 1 recently drawn).

Any player who is found to have violated the 3-Buy maximum should be henceforth referred to as "Clara" and should not be deemed creditworthy.

## Ending a Round

A round ends when a player drops the number of cards in their hand to 0 via a discard.

At this point, all players must assess the points remaining in their hand (*not* including cards laid down):

* 5 points for cards rank 2-9
* 10 points for cards rank 10-K
* 15 points for Aces
* 50 points for Jokers

A scribe should write these scores down, per player, on a notepad.

## Ending the Game

At the end of the final round, Three Runs, the scribe should sum the six round scores for each player. The player with the lowest sum wins.

## Minor Notes

### "Going around"

If the number of cards in a player's hand drops to 0 by any means other than discarding, that player's turn ends, and play continues as usual, with the stipulation that the visible card on the discard pile is dead and undrawable.

It's seen as courteous, though not strictly a rule, to allow the game to "go around" if possible.

### Names and Labels
* *Lay Down*: The term for placing cards face-up on the table, signalling transition to Butterfly phase.
* *Get Skunked*: Similar to "Caught with a Mitfull."
* *Down'n'Out*: To lay down and end the game in the same turn.

***Nicknames***
* *Ben*: A player who discards all non-5-point cards, taking 45 points instead of attempting to build the required hand.
* *Lizzie*: A sore loser, especially one who throws their cards at the end of a round.
* *Nettie*: A player who makes up additional rules/brings up archaic texts at inconvenient times.
* *Racheal*: A player who goes down'n'out while everyone else is still a Caterpillar.

# About this Project

I (Adam Kunesh) started this project as a fun Python challenge during the third year of my PhD at UC Davis. This year especially, it's been difficult for the family to congregate and play Torpedo due to the COVID-19 Pandemic.

If you see any glaring bugs, or are having difficulty with the interface, please shoot me a message!

-Adam