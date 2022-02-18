import opc

led_colour  =[(0,255,0)]*60
led_colour2 =[(255,255,0)]*120
led_colour3 =[(4,255,0)]*120
led_colour4 =[(0,255,238)]*120
led_colour5  =[(13,0,255)]*120


all_colour =led_colour+led_colour2+led_colour3+led_colour4+led_colour5 

client = opc.Client('localhost:7890')

client.put_pixels(all_colour)
print (all_colour)