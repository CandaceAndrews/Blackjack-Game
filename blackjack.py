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

    def add_cards(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))


class Game:
    def __init__(self):
        self.player = None
        self.dealer = None
        self.deck = None
        self.setup()
        # calling the Game class's setup function

    def setup(self):
        self.deck = Deck()
        # calls line 13, creates a deck
        self.deck.add_cards()
        # calls line 16, adds cards to the deck
        for card in self.deck.cards:
            print(card)
            # calls the __str__ method for each card


new_game = Game()
# created the game and the deck with cards

# TODO
# make a player, like we did with Deck
# make a dealer, also like we did with Deck
# play
# shuffle deck
# deal cards
# player's turn (hit/stay)
# calculate score from cards in hand
# dealer's turn
# calculate score from cards in hand
# who won/lost/busted/21
