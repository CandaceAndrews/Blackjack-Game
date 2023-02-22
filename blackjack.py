import random

SUITS = ['♥', '♣️', '♠️', '♦']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


class Card:
    """store suit and rank for each card
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit}{self.rank}"


class Deck:
    """create deck of cards and shuffle
    """

    def __init__(self):
        self.cards = []

    def add_cards(self):
        for symbol in SUITS:
            for number in RANKS:
                self.cards.append(Card(symbol, number))

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    """name input and view player hand
    """

    def __init__(self):
        self.name = input("What is your name? ")
        self.hand = []

    def __str__(self):
        return f"{self.name} is the player"

    def view_cards(self):
        for card in self.hand:
            print(card)


class Dealer(Player):
    # inherits from Player
    """name output, cards in hand
    """

    def __init__(self):
        self.name = "Dealer"
        self.hand = []

    def __str__(self):
        # when we write cariables and methods with the same
        # as the parent class, they override the code from
        # the parent class (Player)
        return f"{self.name} is the dealer"

    def turn(self):
        # unlike player, dealer follows the house rules
        pass

    def end_game(self):
        pass


class Game():
    """main flow of the game
    """
    print("Welcome to Blackjack!\n")

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.setup()

    def setup(self):
        self.deck = Deck()
        self.deck.add_cards()

    def player_turn(self):
        """decide if player hits or stands
        """
        decided_action = input("Hit or Stand? ").lower()
        if decided_action == "hit":
            drawn_card = self.deck.cards.pop()
            self.player.hand.append(drawn_card)
            self.player.view_cards()

    def deal(self):
        self.setup()
        self.deck.shuffle()

        # print(new_game.player)
        print()

        card = self.deck.cards.pop()
        self.player.hand.append(card)

        card = self.deck.cards.pop()
        self.player.hand.append(card)

        print(f"{self.player.name}'s hand:")
        self.player.view_cards()

        # print(new_game.dealer)
        print()

        card = self.deck.cards.pop()
        self.dealer.hand.append(card)

        card = self.deck.cards.pop()
        self.dealer.hand.append(card)

        print("Dealer's hand:")
        self.dealer.view_cards()


# GAME START
new_game = Game()
new_game.deal()
new_game.player_turn()
