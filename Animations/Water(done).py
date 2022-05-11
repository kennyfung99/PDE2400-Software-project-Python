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





def Water():
    for x in range(80):
        pixels = [ (0,0,0) ] * numLEDs
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
        
    

pixels = [ (0,0,0) ] * numLEDs
Water()
