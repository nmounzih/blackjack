import random


class UnknownSuitError(Exception):
    pass


class Card:
    numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(Card.numbers[self.number], Card.suits[self.suit])

    def __str__(self):
        return "{} {}".format(Card.numbers[self.number], Card.suits[self.suit])

    def __eq__(self, other):
        return self.number == other.number and self.suit == other.suit

    def value(self):
        if self.number > 8:
            return 10
        if self.number == 0:
            return 11
        return self.number + 1


class Deck:
    def __init__(self, number=1):
        self.cards = [Card(c % 13, c//13) for c in range(52)] * number
        self.current_place = 0

    def __repr__(self):
        return str(self.cards)

    def shuffle(self):
        return random.shuffle(self.cards)

    def deal_card(self):
        if self.current_place >= len(self.cards):
            self.shuffle()
            self.current_place = 0
        top_card = self.cards[self.current_place]
        self.current_place += 1
        return top_card


class BlackjackPlayer:
    def __init__(self):
        self.hand = []

    def __repr__(self):
        return str(self.hand)

    def clear_hand(self):
        self.hand = []

    def take_card(self, card):
        self.hand.append(card)

    def score(self):
        total = 0
        ace_count = 0
        for card in self.hand:
            total += card.value()
            if card.value() == 11:
                ace_count += 1
        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1
        return total


class Dealer(BlackjackPlayer):
    def hit(self):
        if self.score() >= 17:
            return False
        return True


class Player(BlackjackPlayer):
    def hit(self):
        print(self.hand)
        query = 'You have {} points, would you like to hit or stand? h/s '
        return 'h' == input(query.format(self.score()))


class Game:
    def __init__(self, player, dealer):
        self.dealer = dealer
        self.player = player

    def play_hand(self):
        deck = Deck(2)
        deck.shuffle()
        self.player.clear_hand()
        self.dealer.clear_hand()

        for _ in range(2):
            self.dealer.take_card(deck.deal_card())
            self.player.take_card(deck.deal_card())

        while self.player.score() < 21 and self.player.hit():
            self.player.take_card(deck.deal_card())

        while self.dealer.hit():
            self.dealer.take_card(deck.deal_card())

        print("Player: {}\nDealer: {}".format(self.player, self.dealer))

        if self.player.score() > 21:
            print("\nPlayer busts. Game over.\n")
        elif self.dealer.score() > 21:
            print("\nDealer busts. Game over.\n")
        elif self.player.score() > self.dealer.score():
            print("\nPlayer wins.\n")
        else:
            print("\nHouse wins.\n")


def main():
    print("\n~ Welcome to the BELLAGIO ~ ")
    game = Game(Player(), Dealer())
    while 'y' == input("Ready for some blackjack? [y/n]\n"):
        game.play_hand()


if __name__ == '__main__':
    main()
