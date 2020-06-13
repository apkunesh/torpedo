def print_action(player):
    """Shows all available actions of a player as text.

    Args:
        player (Player): The player whose available actions are to be shown.
    """
    [print(str(i)+': '+player.available_actions[i]) for i in range(len(player.available_actions))]


def get_action(player):
    """Queries the player for any desired actions.

    Args:
        player (Player): The player whose action is desired.

    Returns:
        String: The player's choice of action
    """
    print_action(player)
    chosen_action_index = int(input('Please indicate your selection from the following list by inputting the number: '))
    return player.available_actions[chosen_action_index]


def indicate_discard_card(whose_turn,players):
    """Queries and returns a player who is sending a card to the discard pile.

    Args:
        whose_turn (int): The index of the active player
        players ([type]): The players of your game of torpedo.

    Returns:
        int: The index (in the player's hand) of the card which the player has chosen to discard.
    """
    cards_to_choose_from = players[whose_turn].hand.cards
    players[whose_turn].hand.print_cards()
    chosen_to_discard = int(input('Select a card to discard. Type a number. '))
    return chosen_to_discard