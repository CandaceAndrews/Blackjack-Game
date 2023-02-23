import random

SUITS = ['♥️', '♣️', '♠️', '♦️']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def get_hand_value(self):
        value = 0
        num_aces = 0
        for card in self.hand:
            if card.rank == 'A':
                num_aces += 1
                value += 11
            elif card.rank in ['K', 'Q', 'J']:
                value += 10
            else:
                value += card.rank
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value


class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player('Player')
        self.dealer = Player('Dealer')
        self.play_game()

    def play_game(self):
        print("Welcome to Blackjack!\n")
        while True:
            self.deck.reset()
            self.deck.shuffle()
            self.player.clear_hand()
            self.dealer.clear_hand()

            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

            print("Dealer's hand:")
            print(self.dealer.hand[0])
            print("<hidden card>\n")

            while True:
                print("Player's hand:")
                for card in self.player.hand:
                    print(card)
                player_value = self.player.get_hand_value()
                print(f"Value of player's hand: {player_value}\n")

                if player_value == 21:
                    print("Blackjack! Player wins!\n")
                    break

                choice = input("Do you want to hit or stay? ")
                print()
                while choice.lower() not in ['hit', 'stay']:
                    choice = input(
                        "Invalid choice. Do you want to hit or stay? ")
                    print()

                if choice.lower() == 'hit':
                    self.player.add_card(self.deck.deal_card())
                    if self.player.get_hand_value() > 21:
                        print("Player busts. Dealer wins.\n")
                        break
                else:
                    dealer_value = self.dealer.get_hand_value()
                    print("Dealer's hand:")
                    for card in self.dealer.hand:
                        print(card)
                    print(f"Value of dealer's hand: {dealer_value}\n")
                    while dealer_value < 17:
                        self.dealer.add_card(self.deck.deal)


blackjack = Blackjack()
