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
white=(255, 255, 255)






def ice():
    for x in range(1):
        pixels = [ (0,0,0) ] * numLEDs
       

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
        
    

pixels = [ (0,0,0) ] * numLEDs
ice()
