from playing_cards import construct_hand_by_cardnames


run_group = construct_hand_by_cardnames('2S','3S','4S','5S')
print(run_group.is_run())
print(run_group.is_book())

book_group = construct_hand_by_cardnames('AS','AS','AD')
print(book_group.is_run())
print(book_group.is_book())

nothing_group = construct_hand_by_cardnames('AS','AS','QD')
print(nothing_group.is_book())
print(nothing_group.is_run())