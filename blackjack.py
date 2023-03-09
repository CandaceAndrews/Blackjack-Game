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
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    """name input, view hand and value of their cards
    """

    def __init__(self):
        self.name = input("What is your name? ")
        print()
        self.hand = []

    def __str__(self):
        return f"{self.name} is the player"

    def view_cards(self):
        """view the cards in hand
        """
        for card in self.hand:
            print(card)

    def get_hand_value(self):
        """add total value of cards in hand
        """
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

    def view_hand_value(self):
        """display total value of hand
        """
        print(f"Value of {self.name}'s hand: {self.get_hand_value()}")


class Dealer(Player):
    # inherits from Player
    """name output, cards in hand
    """

    def __init__(self):
        self.name = "Dealer"
        self.hand = []

    def __str__(self):
        return f"{self.name} is the dealer"

    def view_cards(self, hide_second_card=True):
        """view the cards in hand
        """
        print(f"{self.name}'s hand:")
        # only show the first card
        print(self.hand[0])
        if hide_second_card:
            print("< hidden card >")
        else:
            for card in self.hand[1:]:
                print(card)


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
        while True:
            choice = input("--> Hit or Stand? ").lower()
            if choice == "hit":
                self.give_card(self.player)
                self.player.view_cards()
                self.player.view_hand_value()
                hand_value = self.player.get_hand_value()
                if hand_value == 21:
                    self.dealer_turn()
                    break
                elif hand_value > 21:
                    print(
                        f"--> {self.player.name} has busted! <--")
                    self.end_game()
                    break
            elif choice == "stand":
                self.dealer_turn()
                break
            else:
                print("--> Invalid input. Please enter 'hit' or 'stand' <--")
                continue

    def dealer_turn(self):
        """dealer follows house rules to draw cards
        """
        print("\nDealer's turn...\n")
        while self.dealer.get_hand_value() < 17:
            self.give_card(self.dealer)
        self.dealer.view_cards(hide_second_card=False)
        self.dealer.view_hand_value()
        self.end_game()

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
        self.player.view_hand_value()
        print()

        # two cards for dealer ---
        self.give_card(self.dealer)
        self.give_card(self.dealer)

        # print dealer info ---
        # hide second card ---
        self.dealer.view_cards(True)
        print()

    def end_game(self):
        """determine the winner and end the game
        """
        player_final_score = self.player.get_hand_value()
        dealer_final_score = self.dealer.get_hand_value()

        if player_final_score > 21:
            print(" * * * Dealer wins! * * * ")
        elif dealer_final_score > 21:
            print(
                f" * * * {self.player.name} wins! * * * ")
        elif player_final_score > dealer_final_score:
            print(
                f" * * * {self.player.name} wins! * * * ")
        elif player_final_score < dealer_final_score:
            print(" * * * Dealer wins! * * * ")
        else:
            print(" * * * It's a tie! * * * ")

        play_again = input("\nDo you want to play again? (Y/N) ").lower()
        if play_again == "y" or play_again == "yes":
            self.__init__()
        else:
            print("Thank you for playing!")


# GAME START
new_game = Game()
