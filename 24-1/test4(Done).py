# Open Pixel Control client: Every other light to solid white, others dark.

import opc, time

numPairs = 360
client = opc.Client('localhost:7890')

black = [ (0,0,0), (0,60,255),(255,0,0) ] * numPairs
white = [ (255,255,255), (0,0,0) ] * numPairs
red=[(255,0,0)]* numPairs
bule=[(0,60,255),(255,0,0)]* numPairs

# Fade to white
client.put_pixels(black)
client.put_pixels(black)
time.sleep(2)
client.put_pixels(white)
time.sleep(2)
client.put_pixels(bule)
time.sleep(2)
client.put_pixels(red)