from turn_management import Player, player_actions, draw_or_allow_buy
players = [Player(usernameboi) for usernameboi in ['Adam','Darcy','Randy']]
from visualization import show_all_hands(players)


print(draw_or_allow_buy(3,players,None))

'''
class kappaboi:
    def __init__(self):
        self.id = 32

kappa = kappaboi()
print(kappa.id)

def change_kappaid(kappa):
    kappa.id = 12

change_kappaid(kappa)
print(kappa.id)
'''
'''
k = [0,1,2,3]
#print(k[0:1]+k[3:])
for i in range(4):
    mylist = k[0:i]+k[i+2:]
    if i == len(k)-1:
        mylist = mylist[1:]
    print(mylist)
'''