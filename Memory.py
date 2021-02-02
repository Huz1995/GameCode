#http://www.codeskulptor.org/#user47_fQtm2IvzbY_0.py - can play here

import simplegui
import random


deck = list(range(1,9))*2
random.shuffle(deck)
card_down = [True]*16
card_index1 = 0
card_index2 = 0
state = 0
turns = 0

def reset():
    global deck, card_down, state, turns, card_index1, card_index2
    deck = list(range(1,9))*2
    random.shuffle(deck)
    card_down = [True]*16
    card_index1 = 0
    card_index2 = 0
    state = 0
    turns = 0

def mouseclick(pos):
    global deck, card_down, state, turns, card_index1, card_index2
    clicked_index = pos[0]//50
    if card_down[clicked_index] == True:
        if state == 0:
            card_index1 = clicked_index
            card_down[card_index1] = False
            state += 1
        elif state == 1:
            card_index2 = clicked_index
            card_down[card_index2] = False
            state += 1
            if deck[card_index1] == deck[card_index2]:
                state = 0
                turns += 1
        else:
            if deck[card_index1] != deck[card_index2]:
                state = 0
                card_down[card_index1] = True
                card_down[card_index2] = True
                card_index1 = 0
                card_index2 = 0
                turns += 1
    
def draw(canvas):
    global deck, card_down, state, turns
    for i in range(16):
        if card_down[i] == False:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Black", "White")
            canvas.draw_text(str(deck[i]), (i*50+11, 69), 55, "Red")
        else:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 5, "Orange", "Red")
    label.set_text("Turns = " + str(turns))
  
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", reset)
label = frame.add_label("Turns = 0")


frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)



frame.start()
