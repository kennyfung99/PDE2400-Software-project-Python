from random import randint
import opc, time, math
#import numpy
import threading
import time
import sys

'''Global variables that may be used throughout this file'''
boy = True
numLEDs = 360                                                                                                           #No of leds in the entire panel = 60*6
row = 6
column = 60
client = opc.Client('localhost:7890')
print('Step 1 over')


''' Function declaration for the Vertical Fill LED Sequence'''


def vert_fill():
    pixels = [(0, 0, 0)] * numLEDs
    for i in range(column):                                                                                         # Command iterates through all leds and changes the color to the desired value
        for j in range(row):
            pixels[(60 * j) + i] = (25 * (i / 2.4) - j, 50, 25 * (i / 2.4) - j)                                     # Mathematical formula that ensures the leds are lit vertically downwards in the panel
            # pixels[numLEDs-i-1] = (173, 255, 76)                                                                  Adding this command to the code will result in the leds lighting up from the reverse
            client.put_pixels(pixels)
            time.sleep(0.01)


''' Function declaration for Gradual Fade of LEDs'''


def grad_fad():
    count = 0
    sec = 0
    bentley = [(0, 0, 0)] * numLEDs
    while True:
        sec += 0.04
        brightness = int(min(1, 1.25 + math.cos(sec)) * 255)                                                        # Trigonometry function cosine is used since it's values gradually increase and decrease from 1 to 0 and vice versa
        bentley = [(brightness + 50, brightness + 100, brightness - 50)] * numLEDs
        client.put_pixels(bentley)
        time.sleep(0.05)
        count+=1
        if count > 500:
            return



'''Function declaration for Forward/Reverse fill LED Sequence'''


def for_rev_fill():
    pixels = [(0, 0, 0)] * numLEDs
    for i in range(numLEDs):
        pixels[i] = (50, 255, 180)                                                                                  # Statement iterates in the forward direction - i.e. from led 1 to led 360
        pixels[numLEDs - i - 1] = (173, 154, 76)                                                                    # Statement iterates in the backward direction - i.e. from led 360 to led 1
        client.put_pixels(pixels)
        time.sleep(0.01)
    return



'''Function declaration for Crescent Fill LED Sequence'''


def cresc_fill():
    pixels = [(0, 0, 0)] * numLEDs
    color = randint(1, 360)
    while True:
        buddha = 3                                                                                                  # A variable that contains the value of the maximum difference in leds of the longest strip (tip of the crescent) and leds of the shortest strip (the middle of the crescent)
        for i in range(column):  # Command iterates through all leds and changes the color to the desired value
            for j in range(row):
                for k in range(buddha):
                    try:
                        pixels[(60 * j) + i + k] = (color, 200, color*2)                                            # Mathematical formula that ensures the leds are lit in the shape of a crescent
                        client.put_pixels(pixels)
                        time.sleep(0.01)
                    except IndexError:
                        print("End of led string has been reached")
                        return

                if j < 2:
                    buddha -= 1
                else:
                    buddha += 1


'''Function declaration for Bounce Game'''


def blocks():                                                                                                       # Function that creates moving blocks for the game
    jada = 6                                                                                                        # maximum width a block can have
    lamba = 5                                                                                                       # maximum height a block can have
    score = 0                                                                                                       # average spacing required between blocks for ease in play
    print('w: Move Up'
          '\n s: Move Down'
          '\n x: Exit Game')

    while True:                                                                                                     # This loop focuses on infinitely creating moving blocks for the game
        blob = randint(1, lamba)                                                                                    # random height for block stored in a variable
        bleh = randint(1, jada)                                                                                     # random width of block stored in a variable
        for shift in range(60):
            pixels = [(0, 0, 0)] * numLEDs
            pixels[359] = (255, 0, 0)
            client.put_pixels(pixels)
            for height in range(blob):                                                                              # iteration for blinking the height of block
                for width in range(bleh):                                                                               # iteration for blinking the width of the block
                    try:
                        if not pixels[(60 * (5-width)) + height + shift] == (255, 0, 0):                                         # 'If' condition checks whether the block has hit the ball. If yes, then they subsequent code will be skipped
                            pixels[(60 * (5-width)) + height + shift] = (255, 255, 255)                                          # Pixel index calculation is done in such a way that the block fills up from bottom left corner, moving to the right as it fills up
                            client.put_pixels(pixels)
                                                                                                                    #time.sleep(0.001)
                        elif pixels[(60 * (5-width)) + height + shift] == (255, 0, 0):                                           # 'Elif' that checks whether the ball struck the obstacle.
                            print('You''ve lost !!! X(|'
                                  '\n your final score is: ', score )
                            return
                    except IndexError:
                        continue
                    time.sleep(0.01)
            if shift == 59:                                                                                             # At this point, the ball has successfully cleared the obstacle. The score gets incremented and printed
                score += 10
                print(score)

            def cont():                                                                                             # Threaded function that continuously checks for user input (control for the ball) and updates accordingly
                while True:
                    if input() == 'w':
                        ctrl_up()
                    elif input() == 's':
                        ctrl_dwn()
                    elif input() == 'x':
                        exit()

            def ctrl_up():                                                                                          # Function that is called when user wants to make the ball move up
                a = int(pixels.index((255, 0, 0)))
                if not a == 60:
                    pixels[a - 60] = (255, 0, 0)
                    pixels[a] = [0, 0, 0]
                    client.put_pixels(pixels)
                    return()

            def ctrl_dwn():                                                                                         # Function that is called when user wants to make the ball move down
                a = int(pixels.index((255, 0, 0)))
                if not a == 60:
                    pixels[a + 60] = (255, 0, 0)
                    pixels[a] = [0, 0, 0]
                    client.put_pixels(pixels)

            thread1 = threading.Thread(target=cont)                                                                 # Syntax for initiating the threading process
            thread1.daemon = True
            thread1.start()


#Functions = {'1':vert_fill(), '2':for_rev_fill(), '3':cresc_fill()}


while boy == True:                                                                                                  #Main syntax - the interactive menu for the users
    print('Welcome to Kenny''s Python Project !!'
          '\n Below given are the animations and game that you can enjoy. Please make a choice: '
          '\n 1) Vertical Fill animation with gradual color fade'
          '\n 2) Gradual Fade of LEDs'
          '\n 3) Forward + Reverse Fill (at the same time)'
          '\n 4) Crescent Fill'
          '\n 5) Bounce Game'
          '\n User Input: ')

    try:                                                                                                            # conditional statements are used to check for user input and call for the appropriate function
        review = input()
        if review == '1':
            vert_fill()
        elif review == '2':
            grad_fad()
        elif review == '3':
            for_rev_fill()
        elif review == '4':
            cresc_fill()
        elif review == '5':
            blocks()

    except ValueError:
        print('wrong value given')

    print('Would you like to try out the rest (y/n)? ')
    if input() == 'n':
        boy = False
    else:
        continue




