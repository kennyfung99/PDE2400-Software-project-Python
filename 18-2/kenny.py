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



def Kenny():
    for x in range(0,80):
        pixels = [ (0,0,0) ] * numLEDs
        #K
        for i in range(5):                        #the frist line to be red and move forword by 1 
            pixels[60*i + x] = red
        pixels[3+x] = red
        pixels[62+x] = red
        pixels[121+x] = red
        pixels[182+x] = red
        pixels[243+x] = red
        #E
        for i in range(5):                         
            pixels[ 60*i+7 + x] = pink
        for i in range(5):
             pixels[i+8+x] = pink
        for i in range(5):
             pixels[i+128+x] = pink
        for i in range(5):
             pixels[i+248+x] = pink
        #N
        for i in range(5):                         
            pixels[ 60*i+16 + x] = green
        for i in range(5):                         
            pixels[ 60*i+20 + x] = green
        pixels[77+x] = green
        pixels[138+x] = green
        pixels[199+x] = green
        #N
        for i in range(5):                         
            pixels[ 60*i+23 + x] = bule
        for i in range(5):                         
            pixels[ 60*i+27 + x] = bule
        pixels[84+x] = bule
        pixels[145+x] = bule
        pixels[206+x] = bule
        #Y
        pixels[31+x] = purple
        pixels[92+x] = purple
        pixels[154+x] = purple
        pixels[37+x] = purple
        pixels[96+x] = purple
        for i in range(3):
            pixels[ 60*i+154 + x] = purple
        client.put_pixels(pixels)
        time.sleep(0.1)
        client.put_pixels(red)
    

pixels = [ (0,0,0) ] * numLEDs

Kenny()