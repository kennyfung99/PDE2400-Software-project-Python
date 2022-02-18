import opc, time

num_led=20
client = opc.Client('localhost:7890')

led_colour={
    'bule':(0,6,255),
    'red':(255, 0, 0),
    'yellow':(255, 251, 0)
    }

h=led_colour.get('bule','yellow','red')*num_led
x=led_colour.get('yellow','red','bule')*num_led

client.put_pixels(h)
time.sleep(2)
client.put_pixels(x)


