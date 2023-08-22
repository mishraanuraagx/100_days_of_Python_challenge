import os
import random


def get_cards():
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    decks_in_play = 2
    cards = 2 * cards
    random.shuffle(cards)
    return cards


def main():
    # get the cards
    cards:list = get_cards()
    players_hand: list = []
    dealers_hand: list = []
    hit = True
    # serve the first two cards
    cards, players_hand, dealers_hand = draw_cards(cards, players_hand, dealers_hand)
    cards, players_hand, dealers_hand = draw_cards(cards, players_hand, dealers_hand)
    while hit and len(cards) > 1:
        print_status(players_hand, dealers_hand)
        hit = not game_over(players_hand, dealers_hand)
        if hit:
            action = input("Do you wish to be dealt another hand. yes/no ")
            if action.lower() == 'no':
                hit = False
            else:
                cards, players_hand, dealers_hand = draw_cards(cards, players_hand, dealers_hand)

    print_result(players_hand, dealers_hand)


def game_over(players_hand, dealers_hand):
    player_sum = sum_cards(players_hand)
    dealer_sum = sum_cards(dealers_hand)
    if player_sum > 21 or dealer_sum > 21:
        return True
    return False


def print_status(players_hand: list, dealers_hand: list):
    # clear screen
    os.system("clc" if os.name == 'nt' else "clear")
    print(blackjack_logo)
    print(cards_logo)
    print(f"Players Hand: {players_hand}")
    # replace all card with * in dealer's hand
    tmp = dealers_hand.copy()
    tmp.pop(-1)
    tmp.append("*")
    print(f"Dealers Hand: {tmp}")


def print_result(players_hand: list, dealers_hand: list):
    # clear screen
    os.system("clc" if os.name == 'nt' else 'clear')
    print(blackjack_logo)
    print(cards_logo)
    print(f"Players Hand: {players_hand}")
    print(f"Dealers Hand: {dealers_hand}")
    player_sum = sum_cards(players_hand)
    dealer_sum = sum_cards(dealers_hand)
    if dealer_sum > 21 and player_sum > 21:
        print(f"Both of you are bust. Both exceeded 21. Dealer's Sum : {dealer_sum}. Player's Sum : {player_sum}.")
    elif dealer_sum > player_sum or player_sum > 21:
        print(f"Dealer won with total sum of {dealer_sum} vs your {player_sum}. You lost all of your bet.")
    elif dealer_sum < player_sum or dealer_sum > 21:
        print(f"You won with total sum of {player_sum} vs dealer's {dealer_sum}. You doubled your bet amount.")
    else:
        print(f"It was a tie, you got your money back. Both had a total sum of {player_sum}.")


def sum_cards(cards:list):
    # maximize the sum
    sum = 0
    for i in cards:
        if i == "A":
            # add 1 for now
            sum += 1
        elif i == "J" or i == "Q" or i == "K":
            sum += 10
        else:
            sum += int(i)

    for i in range(cards.count("A")):
        if sum + 10 <= 21:
            sum += 10
        else:
            break;

    return sum


def draw_cards(cards:list, players_hand, dealers_hand):
    players_hand.append(cards.pop(-1))
    dealers_hand.append(cards.pop(-1))
    return cards, players_hand, dealers_hand


blackjack_logo = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\               
'''

# https://ascii.co.uk/art/cards
cards_logo = '''                               _
                               _
       ,'`.    _  _    /\    _(_)_
      (_,._)  ( `' )  <  >  (_)+(_)
        /\     `.,'    \/      |
                               _
       ,db.                  _(M)_
      (MMMM)       Stef     (M)+(M)
        db                     |
'''

if __name__ == "__main__":
    main()
