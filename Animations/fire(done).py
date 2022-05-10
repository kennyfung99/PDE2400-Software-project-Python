import opc, time
from time import sleep

numLEDs = 360
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
     




def Fire():
    for x in range(15):
        pixels = [ (0,0,0) ] * numLEDs
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
        time.sleep(0.1)
        
    

pixels = [ (0,0,0) ] * numLEDs
Fire()
