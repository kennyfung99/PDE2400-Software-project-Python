#setup-----------------------------------
#OPC:
import opc
import time
import random
from time import sleep
import colorsys

leds = [(255,255,255)]*360 #set background color

client = opc.Client('localhost:7890') #connect to sim
client.put_pixels(leds) #display the first colours (black)
client.put_pixels(leds)

#LED colors:
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
white=(255, 255, 255)

#tkinter:
import tkinter as tk

window = tk.Tk()  #this will generate the window for GUI.
window.title('Software project Python')



#setup for RGB
colour = 1.0 ##maximum colour
Brightness = 1.0 ##maximum brightness
number_LED=360




#Function---------------------------------------------------------
#function (RGB)

def RGB():
    for hue in range(360):
        rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, colour, Brightness) #colorsys returns floats between 0 and 1
    
        r_float = rgb_fractional[0] #extract said floating point numbers
        g_float = rgb_fractional[1]
        b_float = rgb_fractional[2]

        rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
   
        leds[hue] = rgb 
        client.put_pixels(leds) #send out the leds

        sleep(0.02) #20ms
        
#function (backward_fill_bule)      
def backward_fill_bule():
    pixels = [(0, 0, 0)] * number_LED
    for x in range(number_LED):
        pixels[x] = bule                                                                                  #  it make  forward direction  from 1 to  360 led 
        pixels[number_LED - x - 1] = light_bule                                                             # it make to gobackward direction from 360 to  1 led
        client.put_pixels(pixels)
        time.sleep(0.05)
#game LED        
def Fire():
    for x in range(15):
        pixels = [ (0,0,0) ] * number_LED
        #F
        for i in range(5):  pixels[60*i + x] = red                         #the frist line to be red and move forword by 1
        
        for i in range(4):  pixels[i+1+x] = red
        for i in range(4):  pixels[i+121+x] = red
        #I
        for i in range(5):  pixels[ 60*i+10 + x] = red
        for i in range(5):  pixels[i+8+x] = red
        for i in range(5):  pixels[i+248+x] = red
        #R
        for i in range(5):  pixels[ 60*i+16 + x] = red
        for i in range(5):  pixels[ i+16 + x] = red
        for i in range(5):  pixels[ i+136+ x] = red
        pixels[80+x]= red
        pixels[199+x]= red
        pixels[260+x]= red
        #E
        for i in range(5):  pixels[ 60*i+23 + x] = red
        for i in range(5):  pixels[ i+23+ x] = red
        for i in range(5):  pixels[ i+143+ x] = red
        for i in range(5):  pixels[ i+263+ x] = red
        #fire ball
        for i in range(5):  pixels[ i+36+ x] = red          #line 1
        pixels[95+x]= red                                   #line 2
        for i in range(5):  pixels[ i+96+ x] = orange       #line2
        for i in range(4):  pixels[ i+99+ x] = red          #line2
        for i in range(2):  pixels[ 60*i+154+ x] = red      #line 3,4 red 
        for i in range(2):  pixels[ 60*i+155+ x] = orange   #line 3,4 orange 
        for i in range(5):  pixels[ i+156+ x] = yellow      #line 3 yellow 
        for i in range(4):  pixels[ i+159+ x] = orange      #line 3 orange
        for i in range(4):  pixels[ i+161+ x] = red         #line 3 red
        for i in range(6):  pixels[ i+216+ x] = yellow      #line 4 yellow
        for i in range(4):  pixels[ i+220+ x] = orange      #line 4 orange
        for i in range(4):  pixels[ i+222+ x] = red         #line 4 red
        pixels[275+x]= red
        for i in range(5):  pixels[ i+276+ x] = orange
        for i in range(5):  pixels[ i+279+ x] = red
        for i in range(6):  pixels[ i+336+ x] = red
        client.put_pixels(pixels)
        time.sleep(0.1)
        
def ice():
    for x in range(1):
        pixels = [ (0,0,0) ] * number_LED
        #ice cube
        for i in range(5):  pixels[60*i+1+ x] = white
        for i in range(5):  pixels[60*i+2+ x] = white
        for i in range(5):  pixels[60*i+3 + x] = white
        for i in range(5):  pixels[60*i+4 + x] = white
        for i in range(5):  pixels[60*i+5 + x] = white
        for i in range(5):  pixels[60*i+6 + x] = white
        #I
        for i in range(5):  pixels[i+11+x] = bule
        for i in range(5):  pixels[60*i+13 + x] = bule
        for i in range(5):  pixels[i+251+x] = bule
        #C
        for i in range(6):  pixels[i+25+x] = bule
        for i in range(5):  pixels[60*i+25 + x] = bule
        for i in range(6):  pixels[i+265+x] = bule
        #E
        for i in range(6):  pixels[i+40+x] = bule
        for i in range(5):  pixels[60*i+40 + x] = bule
        for i in range(6):  pixels[i+280+x] = bule
        for i in range(6):  pixels[i+160+x] = bule
        #ice cube
        for i in range(5):  pixels[60*i+53+ x] = white
        for i in range(5):  pixels[60*i+54+ x] = white
        for i in range(5):  pixels[60*i+55 + x] = white
        for i in range(5):  pixels[60*i+56 + x] = white
        for i in range(5):  pixels[60*i+57 + x] = white
        for i in range(5):  pixels[60*i+58 + x] = white

        client.put_pixels(pixels)
        time.sleep(0.1)

def Water():
    for x in range(80):
        pixels = [ (0,0,0) ] * number_LED
        #w
        for i in range(2):  pixels[60*i+7 + x] = bule
        pixels[60*2+7+x]= bule
        pixels[60*3+8+x]= bule
        pixels[60*4+9+x]= bule
        pixels[60*3+10+x]= bule
        pixels[60*2+11+x]= bule
        pixels[72+x]= bule
        pixels[60*2+13+x]= bule
        pixels[60*3+14+x]= bule
        pixels[60*4+15+x]= bule
        pixels[60*3+16+x]= bule
        pixels[60*2+17+x]= bule
        for i in range(2):  pixels[60*i+17 + x] = bule
        #A
        pixels[22+x]= bule
        pixels[60*1+21+x]= bule
        pixels[60*3+19+x]= bule
        pixels[60*4+19+x]= bule
        pixels[60*1+23+x]= bule
        for i in range(5):  pixels[i+140+x] = bule
        pixels[60*3+25+x]= bule
        pixels[60*4+25+x]= bule
        #T
        for i in range(5):  pixels[i+27+x] = bule
        for i in range(5):  pixels[60*i+29 + x] = bule
        #E
        for i in range(5):  pixels[60*i+35+ x] = bule
        for i in range(4):  pixels[i+36+x] = bule
        for i in range(4):  pixels[i+60*2+36+x] = bule
        for i in range(4):  pixels[i+60*4+36+x] = bule
        #R
        for i in range(5):  pixels[60*i+42+ x] = bule
        for i in range(4):  pixels[i+43+x] = bule
        for i in range(4):  pixels[i+60*2+43+x] = bule
        pixels[60*1+46+x]= bule
        pixels[60*3+45+x]= bule
        pixels[60*4+46+x]= bule

        client.put_pixels(pixels)
        time.sleep(0.1)




#Game 

#GUI-------------------------------------------------------------------
#geometry:

window.rowconfigure(1, minsize = 20, weight = 1)
window.rowconfigure(2, weight = 3)
#widgets:
Animations1_button = tk.Button(window, text = 'RGB light ', command = RGB)
Animations2_button = tk.Button(window, text = 'forward and backward fill ', command = backward_fill_bule)
Animations3_button = tk.Button(window, text = 'ice ', command = ice)
Animations4_button = tk.Button(window, text = 'water ', command = Water)
exit_button = tk.Button(window, text = 'Exit', command = window.destroy) #destroy the window, closing the program.

#layout:
Animations1_button.grid(column = 0, row = 1, padx = 5, pady = 5)
Animations2_button.grid(column = 0, row = 2, padx = 5, pady = 5)
Animations3_button.grid(column = 0, row = 3, padx = 5, pady = 5)
Animations4_button.grid(column = 0, row = 4, padx = 5, pady = 5)
exit_button.grid(column = 5, row = 2, sticky='e', padx = 5, pady = 5)

window.mainloop()
