import opc ,time

#setup
client = opc.Client('localhost:7890')

led_columns = 60  #60 led in  1 strip 
led_rows = 6      #6 strip 
total_led=led_columns*led_rows #total led =60*6 =360
number_LED=360
columns=60

yes=True

#color
red=(250, 0, 0)
orange=(250, 125, 0)
yellow=(255, 255, 0)
spring_green=(125,255,0)
green=(0, 255, 0)
turquoise=(0,255,125)
cyan=(0,255,255)
ocean=(0,125,255)
blue=(0,0,255)
violet=(125,0,255)
magenta=(255,0,255)
raspberry=(255,0,125)




pixels = [ (0,0,0) ] * total_led
#This is color wave 
#def color_wace  will work by printing evey line with different colour and become a color wave on a rgb keyboard

def color_wave():
    for x in range(0,60):                           #this will allow the led to move 1 forword to the end 
        for i in range(6):                          #this will allow me to put led on a rows 
            pixels[60*i + x] =red                   #this will allow me to have one row with one colour (red)and it will move 1 forword 
        for i in range(6):
            pixels[60*i +1+ x] =orange                  
        for i in range(6):
            pixels[60*i +2+ x] =yellow                 
        for i in range(6):
            pixels[60*i +3+ x] =spring_green                  
        for i in range(6):
            pixels[60*i +4+ x] =green                 
        for i in range(6):
            pixels[60*i +5+ x] =turquoise                  
        for i in range(6):
            pixels[60*i +6+ x] =cyan                  
        for i in range(6):
            pixels[60*i +7+ x] =ocean                
        for i in range(6):
            pixels[60*i +8+ x] =blue
        for i in range(6):
            pixels[60*i + 9+ x] =violet                
        for i in range(6):
            pixels[60*i +10+ x] =magenta                 
        for i in range(6):
            pixels[60*i +11+ x] =raspberry                 
        for i in range(6):
            pixels[60*i+12+ x] =red                 
        for i in range(6):
            pixels[60*i+13+ x] =orange                 
        for i in range(6):
            pixels[60*i+14+ x] =yellow                
        for i in range(6):
            pixels[60*i+15+ x] =spring_green                 
        for i in range(6):
            pixels[60*i+16+ x] =green                 
        for i in range(6):
            pixels[60*i+17+ x] =turquoise                 
        for i in range(6):
            pixels[60*i +18+x] =cyan                  
        for i in range(6):
            pixels[60*i +19+ x] =ocean                  
        for i in range(6):
            pixels[60*i +20+ x] =blue              
        for i in range(6):
            pixels[60*i +21+ x] =violet                                   
        for i in range(6):
            pixels[60*i +22+ x] =magenta                  
        for i in range(6):
            pixels[60*i +23+ x] =raspberry                  
        for i in range(6):
            pixels[60*i +24+ x] =red                  
        for i in range(6):
            pixels[60*i +25+ x] =orange                
        for i in range(6):
            pixels[60*i +26+ x] =yellow                 
        for i in range(6):
            pixels[60*i +27+ x] =spring_green                 
        for i in range(6):
            pixels[60*i +28+ x] =green                 
        for i in range(6):
            pixels[60*i +29+ x] =turquoise                 
        for i in range(6):
            pixels[60*i+30+ x] =cyan                 
        for i in range(6):
            pixels[60*i+31+ x] =ocean                 
        for i in range(6):
            pixels[60*i+32+ x] =blue                
        for i in range(6):
            pixels[60*i+33+ x] =violet                 
        for i in range(6):
            pixels[60*i+34+ x] =magenta                 
        for i in range(6):
            pixels[60*i+35+ x] =raspberry                  
        for i in range(6):
            pixels[60*i +36+x] =red                  
        for i in range(6):
            pixels[60*i +37+ x] =orange                  
        for i in range(6):
            pixels[60*i +38+ x] =yellow                  
        for i in range(6):
            pixels[60*i +39+ x] =spring_green                  
        for i in range(6):
            pixels[60*i +40+ x] =green                  
        for i in range(6):
            pixels[60*i +41+ x] =turquoise                              
        for i in range(6):
            pixels[60*i +42+ x] =cyan                  
        for i in range(6):
            pixels[60*i +43+ x] =ocean                 
        for i in range(6):
            pixels[60*i +44+ x] =blue                 
        for i in range(6):
            pixels[60*i +45+ x] =violet                 
        for i in range(6):
            pixels[60*i +46+ x] =magenta                 
        for i in range(6):
            pixels[60*i +47+ x] =raspberry                
        for i in range(6):
            pixels[60*i+48+ x] =red                 
        for i in range(6):
            pixels[60*i+49+ x] =orange                 
        for i in range(6):
            pixels[60*i+50+ x] =yellow                 
        for i in range(6):
           pixels[60*i+51+ x] =spring_green                 
        for i in range(6):
            pixels[60*i+52+ x] =green
        for i in range(6):
            pixels[60*i+53+ x] =turquoise
        for i in range(6):
            pixels[60*i +54+x] =cyan 
        for i in range(6):
            pixels[60*i +55+ x] =ocean 
        for i in range(6):
            pixels[60*i +56+ x] =blue 
        for i in range(6):
            pixels[60*i +57+ x] =violet 
        for i in range(6):
            pixels[60*i +58+ x] =magenta 
        
        client.put_pixels(pixels)
        time.sleep(0.09 )
        
color_wave()
