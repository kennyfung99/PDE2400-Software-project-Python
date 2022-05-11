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
window.configure(background="Black")


#setup for RGB
colour = 1.0 ##maximum colour
Brightness = 1.0 ##maximum brightness
number_LED=360
numLEDs = 360
pixels = [ (0,0,0) ] * numLEDs




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
#game LED-----------------------------       
def Fire():
    pixels = [ (0,0,0) ] * numLEDs
    for blink in range(4):   #blinks 4 times
        for x in range(1):
            #F
            for i in range(5):                        #the frist line to be red and move forword by 1
                pixels[60*i + x] = red 
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
            time.sleep(0.5)
            pixels = [ (0,0,0) ] * numLEDs
            client.put_pixels(pixels)
            time.sleep(0.5)
        
#ice--       
def Ice():
    pixels = [ (0,0,0) ] * numLEDs
    for bright in range (25):
        bule = (0, (bright*5), (bright*10))
        white = ((bright*10),(bright*10),(bright*10))
    
        for x in range(1):
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

#water--
def Water():
    for x in range(60):
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
#winner--        
def Winner():
    for x in range(60):
        pixels = [ (0,0,0) ] * numLEDs
        #w
        for i in range(2):  pixels[60*i+7 + x] = yellow
        pixels[60*2+7+x]= yellow
        pixels[60*3+8+x]= yellow
        pixels[60*4+9+x]= yellow
        pixels[60*3+10+x]= yellow
        pixels[60*2+11+x]= yellow
        pixels[72+x]= yellow
        pixels[60*2+13+x]= yellow
        pixels[60*3+14+x]= yellow
        pixels[60*4+15+x]= yellow
        pixels[60*3+16+x]= yellow
        pixels[60*2+17+x]= yellow
        for i in range(2):  pixels[60*i+17 + x] = yellow
        #I
        for i in range(5):  pixels[i+22+x] = bule
        for i in range(5):  pixels[60*i+24 + x] = bule
        for i in range(5):  pixels[i+60*4+22+x] = bule
        #N
        for i in range(5):  pixels[60*i+30+ x] = green
        pixels[91+x]= green
        pixels[152+x]= green
        pixels[213+x]= green
        for i in range(5):  pixels[60*i+34+ x] = green
        #N
        for i in range(5):  pixels[60*i+39+ x] = pink
        pixels[100+x]= pink
        pixels[159+x]= pink
        pixels[222+x]= pink
        for i in range(5):  pixels[60*i+43+ x] = pink
        #R
        for i in range(5):  pixels[60*i+48+ x] = purple
        for i in range(4):  pixels[i+49+x] = purple
        for i in range(4):  pixels[i+60*2+49+x] = purple
        pixels[60*1+52+x]= purple
        pixels[60*3+51+x]= purple
        pixels[60*4+52+x]= purple
        client.put_pixels(pixels)
        time.sleep(0.1)
        




#Game------------------------------------------------------------------------------
#SETUP:

import random

computer = {     
  "card_symbol":"",
  "card_number":-1,
  "Fire": 0,
  "Ice": 0,
  "Water": 0,
}

player1 = {
  "card_symbol":"",
  "card_number":-1,
  "Fire": 0,
  "Ice": 0,
  "Water": 0,
}

player2 = {
  "card_symbol":"",
  "card_number":-1,
  "Fire": 0,
  "Ice": 0,
  "Water": 0,
}

Symbol = ["Fire","Ice","Water"]

#Functions-----------------------------------------------------
def Game():
  while True:
    #Main Menu Options
    print("Welcome to Fire Ice Water!\n\
        1 - How to play\n\
        2 - Start 2 player game \n\
        3 - Start Vs Computer\n\
        4 - Exit")
  
    Choice = input('Choice: ')
    if Choice == "1":
      print('How to play')
  
    elif Choice == "2":
      Two_Player()
      break
  
    elif Choice == "3":
      Vs_Computer()
      break
  
    elif Choice == "4":
      break
    
    else: 
      print ("Sorry please enter a number from 1 to 4: ")

def get_player(player):
  if player == 0:
    return computer
  elif player == 1:
    return player1
  elif player == 2:
    return player2
  
def score_player(player):
  print ("----------------------------------------")
  print ("Player", player, " cards collected:")
  print ("Fire:", get_player(player)["Fire"]   )
  print ("Ice: ", get_player(player)["Ice"])
  print ("Water: ", get_player(player)["Water"], "\n")


#Choose a card 
def choose_card(player):
  if player == 0:                       #If player is computer it will return a random card choice
    return ((random.randint(0,5))-1) 
  else:
    while True:
        try:                            #Try to choose a card with players input
            card_choice = int(input("Choose a card from 1 to 5: "))

            
            #exception handling needed to run the rest of the code and choose a card
            if (0 <= (card_choice-1)  < 5):
                return (card_choice-1)
                break

            else:
                print ("Sorry please enter a number from 1 to 5: ")
                
        #Exception handling if input is a string instead of integer
        except ValueError:                          
            print ("Please enter a number")
            
      

def Cards(player):
  playerStr = ""
  if player == 0:
    playerStr = "Computer"
  elif player == 1:
    playerStr = "Player 1"
  elif player == 2:
    playerStr = "Player 2"
    
  print("Card options for", playerStr) #input
  #if statement for player
  #random selection of cards
  card_numbers = [0,0,0,0,0]
  card_symbols = [0,0,0,0,0]
  
  for x in range(5):
    card_numbers[x] = random.randint(0,10)
    card_symbols[x] = random.choice(Symbol)
    print ((x+1), ": [",card_symbols[x],"-",card_numbers[x],"]")
  
  

  Your_card = choose_card(player)
  print (playerStr," chose card ",": [",card_symbols[Your_card],"-",card_numbers[Your_card],"]\n")
  
  #Update card number and symbol chosen
  get_player(player).update({"card_number": card_numbers[Your_card]})
  get_player(player).update({"card_symbol": card_symbols[Your_card]})
  

def compare_cards(first, second):
  secondStr = ""
  if (second == 0):
    secondStr = "Computer"
  elif (second == 2):
    secondStr = "Player 2" 
  else:
    print("Invalid player")
    
  if (get_player(first)["card_symbol"] == "Fire" and get_player(second)["card_symbol"] == "Ice"):
    print ("Player 1 scores a point")
    get_player(first).update({"Fire": +1})
    Fire()
    
  elif (get_player(first)["card_symbol"] == "Fire" and get_player(second)["card_symbol"] == "Water"):
    print (secondStr +" scores a point")
    get_player(second).update({"Water": +1})
    Water()

  elif (get_player(first)["card_symbol"] == "Water" and get_player(second)["card_symbol"] == "Fire"):
    print ("Player 1 scores a point")
    get_player(first).update({"Water": +1})
    Water()

  elif (get_player(first)["card_symbol"] == "Water" and get_player(second)["card_symbol"] == "Ice"):
    print (secondStr +" scores a point")
    get_player(second).update({"Ice": +1})
    Ice()

  elif (get_player(first)["card_symbol"] == "Ice" and get_player(second)["card_symbol"] == "Water"):
    print ("Player 1 scores a point")
    get_player(first).update({"Ice": +1})
    Ice()

  elif (get_player(first)["card_symbol"] == "Ice" and get_player(second)["card_symbol"] == "Fire"):
    print (secondStr +" scores a point")
    get_player(second).update({"Fire": +1})
    Fire()

  
  elif (get_player(first)["card_symbol"] == get_player(second)["card_symbol"]):
    if ( (get_player(first)["card_number"]) > (get_player(second)["card_number"])):
      print ("Player 1 scores a point")
      get_player(first).update({get_player(first)["card_symbol"]: +1})
  
    elif ( get_player(first)["card_number"] < get_player(second)["card_number"]):
      print (secondStr +" scores a point")
      get_player(second).update({get_player(second)["card_symbol"]: +1})
      
    elif ( get_player(first)["card_number"] == get_player(second)["card_number"]):
      print ("Draw! One point each")
      get_player(first).update({get_player(first)["card_symbol"]: +1})
      get_player(second).update({get_player(second)["card_symbol"]: +1})

#Function to end game and find a winner
def End_game(first, second):
  #If player1 has 4 cards or more of the same element
  if ((get_player(first)["Fire"] > 3) or (get_player(first)["Ice"] > 3) or (get_player(first)["Water"] > 3)):
    print ("Player 1 wins!")
    return True

  #If player2 has 4 cards or more of the same element
  elif ((get_player(second)["Fire"] > 3) or (get_player(second)["Ice"] > 3) or (get_player(second)["Water"] > 3)):
    print ("Player 2 wins!")
    return True

  #If player1 has cards for each element
  elif ((get_player(first)["Fire"] > 0) and (get_player(first)["Ice"] > 0) and (get_player(first)["Water"] > 0)):
    print ("Player 1 wins!")
    return True
    
  #If player2 has cards for each element
  elif ((get_player(second)["Fire"] > 0) and (get_player(second)["Ice"] > 0) and (get_player(second)["Water"] > 0)):
    print ("Player 2 wins!")
    return True
    
  else:
    return False

#2 player game structure
def Two_Player(): 
  while True:
    score_player(1)
    Cards(1)
    score_player(2)
    Cards(2)
    compare_cards(1,2)
    if bool(End_game(1,2)) == True:
        RGB()
        Winner()
        break

#Vs Computer game structure
def Vs_Computer():
  while True:
    score_player(1)
    Cards(1)
    score_player(0)
    Cards(0)
    compare_cards(1,0)
    if bool(End_game(1,0)) == True:
        RGB()
        Winner()
        break


#GUI-------------------------------------------------------------------
#geometry:

window.rowconfigure(1, minsize = 20, weight = 1)
window.rowconfigure(2, weight = 3)


#widgets/M:
Animations1_button = tk.Button(window, text = 'RGB light ', command = RGB)
Animations2_button = tk.Button(window, text = 'forward and backward fill ', command = backward_fill_bule)
Animations3_button = tk.Button(window, text = 'ice ', command = Ice)
Animations4_button = tk.Button(window, text = 'Fire ', command = Fire)
Animations5_button = tk.Button(window, text = 'Game ', command = Game)




exit_button = tk.Button(window, text = 'Exit', command = window.destroy) #destroy the window, closing the program.

#layout:
Animations1_button.grid(column = 0, row = 1, padx = 5, pady = 5)
Animations2_button.grid(column = 0, row = 2, padx = 5, pady = 5)
Animations3_button.grid(column = 0, row = 3, padx = 5, pady = 5)
Animations4_button.grid(column = 0, row = 4, padx = 5, pady = 5)
Animations5_button.grid(column = 0, row = 5, padx = 5, pady = 5)
exit_button.grid(column = 5, row = 7, sticky='e', padx = 5, pady = 5)


window.mainloop()
