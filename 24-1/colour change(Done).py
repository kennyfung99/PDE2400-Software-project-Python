

import opc, time

numLEDs = 512
client = opc.Client('localhost:7890')

black = [ (0,0,0) ] * numLEDs
white = [ (255,255,255) ] * numLEDs
blue =[(0,4,255)] * numLEDs
yollow =[(251,255,0)] * numLEDs

while True:
    client.put_pixels(white)
    time.sleep(0.2) 
    client.put_pixels(black)
    time.sleep(0.05)
    client.put_pixels(yollow)
    time.sleep(0.3) 
    client.put_pixels(blue)
    time.sleep(0.05)