
import pygame as pg
import random
import threading

#initializing
pg.init()
screen = pg.display.set_mode((900,600))

pg.display.set_caption("PT REVOLUTION")
'''icon = pg.image.load(('icon location'))
pg.display.set_icon(icon)'''

#background
background = pg.image.load('background.png')

#Destiantion Arrows
top_arrows = (  pg.image.load('arr1.png'),
                pg.image.load('arr2.png'),
                pg.image.load('arr3.png'),
                pg.image.load('arr4.png'))

top_arrows_coord = (( 39, 20),
                    (137, 20),
                    (235, 20),
                    (333, 20),
                    (491, 20),
                    (589, 20),
                    (687, 20),
                    (785, 20))

#Input arrows
input_arr1 = pg.image.load('input_arr1.png')
input_arr2 = pg.image.load('input_arr2.png')
input_arr3 = pg.image.load('input_arr3.png')
input_arr4 = pg.image.load('input_arr4.png')

arr_img_left  = ((input_arr1, ( 39, 564)),
                 (input_arr2, (137, 564)),
                 (input_arr3, (235, 564)),
                 (input_arr4, (333, 564))
                )

arr_img_right = ((input_arr1, (491, 564)),
                 (input_arr2, (589, 564)),
                 (input_arr3, (687, 564)),
                 (input_arr4, (785, 564))
                )

# make another list pf inp_arr from 5-8 for the right side and make lists to produce 2 arrows at a time on both the sides

def select_arrow(left = True):
    if left:
        return random.choice(arr_img_left)
    else:
        return random.choice(arr_img_right)

def display_arrow(img, x, y):
    screen.blit(img, (x, y))

# displaying the score
score_value = 0
font = pg.font.SysFont('calibri', 25, pg.font.Font.bold)
def show_score(score_value):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (405,560))

'''initialized the coordinates to trick the while loop in generating the new arr_images 
   as condition gives is arr_ychange < 20''' 
arr_xchange_l, arr_ychange_l = (0, 10)
arr_xchange_r, arr_ychange_r = (0, 10)

game_run = True
while game_run:

    screen.blit(background, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_run = False
        
        if event.type == pg.KEYDOWN and arr_ychange_l < 170:
            if event.key == pg.K_a and arrow_img_l == input_arr1:
                    score_value+=1
            if event.key == pg.K_s and arrow_img_l == input_arr2:
                    score_value+=1
            if event.key == pg.K_w and arrow_img_l == input_arr3:
                    score_value+=1
            if event.key == pg.K_d and arrow_img_l == input_arr4:
                    score_value+=1

            if event.key == pg.K_LEFT and arrow_img_r == input_arr1:
                    score_value+=1
            if event.key == pg.K_DOWN and arrow_img_r == input_arr2:
                    score_value+=1
            if event.key == pg.K_UP and arrow_img_r == input_arr3:
                    score_value+=1
            if event.key == pg.K_RIGHT and arrow_img_r == input_arr4:
                    score_value+=1           

    
    for i in range(8):
        screen.blit(top_arrows[i%4], top_arrows_coord[i])

    

    arr_ychange_l -= 4
    arr_ychange_r -= 4

    # generate the new arrows at different y-axis distances in left and right side
    # y = 170 dotted line

    if arr_ychange_l < 20:
        arrow_img_l,coord_l = select_arrow(True)
        arr_xchange_l = coord_l[0]
        arr_ychange_l = coord_l[1]

    # if event.type == pg.KEYDOWN:
    #     print(event.key)
   
    if arr_ychange_r < 20:
        arrow_img_r,coord_r = select_arrow(False)
        arr_xchange_r = coord_r[0]
        arr_ychange_r = coord_r[1]

    display_arrow(arrow_img_l, arr_xchange_l, arr_ychange_l)
    display_arrow(arrow_img_r, arr_xchange_r, arr_ychange_r)
    show_score(score_value)
    pg.display.update()

pg.quit() #for quit event
            
