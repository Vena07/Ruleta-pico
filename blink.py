import machine,time,random

# Dokumentace zapojení kabelu:
    # led1 do GP1
    # led2 do GP2
    # led3 do GP3
    # button1 do GP4 
    # buzzer do GP5 



led1 = machine.Pin(1,machine.Pin.OUT)
led2 = machine.Pin(2,machine.Pin.OUT)
led3 = machine.Pin(3,machine.Pin.OUT)


button = machine.Pin(4,machine.Pin.IN,machine.Pin.PULL_DOWN)
buzzer =  machine.PWM(machine.Pin(5))


def play_tone(frequency, duration):
    buzzer.freq(frequency)
    buzzer.duty_u16(1200)
    time.sleep(duration)
    buzzer.duty_u16(0)  


def play_win_melody():
    melody = [
        (523, 0.2), (523, 0.2), (523, 0.2), (659, 0.2), (784, 0.2), 
        (1046, 0.2), (784, 0.2), (659, 0.2), (523, 0.2), (392, 0.2),
        (330, 0.2), (523, 0.2), (523, 0.2), (523, 0.2), (659, 0.2), 
        (784, 0.2), (1046, 0.2), (784, 0.2), (659, 0.2), (523, 2)
    ]
    for tone in melody:
        play_tone(tone[0], tone[1])

def play_loss_melody():
    melody = [
        (392, 0.5), (370, 0.5), (349, 0.5), (330, 0.5), (294, 1)
    ]  
    for tone in melody:
        play_tone(tone[0], tone[1])

def play_beep():
    buzzer.freq(1000)  
    buzzer.duty_u16(1200)  
    time.sleep(0.1)  
    buzzer.duty_u16(0) 

led3.value(0)
led2.value(0)
led1.value(0)

while True:
    cislo = random.randint(1,3)
    vybrano = True
    while vybrano == True:
        vase_cislo = int(input("Vyberte si 1 / 2 / 3 : "))
        if 0<vase_cislo<4:
            vybrano = False
            print("Pro spusteni rulety zmasknete tlacitko 1:")
            zmacknuto = True
        else:
            print("špatný výběr")
            print("")
    


    while zmacknuto == True:
        if button.value() == 1:
            zmacknuto = False
    for i in range(8):
        led3.value(0)
        led1.value(1)
        play_beep()
        time.sleep(i/10)
        led1.value(0)
        led2.value(1)
        play_beep()
        time.sleep(i/10)
        led2.value(0)
        led3.value(1)
        play_beep()
        time.sleep(i/10)
    if cislo == 1:
        led3.value(0)
        led1.value(1)
        play_beep()
        time.sleep(i/10)    
        if cislo == vase_cislo:
            play_win_melody()
            print("Vyhra!!")
        else:
            play_loss_melody()
            print("Prohra!!")
    elif cislo == 2:
        led3.value(0)
        led1.value(1)
        play_beep()
        time.sleep(i/10)
        led1.value(0)
        led2.value(1)
        play_beep()
        time.sleep(i/10)
        if cislo == vase_cislo:
            play_win_melody()
            print("Vyhra!!")
        else:
            play_loss_melody()
            print("Prohra!!")
    else:
        if cislo == vase_cislo:
            play_win_melody()
            print("Vyhra!!")
        else:
            play_loss_melody()
            print("Prohra!!")
        
        
        

            
        




