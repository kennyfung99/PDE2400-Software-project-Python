import opc ,time
import numpy
#setup
client = opc.Client('localhost:7890')

led_columns = 100  #60 led in  1 strip 
led_rows = 6      #6 strip 
total_led=led_columns*led_rows #total led =60*6 =360
number_LED=360
columns=60

yes=True

#color
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

pixels = [ (0,0,0) ] * total_led
#This is color wave 
#def color_wace  will work by printing evey line with different colour and become a color wave on a rgb keyboard

def color_wave():
    for x in range(0,60):                           #this will allow the led to move 1 forword to the end 
        for i in range(6):                          #this will allow me to put led on a rows 
            pixels[60*i + x] = red                  #this will allow me to have one row with one colour (red)and it will move 1 forword 
        for i in range(6):
            pixels[60*i +1+ x] = orange
        for i in range(6):
            pixels[60*i +2+ x] = yellow
        for i in range(6):
            pixels[60*i +3+ x] = light_green
        for i in range(6):
            pixels[60*i +4+ x] = green
        for i in range(6):
            pixels[60*i +5+ x] = dark_green
        for i in range(6):
            pixels[60*i +6+ x] = light_bule
        for i in range(6):
            pixels[60*i +7+ x] =bule
        for i in range(6):
            pixels[60*i +8+ x] =light_purple
        for i in range(6):
            pixels[60*i + 9+ x] =purple
        for i in range(6):
            pixels[60*i +10+ x] =dark_purplr
        for i in range(6):
            pixels[60*i +11+ x] =light_pink
        for i in range(6):
            pixels[60*i+12+ x] =color_1
        for i in range(6):
            pixels[60*i+13+ x] =color_2
        for i in range(6):
            pixels[60*i+14+ x] =color_3
        for i in range(6):
            pixels[60*i+15+ x] =color_4
        for i in range(6):
            pixels[60*i+16+ x] =color_5
        for i in range(6):
            pixels[60*i+17+ x] =color_6
        for i in range(6):
            pixels[60*i +18+x] = red
        for i in range(6):
            pixels[60*i +19+ x] = orange
        for i in range(6):
            pixels[60*i +20+ x] = yellow
        for i in range(6):
            pixels[60*i +21+ x] = light_green
        for i in range(6):
            pixels[60*i +22+ x] = green
        for i in range(6):
            pixels[60*i +23+ x] = dark_green
        for i in range(6):
            pixels[60*i +24+ x] = light_bule
        for i in range(6):
            pixels[60*i +25+ x] =bule
        for i in range(6):
            pixels[60*i +26+ x] =light_purple
        for i in range(6):
            pixels[60*i +27+ x] =purple
        for i in range(6):
            pixels[60*i +28+ x] =dark_purplr
        for i in range(6):
            pixels[60*i +29+ x] =light_pink
        for i in range(6):
            pixels[60*i+30+ x] =color_1
        for i in range(6):
            pixels[60*i+31+ x] =color_2
        for i in range(6):
            pixels[60*i+32+ x] =color_3
        for i in range(6):
            pixels[60*i+33+ x] =color_4
        for i in range(6):
            pixels[60*i+34+ x] =color_5
        for i in range(6):
            pixels[60*i+35+ x] =color_6 
        for i in range(6):
            pixels[60*i +36+x] = red
        for i in range(6):
            pixels[60*i +37+ x] = orange
        for i in range(6):
            pixels[60*i +38+ x] = yellow
        for i in range(6):
            pixels[60*i +39+ x] = light_green
        for i in range(6):
            pixels[60*i +40+ x] = green
        for i in range(6):
            pixels[60*i +41+ x] = dark_green
        for i in range(6):
            pixels[60*i +42+ x] = light_bule
        for i in range(6):
            pixels[60*i +43+ x] =bule
        for i in range(6):
            pixels[60*i +44+ x] =light_purple
        for i in range(6):
            pixels[60*i +45+ x] =purple
        for i in range(6):
            pixels[60*i +46+ x] =dark_purplr
        for i in range(6):
            pixels[60*i +47+ x] =light_pink
        for i in range(6):
            pixels[60*i+48+ x] =color_1
        for i in range(6):
            pixels[60*i+49+ x] =color_2
        for i in range(6):
            pixels[60*i+50+ x] =color_3
        for i in range(6):
           pixels[60*i+51+ x] =color_4
        for i in range(6):
               pixels[60*i+52+ x] =color_5
        for i in range(6):
               pixels[60*i+53+ x] =color_6
        for i in range(6):
                pixels[60*i +54+x] = red
        for i in range(6):
                pixels[60*i +55+ x] = orange
        for i in range(6):
            pixels[60*i +56+ x] = yellow
        for i in range(6):
            pixels[60*i +57+ x] = light_green
        for i in range(6):
            pixels[60*i +58+ x] = green
        
        client.put_pixels(pixels)
        time.sleep(0.09 )
def backward_fill_bule():
    pixels = [(0, 0, 0)] * number_LED
    for x in range(number_LED):
        pixels[x] = bule                                                                                  #  it make  forward direction  from 1 to  360 led 
        pixels[number_LED - x - 1] = light_bule                                                             # it make to gobackward direction from 360 to  1 led
        client.put_pixels(pixels)
        time.sleep(0.05)
    return
def HI():
    for x in range(0,20):
        pixels = [ (0,0,0) ] * total_led
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
        time.sleep(0.1)
def Kenny():
    for x in range(0,80):
        pixels = [ (0,0,0) ] * total_led
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
def P1():
    color=[(252, 3, 7),(17, 0, 255),(255,255,255),(255,192,203),(148,0,211),(251,255,0),(245, 0, 0),(191, 0, 0),(166, 0, 0),(120, 2, 2),(255, 0, 238),(255, 133, 247),(65, 0, 140),(101, 0, 217),(145, 59, 245)]*360
    for i in range (20):
        
        #print(color)
        color = numpy.roll(color,1)
        time.sleep(1) 
        client.put_pixels(color)




while yes == True:
    print('welcome to the LED show!'
        '\n choose the following option?'
        '\n a}color wave'
        '\n b}backward fill'
        '\n c}word-hi'
        '\n d}word-kenny'
        '\n e}Patterm 1'
        '\n f}show all'
        )
    
    try:
        user_input=input()
        if user_input=='a':
            color_wave()
        elif user_input=='b':
            backward_fill_bule()
        elif user_input=='c':
            HI()
        elif user_input=='d':
            Kenny()
        elif user_input=='e':
            P1()
        elif user_input=='f':
            color_wave()
            color_wave()
            time.sleep(1) 
            backward_fill_bule()
            HI()
            time.sleep(1) 
            Kenny()
            P1()

    except ValueError:
        print('incorrect value (use a,b,c,d,e,,f)')
    print('Would you want to go back to the main menu (yes/no)? ')
    
    if input()=='no':
        yes=False
    else:
        continue










