import random
import os


class UnknownSuitError(Exception):
    pass


class Card:
    numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self, number, suit):
        if isinstance(suit, str):
            try:
                suit = Card.suits.index(suit)
            except:
                raise UnknownSuitError
        self.number = number
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(str(Card.numbers[self.number]), Card.suits[self.suit])

    def __str__(self):
        return "{} {}".format(Card.numbers[self.number], Card.suits[self.suit])

    def __eq__(self, other):
        return self.number == other.number and self.suit == other.suit


class Deck:

    def __init__(self):
        self.cards = [Card(c%13, c//13) for c in range(52)]

    def __repr__(self):
        return str(self.cards)

    def shuffle(self):
        return random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    # def start_deal(self):
    #     for x in range(2):
    #         return self.cards.pop()

# deck = Deck()
# deck.shuffle()
# for card in deck.cards:
#     print(card.number, end=":")
#     print(card.suit)

# class Hand:
#
#     def __init__(self, player):
#         self.player = player
#         self.cards = [] #how to use Card class here?
#
#     def draw_card(self):
#         global deck #took this from stackexchange... unsure how to do without?
#         take_card = deck.deal_card()
#         self.cards.append(take_card)

def clear():
    os.system("clear")

# def player_turn():
#
#         player_turn()

#def dealer_turn():



def main():
    print("\n~ Welcome to the BELLAGIO ~ ")
    start = input(("Ready for some blackjack?\n"))
    deck = Deck()
    deck.shuffle()
    player_hand = []
    dealer_hand = []
    player_hand_values = []
    dealer_hand_values = []

    next_card = deck.deal_card()# player card one
    player_hand.append(next_card)

    next_card = deck.deal_card()# player card two
    player_hand.append(next_card)

    next_card = deck.deal_card()# dealer card one
    dealer_hand.append(next_card)

    next_card = deck.deal_card()# dealer card two
    dealer_hand.append(next_card)



    print("Dealer has {}\n".format(dealer_hand))
    print("Player has {}\n".format(player_hand))

    while sum(player_hand_values) < 21:
        for card in player_hand:
            player_hand_values.append(Card.numbers[card.number])
            for value in player_hand_values:
                if value == 'King' or value == 'Queen' or value == 'Jack':
                    player_hand_values.append(10)
                    player_hand_values.remove(value)
                elif value == 'Ace':
                    player_hand_values.append(1)
                    player_hand_values.remove(value)
        choice = input("Would you like to [S]tand or [H]it? ").lower()
        if choice == 's'.lower(): #dealer turn
            while sum(dealer_hand_values) < 17:
                for card in dealer_hand:
                    dealer_hand_values.append(Card.numbers[card.number])
                    for value in dealer_hand_values:
                        if value == 'King' or value == 'Queen' or value == 'Jack':
                            dealer_hand_values.append(10)
                            dealer_hand_values.remove(value)
                        elif value == 'Ace':
                            dealer_hand_values.append(1)
                            dealer_hand_values.remove(value)
                next_card = deck.deal_card()
                dealer_hand.append(next_card)
                print("Dealer now has {}".format(dealer_hand))
        else:
            next_card = deck.deal_card()
            player_hand.append(next_card)
            print("Player now has {}".format(player_hand))
    if sum(player_hand_values) > 21:
        print("\nBUST. The house wins.")
        play_again = input("\nPlay again? Y/n ").lower()
        if play_again != 'n':
            clear()
            main()





if __name__ == '__main__':
    main()
