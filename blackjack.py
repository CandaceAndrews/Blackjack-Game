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
        return f"{self.rank} of {self.suit}"


class Deck:
    """create deck of cards and shuffle
    """

    def __init__(self):
        self.cards = []
        self.add_cards()
        self.shuffle()

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

    def get_hand_value(self):
        hand_value = 0
        aces = 0
        for card in self.hand:
            if card.rank == 'A':
                aces += 1
            elif card.rank in ['K', 'Q', 'J']:
                hand_value += 10
            else:
                hand_value += card.rank
        for _ in range(aces):
            if hand_value + 11 > 21:
                hand_value += 1
            else:
                hand_value += 11
            return hand_value
        print(f"Value of {self.name}'s hand: {hand_value}")


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
        # can't go over 17
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
        self.deck = Deck()
        self.deal()
        self.player_turn()

    def player_turn(self):
        """decide if player hits or stands
        """
        choice = input("--> Hit or Stand? ").lower()
        if choice == "hit":
            self.give_card(self.player)
            self.player.view_cards()
            self.player.get_hand_value()

    def give_card(self, person_playing):
        """give one card
        """
        card = self.deck.cards.pop()
        person_playing.hand.append(card)

    def deal(self):
        """give out cards and print game info
        """
        # two cards for player ---
        self.give_card(self.player)
        self.give_card(self.player)

        # print player info ---
        print(f"{self.player.name}'s hand:")
        self.player.view_cards()
        self.player.get_hand_value()
        print()

        # two cards for dealer ---
        self.give_card(self.dealer)
        self.give_card(self.dealer)

        # print dealer info ---
        print("Dealer's hand:")
        self.dealer.view_cards()
        self.dealer.get_hand_value()
        print()


# GAME START
new_game = Game()
