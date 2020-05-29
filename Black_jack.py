import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return self.rank+" of "+self.suit


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
        
    
    def __str__(self):
        for i in self.deck:
            print(i)
        return "\n"

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value=self.value+values[card.rank]
        if card.rank=='Ace':
          self.aces+=1
    
    def adjust_for_ace(self):
        while self.value<21 and self.aces:
            self.value-=10
            self.aces-=1


class Chips:
    
    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
    
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet


def take_bet(chips):
    while True:
        try:
            bet=int(input("Take a bet : "))
        except:
            print("Not a Integer!Please enter again.")
        else:
            if bet<=chips.total:
                chips.bet=bet
                break
            else:
                print("Chips are not avalable.")


def hit(deck,hand):
    return hand.add_card(deck.deal())


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        temp=input("What you want ?hit or stand type h or s :")
    
        if temp=='h':
            hit(deck,hand)
        elif temp=='s':
            print("player stand ,dealer's turn")
            playing = False
        else:
            print("sorry i can't understand you plse enter h/s.")
            continue
        break


def show_some(player,dealer):
    
    print("Player's cards : \n")
    for i in player.cards:
        print(i)    
    print("\n")
    print("Dealer's cards : \n")
    for i in range(1,len(dealer.cards)):
        print(dealer.cards[i])
        
    print("\n")


def show_all(player,dealer):
    
    print("Player's cards : \n")
    for i in player.cards:
        print(i)
    print("\n")

    print("Dealer's cards : \n")
    for i in dealer.cards:
        print(i)

    print("\n")

        
def player_busts(player,dealer,chips):
    print("player bust!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("player Win!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer bust!Player win")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer win")
    chips.lose_bet()
    
def push(player,dealer,chips):
    print("player and Dealer are tie!")



while True:
    # Print an opening statement
    
    print("*********** Welcom ****************")
  
    
    # Create & shuffle the deck, deal two cards to each player
    
    deck=Deck()
    deck.shuffle()

    player=Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    
    dealer=Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
        
    # Set up the Player's chips
    
    chips=Chips()
    
    # Prompt the Player for their bet
    
    take_bet(chips)
    
    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value>21:
            player_busts(player,dealer,chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value< 21:
            
        while dealer.value < 17:
                hit(deck,dealer)
                
             # Show all cards
        show_all(player,dealer)
        
        # Run different winning scenarios
        
        if dealer.value>21:
            dealer_busts(player,dealer,chips)
        elif dealer.value>player.value:
            dealer_wins(player,dealer,chips)
        elif dealer.value<player.value:
            player_wins(player,dealer,chips)
        else:
            push(player,dealer,chips)    
        
    
    # Inform Player of their chips total 
    print(f"Your avalable chips are {chips.total}")
    # Ask to play again
    temp = input("want to play again y/n:")
    if temp[0].lower=='y':
        continue
    else:
        break


