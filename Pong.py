#http://www.codeskulptor.org/#user47_zjRNV5Ag6Y_12.py - can play here

import simplegui
import random

FRAMEHEIGHT = 700
FRAMEWIDTH = 1200
BALL_RAD = 15
velocity = [0,0]
ball_pos = [600,350]
p1_position = [[1180,300],[1180,400],[1200,400],[1200,300]]
velocity_p1 = 0
p2_position = [[0,300],[0,400],[20,400],[20,300]]
velocity_p2 = 0
score_p1 = 0
score_p2 = 0
space_key_usage = 0
space_start1 = 'Press Space'
space_start2 = 'To Start'

def draw_handler(canvas):
    canvas.draw_line((600,0),(600,700),5,'White')
    canvas.draw_line((20,0),(20,700),3,'White')
    canvas.draw_line((1180,0),(1180,700),3,'White')
    canvas.draw_circle((600,350),4,5,'Green')
    canvas.draw_circle((600,350),100,5,'Yellow')
    canvas.draw_circle((600,350),2,5,'White')
    
    global ball_pos, velocity, space_key_usage, score_p1, score_p2, space_start1,space_start2
    ball_pos[0] += velocity[0]
    ball_pos[1] += velocity[1]
    if ball_pos[1] <= BALL_RAD:
        velocity[1] = -velocity[1]
    if ball_pos[1] >= FRAMEHEIGHT - BALL_RAD:
        velocity[1] = -velocity[1]
    if (ball_pos[0] <= 20 + BALL_RAD) and (p2_position[0][1] < ball_pos[1] < p2_position[1][1]):
        velocity[0] = -velocity[0]
    if (ball_pos[0] <= BALL_RAD) and not (p2_position[0][1] < ball_pos[1] < p2_position[1][1]):
        ball_pos = [600,350]
        velocity = [0,0]
        space_key_usage = 0
        score_p2 += 1
        space_start1 = 'Press Space'
        space_start2 = 'To Start'
    if (ball_pos[0] >= 1180 - BALL_RAD) and (p1_position[0][1] < ball_pos[1] < p1_position[1][1]):
        velocity[0] = -velocity[0]
    if (ball_pos[0] >= 1180 - BALL_RAD) and not (p1_position[0][1] < ball_pos[1] < p1_position[1][1]):
        ball_pos = [600,350]
        velocity = [0,0]
        score_p1 += 1
        space_start1 = 'Press Space'
        space_start2 = 'To Start'
        space_key_usage = 0
        
    canvas.draw_circle(ball_pos,BALL_RAD,3,'White','Orange')

    for i,j in enumerate(p1_position):
        p1_position[i][1] += velocity_p1 
    canvas.draw_polygon(p1_position,3,'White','Red')
    for i,j in enumerate(p2_position):
        p2_position[i][1] += velocity_p2 
    canvas.draw_polygon(p2_position,3,'White','Blue')
    

    canvas.draw_text(str(score_p1), (290, 690), 100, 'Blue')
    canvas.draw_text(str(score_p2), (890, 90), 100, 'Red')
    canvas.draw_text(space_start1, (80, 100), 100, 'Blue')
    canvas.draw_text(space_start2, (750, 650), 100, 'Red')
    
    canvas.draw_text('H', (540, 370), 50, 'White')
    canvas.draw_text('P', (630, 370), 50, 'White')
    
    
def key_handlerdown(key):
    
    global velocity, space_key_usage, score_p1, score_p2, space_start1,space_start2
    if key == simplegui.KEY_MAP['space'] and space_key_usage == 0:
        velocity = random.choice([[-20,4],[20,4]])
        space_start1,space_start2 = ' ',' '
        space_key_usage = 1
    
    global velocity_p1,velocity_p2
    if key == simplegui.KEY_MAP['up']:
            velocity_p1 += -25
    if key == simplegui.KEY_MAP['down']:
            velocity_p1 += 25
    if key == simplegui.KEY_MAP['w']:
            velocity_p2 += -25
    if key == simplegui.KEY_MAP['s']:
            velocity_p2 += 25
def key_handlerup1(key):
    global velocity_p1,velocity_p2
    velocity_p1 = 0
    velocity_p2 = 0  

def reset():
    global velocity, ball_pos, p1_position, velocity_p1, velocity_p2, score_p1, score_p2, space_key_usage, space_start1, space_start2 
    velocity = [0,0]
    ball_pos = [600,350]
    p1_position = [[1180,300],[1180,400],[1200,400],[1200,300]]
    velocity_p1 = 0
    p2_position = [[0,300],[0,400],[20,400],[20,300]]
    velocity_p2 = 0
    score_p1 = 0
    score_p2 = 0
    space_key_usage = 0
    space_start1 = 'Press Space'
    space_start2 = 'To Start'
        
        
frame = simplegui.create_frame('PONG', FRAMEWIDTH,FRAMEHEIGHT)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_handlerdown)
frame.set_keyup_handler(key_handlerup1)
frame.add_button('RESET GAME',reset)

frame.start()