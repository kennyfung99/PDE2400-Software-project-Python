from random import randint
import opc, time, math

import threading
import time
import sys

numLEDs = 360                                                                                                           #No of leds in the entire panel = 60*6
row = 6
column = 60
client = opc.Client('localhost:7890')

red=(255, 0, 0)
orange=(255, 140, 0)
yellow=(255, 230, 0)
light_green=(157, 255, 0)
green=(0, 255, 17)
dark_green=(0, 138, 9)
light_bule=(0, 234, 255)
bule=(0, 64, 255)
light_purple=(145, 59, 245)
purple=(101, 0, 217)
dark_purplr=(65, 0, 140)
light_pink=(255, 133, 247)
pink=(255, 0, 238)
color_1=(255, 0, 144)
color_2=(199, 0, 112)
color_3=(245, 0, 0)
color_4=(191, 0, 0)
color_5=(166, 0, 0)
color_6=(120, 2, 2)

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
for i in range(1):
    cresc_fill()()
