import opc, time

numLEDs = 360
client = opc.Client('localhost:7890')

yellow = (255, 255, 0)

#while True:
 #   for i in range(numLEDs):
  #      pixels = [ (0,0,0) ] * numLEDs
   #     pixels[i] = (255, 0, 0)
    #    client.put_pixels(pixels)
     #   time.sleep(0.1)

def HI():
    for x in range(0,40):
        pixels = [ (0,0,0) ] * numLEDs
        pixels[10+x] = yellow
        pixels[70+x] = yellow
        pixels[130+x] = yellow
        pixels[190+x] = yellow
        pixels[250+x] = yellow
        pixels[131+x] = yellow
        pixels[132+x] = yellow
        pixels[133+x] = yellow
        pixels[134+x] = yellow
        pixels[15+x] = yellow
        pixels[75+x] = yellow
        pixels[135+x] = yellow
        pixels[195+x] = yellow
        pixels[255+x] = yellow

        pixels[20+x] = yellow
        pixels[80+x] = yellow
        pixels[140+x] = yellow
        pixels[200+x] = yellow
        pixels[260+x] = yellow

        client.put_pixels(pixels)
        time.sleep(0.5)
    

pixels = [ (0,0,0) ] * numLEDs

HI()