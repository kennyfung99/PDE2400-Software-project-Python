import opc, time

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





def Wipe_screen():
    pixels = [ (0,0,0) ] * numLEDs
    for x in range(60):
            pixels[x]=dark_purplr
            pixels[x+60]=purple
            pixels[x+120]=dark_purplr
            pixels[x+180]=purple
            pixels[x+240]=dark_purplr
            pixels[x+300]=purple
            
            client.put_pixels(pixels)
            time.sleep(0.10)
            
            
        

Wipe_screen()
