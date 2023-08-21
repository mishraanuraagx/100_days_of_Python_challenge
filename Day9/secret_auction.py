
import os

Hammer_logo = '''
       T                                    \`.    T
       |    T     .--------------.___________) \   |    T
       !    |     |//////////////|___________[ ]   !  T |
            !     `--------------'           )_(      | !
                                          ___|_|___!
'''

def clear_screen():
    os.system("cls" if os.name=='nt' else "clear")
    print(Hammer_logo)

auction_bids = {}

bidders_exist = True

while bidders_exist:
    clear_screen()
    name = input("Please provide the bidder's name: ")
    bid = int(input("And the amount: $"))
    auction_bids = {name:bid}
    more_bidders = input("Are there more bidder(s)? yes/no ")
    if more_bidders.lower() == "no":
        bidders_exist = False

auction_winner = None
for key in auction_bids:
    if auction_winner == None:
        auction_winner = key
    if auction_winner != key and auction_bids[auction_winner] < auction_bids[key]:
        auction_winner = key

clear_screen()
print(f"The secret auction winner is {auction_winner} with bid of ${auction_bids[auction_winner]}")
