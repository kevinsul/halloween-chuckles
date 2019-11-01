import time
import os
import random

def randomsounds():

    randnum1 = random.randrange(1,19)
    
    if randnum1 == 1:
        os.system("mpg321 -g 500 ./sounds/Bike_Horn.mp3 &")
        print ("Playing Bike Horn")
        
    elif randnum1 == 2:
        os.system("mpg321 -g 500 ./sounds/Creepy_Laugh.mp3 &")
        print ("Playing Creepy Laugh")

    if randnum1 == 3:
        os.system("mpg321 -g 500 ./sounds/Dark_Laugh-HopeinAwe.mp3 &")
        print ("Playing Dark_Laugh-HopeinAwe")
        
    elif randnum1 == 4:
        os.system("mpg321 -g 500 ./sounds/Demon_Girls_Mockingbir-Hello.mp3 &")
        print ("Playing Demon_Girls_Mockingbir-Hello")
        
    if randnum1 == 5:
        os.system("mpg321 -g 500 ./sounds/Evil_Monster.mp3 &")
        print ("Playing Evil_Monster")
        
    elif randnum1 == 6:
        os.system("mpg321 -g 500 ./sounds/I_Want_Brains.mp3 &")
        print ("Playing I_Want_Brains")
        
    if randnum1 == 7:
        os.system("mpg321 -g 500 ./sounds/I_will_kill_you.mp3 &")
        print ("Playing I_will_kill_you")
        
    elif randnum1 == 8:
        os.system("mpg321 -g 500 ./sounds/knocking1.mp3 &")
        print ("Playing knocking1")
        
    if randnum1 == 9:
        os.system("mpg321 -g 500 ./sounds/Laugh Evil-SoundBible.mp3 &")
        print ("Playing Laugh Evil-SoundBible")
        
    elif randnum1 == 10:
        os.system("mpg321 -g 500 ./sounds/Little_Demon_Girl_Song.mp3 &")
        print ("Playing Little_Demon_Girl_Song")
        
    if randnum1 == 11:
        os.system("mpg321 -g 500 ./sounds/Maniacal_Witches_Laugh.mp3 &")
        print ("Playing Maniacal_Witches_Laugh")
        
    elif randnum1 == 12:
        os.system("mpg321 -g 500 ./sounds/Mummy_Zombie.mp3 &")
        print ("Playing Mummy_Zombie")

    if randnum1 == 13:
        os.system("mpg321 -g 500 ./sounds/No_mercy.mp3 &")
        print ("Playing No_mercy")
        
    elif randnum1 == 14:
        os.system("mpg321 -g 500 ./sounds/Scary_Scream.mp3 &")
        print ("Playing Scary_Scream")
     
    if randnum1 == 15:
        os.system("mpg321 -g 500 ./sounds/Spooky.mp3 &")
        print ("Playing Spooky")
        
    elif randnum1 == 16:
        os.system("mpg321 -g 500 ./sounds/Strange_Growl.mp3 &")
        print ("Playing Strange_Growl")

    if randnum1 == 17:
        os.system("mpg321 -g 500 ./sounds/witchlaugh.mp3 &")
        print ("Playing witchlaugh")
        
    elif randnum1 == 18:
        os.system("mpg321 -g 500 ./sounds/Yoda-Kevan.mp3 &")
        print ("Playing Yoda-Kevan")
   


print("STARTED")
randomsounds()