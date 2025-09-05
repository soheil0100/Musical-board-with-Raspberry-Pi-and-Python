import pygame.mixer
import RPi.GPIO as GPIO
import signal
import os
import time
import Image

pygame.mixer.pre_init(channels=8, buffer=1024)
pygame.mixer.init()

ap=pygame.mixer.Sound("/home/pi/main/p1.wav")
bp=pygame.mixer.Sound("/home/pi/main/p2.wav")
cp=pygame.mixer.Sound("/home/pi/main/p3.wav")
dp=pygame.mixer.Sound("/home/pi/main/p4.wav")
ep=pygame.mixer.Sound("/home/pi/main/p5.wav")
fp=pygame.mixer.Sound("/home/pi/main/p6.wav")
gp=pygame.mixer.Sound("/home/pi/main/p7.wav")
hp=pygame.mixer.Sound("/home/pi/main/p8.wav")
ab=pygame.mixer.Sound("/home/pi/main/b1.wav")
bb=pygame.mixer.Sound("/home/pi/main/b2.wav")
cb=pygame.mixer.Sound("/home/pi/main/b3.wav")
db=pygame.mixer.Sound("/home/pi/main/b4.wav")
eb=pygame.mixer.Sound("/home/pi/main/b5.wav")
fb=pygame.mixer.Sound("/home/pi/main/b6.wav")
gb=pygame.mixer.Sound("/home/pi/main/b7.wav")
hb=pygame.mixer.Sound("/home/pi/main/b8.wav")
af=pygame.mixer.Sound("/home/pi/main/f1.wav")
bf=pygame.mixer.Sound("/home/pi/main/f2.wav")
cf=pygame.mixer.Sound("/home/pi/main/f3.wav")
df=pygame.mixer.Sound("/home/pi/main/f4.wav")
ef=pygame.mixer.Sound("/home/pi/main/f5.wav")
ff=pygame.mixer.Sound("/home/pi/main/f6.wav")
gf=pygame.mixer.Sound("/home/pi/main/f7.wav")
hf=pygame.mixer.Sound("/home/pi/main/f8.wav")
ag=pygame.mixer.Sound("/home/pi/main/g1.wav")
bg=pygame.mixer.Sound("/home/pi/main/g2.wav")
cg=pygame.mixer.Sound("/home/pi/main/g3.wav")
dg=pygame.mixer.Sound("/home/pi/main/g4.wav")
eg=pygame.mixer.Sound("/home/pi/main/g5.wav")
fg=pygame.mixer.Sound("/home/pi/main/g6.wav")
gg=pygame.mixer.Sound("/home/pi/main/g7.wav")
hg=pygame.mixer.Sound("/home/pi/main/g8.wav")
tashvigh=pygame.mixer.Sound("/home/pi/main/tashvigh.wav")

channelA=pygame.mixer.Channel(0)
channelB=pygame.mixer.Channel(1)
channelC=pygame.mixer.Channel(2)
channelD=pygame.mixer.Channel(3)
channelE=pygame.mixer.Channel(4)
channelF=pygame.mixer.Channel(5)
channelG=pygame.mixer.Channel(6)
channelH=pygame.mixer.Channel(7)

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN)        #1senspin
GPIO.setup(3,GPIO.IN)        #2senspin
GPIO.setup(4,GPIO.IN)        #3senspin
GPIO.setup(17,GPIO.IN)       #4senspin
GPIO.setup(27,GPIO.IN)       #5senspin
GPIO.setup(22,GPIO.IN)       #6senspin
GPIO.setup(10,GPIO.IN)       #7senspin
GPIO.setup(9,GPIO.IN)        #8senspin
GPIO.setup(18,GPIO.OUT)      #1LED 
GPIO.setup(23,GPIO.OUT)      #2LED
GPIO.setup(24,GPIO.OUT)      #3LED
GPIO.setup(25,GPIO.OUT)      #4LED
GPIO.setup(8,GPIO.OUT)       #5LED
GPIO.setup(7,GPIO.OUT)       #6LED
GPIO.setup(12,GPIO.OUT)      #7LED
GPIO.setup(11,GPIO.OUT)      #8LED
GPIO.setup(5,GPIO.IN)        #LSBMELODY
GPIO.setup(6,GPIO.IN)        #MSBMELODY
GPIO.setup(13,GPIO.IN)       #GAMEOREDUCATION
global note=[]
global last=[]

def gamee():
    
    while True:
        if GPIO.input(2)==0:
            note+=['a']
        if GPIO.input(3)==0:
            note+=['b']
        if GPIO.input(4)==0:
            note+=['c']
        if GPIO.input(17)==0:
            note+=['d']
        if GPIO.input(27)==0:
            note+=['e']
        if GPIO.input(22)==0:
            note+=['f']
        if GPIO.input(10)==0:
            note+=['g']
        if GPIO.input(9)==0:
            note+=['h']
        if note!=last:
            if 'a' in note:
                GPIO.output(18,GPIO.HIGH)
            else
                GPIO.output(18,GPIO.LOW)
            if 'b' in note:
                GPIO.output(23,GPIO.HIGH)
            else
                GPIO.output(23,GPIO.LOW)
            if 'c' in note:
                GPIO.output(24,GPIO.HIGH)
            else
                GPIO.output(24,GPIO.LOW)
            if 'd' in note:
                GPIO.output(25,GPIO.HIGH)
            else
                GPIO.output(25,GPIO.LOW)
            if 'e' in note:
                GPIO.output(8,GPIO.HIGH)
            else
                GPIO.output(8,GPIO.LOW)
            if 'f' in note:
                GPIO.output(7,GPIO.HIGH)
            else
                GPIO.output(7,GPIO.LOW)
            if 'g' in note:
                GPIO.output(12,GPIO.HIGH)
            else
                GPIO.output(12,GPIO.LOW)
            if 'h' in note:
                GPIO.output(11,GPIO.HIGH)
            else
                GPIO.output(11,GPIO.LOW)
            if GPIO.input(5)==0 and GPIO.input(6)==0:
                pianogame()
            elif GPIO.input(5)==1 and GPIO.input(6)==0:
                belzgame()
            elif GPIO.input(5)==0 and GPIO.input(6)==1:
                flutgame()
            elif GPIO.input(5)==1 and GPIO.input(6)==1:
                guitargame()
            if GPIO.input(13)==1:
                educationn()


def pianogame():
    if 'a' in note and 'a' not in last:
        channelA.play(ap)
    if 'b' in note and 'b' not in last:
        channelB.play(bp)
    if 'c' in note and 'c' not in last:
        channelC.play(cp)
    if 'd' in note and 'd' not in last:
        channelD.play(dp)
    if 'e' in note and 'e' not in last:
        channelE.play(ep)
    if 'f' in note and 'f' not in last:
        channelF.play(fp)
    if 'g' in note and 'g' not in last:
        channelG.play(gp)
    if 'h' in note and 'h' not in last:
        channelH.play(hp)
    last=note
    note=[]

def belzgame():
    if 'a' in note and 'a' not in last:
        channelA.play(ab)
    if 'b' in note and 'b' not in last:
        channelB.play(bb)
    if 'c' in note and 'c' not in last:
        channelC.play(cb)
    if 'd' in note and 'd' not in last:
        channelD.play(db)
    if 'e' in note and 'e' not in last:
        channelE.play(eb)
    if 'f' in note and 'f' not in last:
        channelF.play(fb)
    if 'g' in note and 'g' not in last:
        channelG.play(gb)
    if 'h' in note and 'h' not in last:
        channelH.play(hb)
    last=note
    note=[]

def flutgame():
    if 'a' in note and 'a' not in last:
        channelA.play(af)
    if 'b' in note and 'b' not in last:
        channelB.play(bf)
    if 'c' in note and 'c' not in last:
        channelC.play(cf)
    if 'd' in note and 'd' not in last:
        channelD.play(df)
    if 'e' in note and 'e' not in last:
        channelE.play(ef)
    if 'f' in note and 'f' not in last:
        channelF.play(ff)
    if 'g' in note and 'g' not in last:
        channelG.play(gf)
    if 'h' in note and 'h' not in last:
        channelH.play(hf)
    last=note
    note=[]

def guitargame():
    if 'a' in note and 'a' not in last:
        channelA.play(ag)
    if 'b' in note and 'b' not in last:
        channelB.play(bg)
    if 'c' in note and 'c' not in last:
        channelC.play(cg)
    if 'd' in note and 'd' not in last:
        channelD.play(dg)
    if 'e' in note and 'e' not in last:
        channelE.play(eg)
    if 'f' in note and 'f' not in last:
        channelF.play(fg)
    if 'g' in note and 'g' not in last:
        channelG.play(gg)
    if 'h' in note and 'h' not in last:
        channelH.play(hg)
    last=note
    note=[]

def gamoredu():
    if GPIO.input(5)==0 and GPIO.input(6)==0:
        pianogame()
    elif GPIO.input(5)==1 and GPIO.input(6)==0:
        belzgame()
    elif GPIO.input(5)==0 and GPIO.input(6)==1:
        flutgame()
    elif GPIO.input(5)==1 and GPIO.input(6)==1:
        guitargame()
    if GPIO.input(13)==0:
        gamee()

def educationn():

    while True:
        Image.open('do.jpg').show()
        GPIO.output(18,GPIO.HIGH)
        while True:
            if GPIO.input(2)==0:
                note=['a']
                break
        gamoredu()
        GPIO.output(18,GPIO.LOW)

        Image.open('re.jpg').show()
        GPIO.output(23,GPIO.HIGH)
        while True:
            if GPIO.input(3)==0:
                note=['b']
                break
        gamoredu()
        GPIO.output(23,GPIO.LOW)

        Image.open('me.jpg').show()
        GPIO.output(24,GPIO.HIGH)
        while True:
            if GPIO.input(4)==0:
                note=['c']
                break
        gamoredu()
        GPIO.output(24,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('ce.jpg').show()
        GPIO.output(12,GPIO.HIGH)
        while True:
            if GPIO.input(10)==0:
                note=['g']
                break
        gamoredu()
        GPIO.output(12,GPIO.LOW)

        Image.open('do2.jpg').show()
        GPIO.output(11,GPIO.HIGH)
        while True:
            if GPIO.input(9)==0:
                note=['h']
                break
        gamoredu()
        GPIO.output(11,GPIO.LOW)

        sleep.time(2)
        channelA.play(tashvigh)
        sleep.time(10)

        #khosh halo shado khandanam
        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('me.jpg').show()
        GPIO.output(24,GPIO.HIGH)
        while True:
            if GPIO.input(4)==0:
                note=['c']
                break
        gamoredu()
        GPIO.output(24,GPIO.LOW)

        Image.open('re.jpg').show()
        GPIO.output(23,GPIO.HIGH)
        while True:
            if GPIO.input(3)==0:
                note=['b']
                break
        gamoredu()
        GPIO.output(23,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('me.jpg').show()
        GPIO.output(24,GPIO.HIGH)
        while True:
            if GPIO.input(4)==0:
                note=['c']
                break
        gamoredu()
        GPIO.output(24,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==1:
                break
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('me.jpg').show()
        GPIO.output(24,GPIO.HIGH)
        while True:
            if GPIO.input(4)==0:
                note=['c']
                break
        gamoredu()
        GPIO.output(24,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==1:
                break
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('me.jpg').show()
        GPIO.output(24,GPIO.HIGH)
        while True:
            if GPIO.input(4)==0:
                note=['c']
                break
        gamoredu()
        GPIO.output(24,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('me.jpg').show()
        GPIO.output(24,GPIO.HIGH)
        while True:
            if GPIO.input(4)==0:
                note=['c']
                break
        gamoredu()
        GPIO.output(24,GPIO.LOW)

        Image.open('re.jpg').show()
        GPIO.output(23,GPIO.HIGH)
        while True:
            if GPIO.input(3)==0:
                note=['b']
                break
        gamoredu()
        GPIO.output(23,GPIO.LOW)
        sleep.time(2)
        channelA.play(tashvigh)
        sleep.time(10)

        #tab tab abasi
        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('ce.jpg').show()
        GPIO.output(12,GPIO.HIGH)
        while True:
            if GPIO.input(10)==0:
                note=['g']
                break
        gamoredu()
        GPIO.output(12,GPIO.LOW)

        Image.open('ce.jpg').show()
        GPIO.output(12,GPIO.HIGH)
        while True:
            if GPIO.input(10)==1:
                break
        while True:
            if GPIO.input(10)==0:
                note=['g']
                break
        gamoredu()
        GPIO.output(12,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('ce.jpg').show()
        GPIO.output(12,GPIO.HIGH)
        while True:
            if GPIO.input(10)==0:
                note=['g']
                break
        gamoredu()
        GPIO.output(12,GPIO.LOW)

        Image.open('ce.jpg').show()
        GPIO.output(12,GPIO.HIGH)
        while True:
            if GPIO.input(10)==1:
                break
        while True:
            if GPIO.input(10)==0:
                note=['g']
                break
        gamoredu()
        GPIO.output(12,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('ce.jpg').show()
        GPIO.output(12,GPIO.HIGH)
        while True:
            if GPIO.input(10)==0:
                note=['g']
                break
        gamoredu()
        GPIO.output(12,GPIO.LOW)

        Image.open('ce.jpg').show()
        GPIO.output(12,GPIO.HIGH)
        while True:
            if GPIO.input(10)==1:
                break
        while True:
            if GPIO.input(10)==0:
                note=['g']
                break
        gamoredu()
        GPIO.output(12,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)

        Image.open('ce.jpg').show()
        GPIO.output(12,GPIO.HIGH)
        while True:
            if GPIO.input(10)==0:
                note=['g']
                break
        gamoredu()
        GPIO.output(12,GPIO.LOW)

        Image.open('ce.jpg').show()
        GPIO.output(12,GPIO.HIGH)
        while True:
            if GPIO.input(10)==1:
                break
        while True:
            if GPIO.input(10)==0:
                note=['g']
                break
        gamoredu()
        GPIO.output(12,GPIO.LOW)

        Image.open('la.jpg').show()
        GPIO.output(7,GPIO.HIGH)
        while True:
            if GPIO.input(22)==0:
                note=['f']
                break
        gamoredu()
        GPIO.output(7,GPIO.LOW)
        sleep.time(2)
        channelA.play(tashvigh)
        sleep.time(10)

        #barf
        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('re.jpg').show()
        GPIO.output(23,GPIO.HIGH)
        while True:
            if GPIO.input(3)==0:
                note=['b']
                break
        gamoredu()
        GPIO.output(23,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==1:
                break
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('re.jpg').show()
        GPIO.output(23,GPIO.HIGH)
        while True:
            if GPIO.input(3)==0:
                note=['b']
                break
        gamoredu()
        GPIO.output(23,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('me.jpg').show()
        GPIO.output(24,GPIO.HIGH)
        while True:
            if GPIO.input(4)==0:
                note=['c']
                break
        gamoredu()
        GPIO.output(24,GPIO.LOW)

        Image.open('re.jpg').show()
        GPIO.output(23,GPIO.HIGH)
        while True:
            if GPIO.input(3)==0:
                note=['b']
                break
        gamoredu()
        GPIO.output(23,GPIO.LOW)

        Image.open('do.jpg').show()
        GPIO.output(18,GPIO.HIGH)
        while True:
            if GPIO.input(2)==0:
                note=['a']
                break
        gamoredu()
        GPIO.output(18,GPIO.LOW)

        Image.open('re.jpg').show()
        GPIO.output(23,GPIO.HIGH)
        while True:
            if GPIO.input(3)==0:
                note=['b']
                break
        gamoredu()
        GPIO.output(23,GPIO.LOW)

        Image.open('me.jpg').show()
        GPIO.output(24,GPIO.HIGH)
        while True:
            if GPIO.input(4)==0:
                note=['c']
                break
        gamoredu()
        GPIO.output(24,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('re.jpg').show()
        GPIO.output(23,GPIO.HIGH)
        while True:
            if GPIO.input(3)==0:
                note=['b']
                break
        gamoredu()
        GPIO.output(23,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==1:
                break
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('re.jpg').show()
        GPIO.output(23,GPIO.HIGH)
        while True:
            if GPIO.input(3)==0:
                note=['b']
                break
        gamoredu()
        GPIO.output(23,GPIO.LOW)

        Image.open('sol.jpg').show()
        GPIO.output(8,GPIO.HIGH)
        while True:
            if GPIO.input(27)==0:
                note=['e']
                break
        gamoredu()
        GPIO.output(8,GPIO.LOW)

        Image.open('fa.jpg').show()
        GPIO.output(25,GPIO.HIGH)
        while True:
            if GPIO.input(17)==0:
                note=['d']
                break
        gamoredu()
        GPIO.output(25,GPIO.LOW)

        Image.open('me.jpg').show()
        GPIO.output(24,GPIO.HIGH)
        while True:
            if GPIO.input(4)==0:
                note=['c']
                break
        gamoredu()
        GPIO.output(24,GPIO.LOW)

        Image.open('re.jpg').show()
        GPIO.output(23,GPIO.HIGH)
        while True:
            if GPIO.input(3)==0:
                note=['b']
                break
        gamoredu()
        GPIO.output(23,GPIO.LOW)

        Image.open('do.jpg').show()
        GPIO.output(18,GPIO.HIGH)
        while True:
            if GPIO.input(2)==0:
                note=['a']
                break
        gamoredu()
        GPIO.output(18,GPIO.LOW)

        Image.open('do.jpg').show()
        GPIO.output(18,GPIO.HIGH)
        while True:
            if GPIO.input(2)==1:
                break
        while True:
            if GPIO.input(2)==0:
                note=['a']
                break
        gamoredu()
        GPIO.output(18,GPIO.LOW)

        Image.open('do.jpg').show()
        GPIO.output(18,GPIO.HIGH)
        while True:
            if GPIO.input(2)==1:
                break
        while True:
            if GPIO.input(2)==0:
                note=['a']
                break
        gamoredu()
        GPIO.output(18,GPIO.LOW)
        sleep.time(2)
        channelA.play(tashvigh)
        sleep.time(10)


while True:
    if GPIO.input(13)==0:
        gamee()
    if GPIO.input(13)==1:
        educationn()
