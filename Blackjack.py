import random 

class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.ranks = [
            {'rank' : 'A', 'value' : 11 },
            {'rank' : 2, 'value' : 2},
            {'rank' : 3, 'value' : 3},
            {'rank' : 4, 'value' : 4},
            {'rank' : 5, 'value' : 5},
            {'rank' : 6, 'value' : 6},
            {'rank' : 7, 'value' : 7},
            {'rank' : 8, 'value' : 8},
            {'rank' : 9, 'value' : 9},
            {'rank' : 10, 'value' : 10},    
            {'rank' : 'J', 'value' : 10},
            {'rank' : 'Q', 'value' : 10},
            {'rank' : 'K', 'value' : 10},
        ] 
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append (Cards(suit, rank))

    def shuffle (self):
       if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal (self, n):
        cards_dealt = []
        for x in range(n):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt


class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"
    

class Hands:

    def __init__(self, dealer=False):
        self.hand = []
        self.value = 0
        self.dealer = dealer
    def add_card(self, card_list):
        self.hand.extend(card_list)
    
    def calculate_values(self):
        self.value = 0
        has_ace = False
        
        for cards in self.hand:
            card_value = int(cards.rank['value'])
            self.value += card_value
        if cards.rank['rank'] == 'A':
            has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_values()
        return self.value
    
    def blackjack(self):
            return self.get_value() == 21
    
    def display(self, show_all = False):
        print (f'''{"Dealer´s" if self.dealer == True else "Your"} hand: ''')
    
        for index, cards in enumerate(self.hand):
            if index == 0 and self.dealer and not show_all and not self.blackjack():
                print('Hidden')
            else:
                print(cards) 
        if not self.dealer:
            print('Value: ', self.get_value())
        print()


class Game():

    def play (self):
        games_played = 0
        games_future = 0
        while games_future == 0:
                try:
                    games_future += int(input('How many games do you want to play?\n'))
                except: 
                 print('You must enter a number')
        
        while games_played < games_future:
            games_played += 1
    
            deck = Deck()
            deck.shuffle()

            player_hand = Hands()
            dealer_hand = Hands(dealer=True)

            for x in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
            
            player_value = player_hand.get_value()
            dealer_value = dealer_hand.get_value()
           
           
            print()
            print('*' * 30)
            print(f'Game {games_played} of {games_future}')
            print('*' * 30)
            print()
            player_hand.display()
            dealer_hand.display()
            
            if self.check_win(player_hand, dealer_hand):
                self.results(player_value, dealer_value)
                continue
        
        
            choice = ''
            while player_hand.get_value() < 21 and choice not in ['s', 'stand']:
                choice = input('Hit or stay?\n').lower()
                print()
                while choice not in ['s', 'h', 'stand', 'hit']:
                    choice = input('Your options are: stand (s) or hit (h)\n').lower()
                    print()
                if choice in ['h', 'hit']:
                    player_hand.add_card(deck.deal(1))
                    player_value = player_hand.get_value()
                    player_hand.display()
    

            while dealer_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_value = dealer_hand.get_value()
            
            if self.check_win(player_hand, dealer_hand):
                self.results(player_value, dealer_value)
                continue
            
            dealer_hand.display(show_all=True)
           
            if self.check_win(player_hand, dealer_hand, game_over=True):
                self.results(player_value, dealer_value)
                continue
           
        


    def check_win(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print('You busted, you lose')
                return True
            elif dealer_hand.get_value() >21:
                    print('Dealer busted, you win!!')
                    return True
            elif dealer_hand.blackjack() and player_hand.blackjack():
                    print('Both of you have blackjack, tie')
                    return True
            elif player_hand.blackjack():
                    print('You have blackjack, you win!!')
                    return True
            elif dealer_hand.blackjack():
                    print('The dealer has a blackjack, you lose')
                    return True
            else:
                return False
        if game_over:
            if dealer_hand.get_value() > 21:
                print('Dealer busted, you win!!')
            elif player_hand.get_value() > dealer_hand.get_value():
                print('You win!!')
                return True
            elif player_hand.get_value() < dealer_hand.get_value():
                print('You lose!!')
                return True
            elif player_hand.get_value() == dealer_hand.get_value():
                print('It is a tie')
                return True
    
    def results(self, player_value, dealer_value):
        print('Final results: ')
        print('your hand', player_value)
        print('Dealer´s hand', dealer_value)
           
        

a = Game()
a.play()
            
