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
        
Winner()
