SUITS = ['♥️', '♣️', '♠️', '♦️']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, suit='🐕', rank=20):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def get_rank(self):
        return self.rank


class Deck:

    def __init__(self):
        self.cards = []

    def add_cards(self):
        for suit in SUITS:
            for rank in RANKS:
                new_card = Card(suit, rank)
                self.cards.append(new_card)


class Player:
    def __init__(self):
        self.name = input("What is your name? ")
        self.hand = []

    def __str__(self):
        return f'{self.name} is the player'

    def turn(self):
        '''Player decides how many times to hit before staying'''
        pass


class Dealer(Player):
    # inherits from Player
    # everything is the same as player, unless you write it differently in here
    def __init__(self):
        self.name = "Dealer"
        # overrides the code asking for player's name
        self.hand = []

    def __str__(self):
        # when we write variables and methods with the same name as the parent class,
        # they override the code from the parent class (Player)
        return f'{self.name} is the dealer'

    def turn(self):
        '''unlike player, dealer follows house rules and stays at 17,
        no choice'''

    def end_game(self):
        pass


class Game:

    def __init__(self, deck=None):
        # can set default values in the signature line, like 'deck=None'
        self.player = Player()
        # the value of self.player is an instance of the class Player
        self.dealer = Dealer()
        self.deck = deck
        # self.setup()
        # calling the Game class's setup function

    def setup(self):
        self.deck = Deck()
        # calls line 13, creates a deck
        self.deck.add_cards()
        # calls line 16, adds cards to the deck

    def money_available(participants):
        pot = 0
        for participant in participants:
            pot += input(int(('What is your bet')))
        return pot


new_game = Game()
# calls the Game class's init method in line 54
new_game.setup()
print(new_game.player)
# calls Player __str__ method
print(new_game.player.hand)
print(new_game.dealer)
# calls Dealer __str__ method
print(new_game.dealer.hand)

# for card in new_game.deck.cards:
#     print(card)

# pot = Game.money_available(['Gerardo', 'Candace'])
# created the game and the deck with cards

# TODO
# ✅ make a player, like we did with Deck
# ✅ make a dealer, also like we did with Deck
# shuffle deck
# play
# deal cards
# player's turn (hit/stay)
# calculate score from cards in hand
# dealer's turn
# calculate score from cards in hand
# who won/lost/busted/21
