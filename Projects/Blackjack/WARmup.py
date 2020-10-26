import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# print(suits[0])
# print(ranks[0])
two_hearts = Card(suits[0], ranks[0])


#
# print('Rank: ',two_hearts.rank)
# print('Value: ',two_hearts.value)
# print(values[two_hearts.rank])

class Deck:

    def __init__(self):

        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # assuming that card class has already been defined
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        # remove one card from the list of all_cards
        return self.all_cards.pop()


# mydeck = Deck()
# print('Before Shuffling -', mydeck.all_cards[51])
# mydeck.shuffle()
# print('After Shuffling -', mydeck.all_cards[51])
#
# my_card = mydeck.deal_one()
# # pops the last card from the deck
# print('My Card: ',my_card)

class Player:

    def __init__(self, name):
        self.name = name
        # A new player will have no cards
        self.all_cards = []

    def remove_one(self):
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


# john = Player("John")
# john.add_cards([two_hearts,two_hearts,two_hearts])
# print(john)

# War Game Logic
player_one = Player("One")
player_two = Player("Two")

#Setup New Game
new_deck = Deck()
new_deck.shuffle()

for x in range (int(len(new_deck.all_cards)/2)):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# print(player_one)
# print(player_two)
# print("Cards left in deck ",len(new_deck.all_cards))

import pdb
game_on =True

rounds_num = 0
while game_on:
    rounds_num += 1
    print(f"Round{rounds_num}")
    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break

    #If not the game will keep on going on

    # Start a new round and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        print('Player One has', player_one_cards[-1], 'Player Two has', player_two_cards[-1])
        print( player_one, player_two)
        if player_one_cards[-1].value > player_two_cards[-1].value :
            #Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            #no longer at war, proceed for next round
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value :
            # Player two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            # no longer at war, proceed for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.

            # First check to see if player has enough cards

            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break
            
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player Two Loses!")
                game_on = False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                



