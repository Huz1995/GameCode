#http://www.codeskulptor.org/#user47_A0y1jDw1Xn_8.py - can play here

#Blackjack

import simplegui
import random

CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")   

#intro_image = simplegui.load_image('http://www.entrylevel.eu/image/fc91feb062a01eb3d52ff4970a321b05.jpg')
                                   
# initialize some useful global variables
in_play = False
starter_page = True
bust = False
stand = False
dealer_bust = False
score = 0
dealer_score = 0
win_lose = ''

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0], pos[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        handstring = ''
        for card in self.hand:
            handstring = handstring + str(card) + ' '
        if handstring == '':
            return 'Your hand is empty'
        else:
            return 'Your hand has: ' + handstring
    
    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        value = 0
        for card in self.hand:
            if value < 11:
                VALUES['A']=11
                value += VALUES[card.get_rank()]
            elif value >= 10:
                VALUES['A']=1
                value += VALUES[card.get_rank()]
        return value
        
    def draw(self, canvas, pos):
        for card in self.hand:
            pos[0] = pos[0] + self.hand.index(card)*100
            card.draw(canvas,pos)
            pos[0] = pos[0] - self.hand.index(card)*100
    
    def returnlist(self):
        handlist = []
        for card in self.hand:
            card = str(card)
            handlist.append(card)
        return handlist
 

class Deck():
    
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def returndeck(self):
        decklist = []
        for card in self.deck:
            card = str(card)
            decklist.append(card)
        return decklist
   
    def __str__(self):
        deckstring = ''
        for card in self.deck:
            deckstring = deckstring + str(card) + ' '
        if deckstring == '':
            return 'The deck is empty'
        else:
            return 'The deck has: ' + deckstring

#define event handlers for buttons
def deal():
    global outcome, in_play, playerhand, dealerhand, deck, message_player, message_dealer,bust, stand, dealer_bust
    deck = Deck()
    deck.shuffle()
    bust = False
    in_play = True
    stand = False
    dealer_bust = False
    playerhand = Hand()
    dealerhand = Hand()
    playerhand.add_card(deck.deal_card())
    playerhand.add_card(deck.deal_card())
    dealerhand.add_card(deck.deal_card())
    dealerhand.add_card(deck.deal_card())

def hit():
    global in_play, playerhand, message, score, bust, dealer_score
    if in_play:
        playerhand.add_card(deck.deal_card())
        if playerhand.get_value() > 21:
            dealer_score = +1
            in_play = False
            bust = True

def stand():
    global in_play, stand, dealer_score, bust, dealer_bust, win_lose, score
    stand = True
    in_play = False
    bust = None
    while dealerhand.get_value() < 18:
        dealerhand.add_card(deck.deal_card())
    if dealerhand.get_value() > 21:
        dealer_bust = True
        stand = False
        score += 1
    elif dealerhand.get_value() > playerhand.get_value():
        win_lose = 'You Lose This Hand'
        dealer_score += 1
    elif dealerhand.get_value() < playerhand.get_value():
        win_lose = 'You Win This Hand'
        score += 1
    elif dealerhand.get_value() == playerhand.get_value():
        win_lose = 'Tie Hand'

def key_handler(key):
    global starter_page, in_play
    if key == simplegui.KEY_MAP['space']:
        starter_page = False
        in_play = True
    
def draw(canvas):
    global starter_page, in_play, bust, stand, dealer_bust
    if starter_page:
        in_play = False
        canvas.draw_text('Welcome to BLACKJACK',(25, 100), 50, 'White')
        canvas.draw_text('Press Space to Play',(210, 210), 25, 'Yellow')
        #canvas.draw_image(intro_image, (226,340), (553,680), (300,300), CARD_BACK_SIZE)
    else:
        playerhand.draw(canvas,[50,410])
        dealerhand.draw(canvas,[50,210])
        if bust == False:
            canvas.draw_text('Your Hand: ',(20,500),25,'Yellow')
            canvas.draw_text("Dealer's Hand",(20,140),25,'Yellow')
            canvas.draw_text(str(playerhand.get_value()),(145,500),25,'Yellow')
            canvas.draw_text('Player Score: ' + str(score),(425,50),25, 'White')
            canvas.draw_text('Dealer Score: ' + str(dealer_score),(425,80),25, 'White')
            canvas.draw_text('Would you like to Hit or Stand?',(20,340),25, 'Yellow')
        if bust == True:
            canvas.draw_text('You BUST out',(20,340),50,'Red')
            canvas.draw_text('For a new hand... press Deal',(80,80),40,'White')
            canvas.draw_text(str(playerhand.get_value()),(145,500),25,'Yellow')
            canvas.draw_text('Your Hand: ',(20,500),25,'Yellow')
        if stand == True:
            canvas.draw_text('Your Hand: ',(20,500),25,'Yellow')
            canvas.draw_text("Dealer's Hand: ",(20,140),25,'Yellow')
            canvas.draw_text(str(playerhand.get_value()),(145,500),25,'Yellow')
            canvas.draw_text(str(dealerhand.get_value()),(175,140),25,'Yellow')
            canvas.draw_text('Player Score: ' + str(score),(425,50),25, 'White')
            canvas.draw_text('Dealer Score: ' + str(dealer_score),(425,80),25, 'White')
            canvas.draw_text(win_lose,(80,320),25, 'White')
        if dealer_bust == True:
            canvas.draw_text('Dealer BUST out',(20,110),50,'Red')
            canvas.draw_text('For a new hand... press Deal',(80,520),40,'White')
        if in_play:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50,210], CARD_BACK_SIZE)
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler)

# get things rolling
deal()
frame.start()