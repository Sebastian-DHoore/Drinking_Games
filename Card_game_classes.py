import random


class Card(object):
    def __init__(self, suit, val, showing):
        self.suit = suit
        self.value = val
        self.showing = showing

    def __unicode__(self):
        return self.show()

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    def show(self):
        if self.value == 1:
            val = "A"
        elif self.value == 11:
            val = "J"
        elif self.value == 12:
            val = "Q"
        elif self.value == 13:
            val = "K"
        else:
            val = self.value

        if self.showing:
            return "{}".format(val)
        else:
            return "Hidden card"


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print(card.show())

    # Generate 52 cards
    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(1, 14):
                self.cards.append(Card(suit, val, True))

    # Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            for i in range(length - 1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]

    # Return the top card
    def deal(self):
        return self.cards.pop()

    # Put a card in the deck and shuffle
    def refill(self, card):
        self.cards.append(card)
        self.shuffle()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.shots = 0
        self.hand = []
        self.turns = 0
        self.turnstreak = 0

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    # Display a players attributes
    def show(self):
        print("{} took {} shots, played {} turns and is on a {} turn streak".
              format(self.name, self.shots, self.turns, self.turnstreak))
        return self

    # Display a players attributes without turnstreak
    def show_without_turnstreak(self):
        print("{} took {} shots and played {} turns".
              format(self.name, self.shots, self.turns))
        return self

    # Display a players attributes and hand
    def show_with_hand(self):
        if len(self.hand) == 0:
            print("{} has an empty hand, took {} shots, played {} turns and is on a {} turn streak".
                  format(self.name, self.shots, self.turns, self.turnstreak))
        else:
            print("{} with hand: {} took {} shots, played {} turns and is on a {} turn streak".
                  format(self.name, self.hand, self.shots, self.turns, self.turnstreak))
        return self

    # Display all the cards in the players hand
    def show_hand(self):
        if len(self.hand) == 0:
            print("{}'s has an empty hand".format(self.name))
        else:
            print("{}'s hand: {}".format(self.name, self.hand))
        return self

    # Discard all cards in hand
    def discard(self):
        return self.hand.pop()

    # Adds shots to player total
    def drink(self, shots):
        self.shots += shots

    # Adds turn to player turn streak
    def turnstreak_up(self):
        self.turnstreak += 1

    # Resets player turn streak
    def turnstreak_reset(self):
        self.turnstreak = 0

    # Adds turn to player turns
    def turn_up(self):
        self.turns += 1


# Test Card
# myCard = Card('Spades', 6, True)
# print(myCard.show())

# Test Deck
# myDeck = Deck()
# myDeck.shuffle()
# myDeck.show()

# Test Player
# bas = Player("Bas")
# bas.draw(myDeck, 5)
# bas.show_hand()
