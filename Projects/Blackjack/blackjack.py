'''
* Computer dealer vs human player
* Human player places a bet
* Player starts with two cards face up
* Computer starts with one card face up and one face down
* Player goal : get closer to total value of 21 than the dealer does
* Possible actions: 1.HIT: receive another card 2.Stay: stop receiving cards\

Special Rules: Face cards(Jack, Queen, King) count as a value of 10 and Aces can count as either 1 or 11 which ever is prefrable.
 GamePlay Steps:
    1. Create a deck of 52 cards
    2. Shuffle the deck
    3. Ask the Player for their bet
    4. Make sure that the Player's bet does not exceed their available chips
    5. Deal two cards to the Dealer and two cards to the Player
    6. Show only one of the Dealer's cards, the other remains hidden
    7. Show both of the Player's cards
    8. Ask the Player if they wish to Hit, and take another card
    9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
    10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
    11. Determine the winner and adjust the Player's chips accordingly
    12. Ask the Player if they'd like to play again
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

game_on = True

"""
    Card object has a suit and a rank
    Card object really only needs two attributes: suit and rank
    Add an attribute for "value" - we chose to handle value later when developing our Hand class.
"""


class Card:

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# card1 = Card('Two','Hearts')
# print(card1,card1.value,card1.suit,card1.rank)

"""
Here we might store 52 card objects in a list that can later be shuffled. 
First, though, we need to instantiate all 52 unique card objects and add them to our list. 
So long as the Card class definition appears in our code, we can build Card objects inside our Deck __init__ method. 
Consider iterating over sequences of suits and ranks to build out each card. This might appear inside a Deck class __init__ method:
"""


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n' + card.__str__()
        return "The deck has: " + deck_composition

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


# test_deck = Deck()
# print(test_deck)
# test_deck.shuffle()
# print(test_deck)

"""
In addition to holding Card objects dealt from the Deck, 
the Hand class may be used to calculate the value of those cards using the values dictionary defined above. 
It may also need to adjust for the value of Aces when appropriate.
"""


class Hand:

    def __init__(self):
        self.cards = []  # Start with an empty list
        self.value = 0  # Start with a zero value
        self.aces = 0  # To keep Track of Aces

    def add_card(self, card):
        # card passed in from Deck.deal() -> single Card(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # If total value > 21 and I still have an Ace
        # Than change my ace to 1 instead of 11
        # self.aces implies self.aces > 0, if 0 it is treated as False

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


test_deck = Deck()
test_deck.shuffle()
'''Test
    # PLAYER
    test_player = Hand()
    # Deal 1 card from the deck Card(suit,rank)
    pulled_card = test_deck.deal()
    print(pulled_card)
    test_player.add_card(pulled_card)
    print(test_player.value)
    # simplified code
    test_player.add_card(test_deck.deal())
    print(test_player.value)
'''

"""
In addition to decks of cards and hands, we need to keep track of a Player's starting chips, bets, and ongoing winnings.
This could be done using global variables, but in the spirit of object oriented programming, let's make a Chips class instead!
"""


class Chips:

    def __init__(self):
        self.total = 100  # Can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


'''
Since we're asking the user for an integer value, this would be a good place to use try/except. 
Remember to check that a Player's bet can be covered by their available chips.
'''


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet'))
        except:
            print("Please provide a valid integer")
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! you have only', chips.total)
            else:
                break


'''
Either player can take hits until they bust.
This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17. 
It should take in Deck and Hand objects as arguments, and deal one card off the deck and add it to the Hand. 
You may want it to check for aces in the event that a player's hand exceeds 21.
'''


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


'''
This function should accept the deck and the player's hand as arguments, and assign playing as a global variable.
If the Player Hits, employ the hit() function above. 
If the Player Stands, set the playing variable to False - this will control the behavior of a while loop later on in our code.
'''


def hit_or_stand(deck, hand):
    global game_on  # To control an upcoming while loop

    while True:
        x = input('Hit or Stand ?')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands, Dealer's Turn")
            game_on = False

        else:
            print("Please enter Hit or Stand")
            continue

        break


'''
When the game starts, and after each time Player takes a card, the dealer's first card is hidden and all of Player's cards are visible. 
At the end of the hand all cards are shown, and you may want to show each hand's total value. 
Write a function for each of these scenarios.
'''


def show_some(player, dealer):
    print("\nDealer's Hand")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


'''
Functions to handle end of game scenarios.
Remember to pass player's hand, dealer's hand and chips as needed.
'''


def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! BUST DEALER!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS! BUST PLAYER!")
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and player tie! PUSH')


while True:
    # Print an opening statement
    print("WELCOME TO BLACKJACK")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while game_on:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print('\n Player total chips are at')

    # Ask to play again
    play_again = input("Would you like to play again? y/n")

    if play_again[0].lower() == 'y':
        game_on = True
        continue
    else:
        print('Thank you for playing')
        break

# not a big fan of gambling, so did'nt understand a lot of logic so followed his walkthrough/ code-along