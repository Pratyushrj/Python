from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a= input()
        if a== stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    # musiconloop("water.mp3","stop")
    init_water =time()
    init_eye =time()
    init_exe =time()
    watersec=5
    eyesec=20
    execsec=10
    while True:
        if time()- init_water>watersec:
            print("Water drinking time , Enter 'DRANK' to stop alarm")
            musiconloop("water.mp3","DRANK")
            init_water=time()
            log_now("Drank water at")
        if time()- init_eye>eyesec:
            print("Eye exercise time , Enter 'EDONE' to stop alarm")
            musiconloop("beep.mp3","EDONE")
            init_eye=time()
            log_now("Eye relaxed at")
        if time()- init_exe>execsec:
            print("Physical Exercise time , Enter 'DONE' to stop alarm")
            musiconloop("bee.mp3","DONE")
            init_exe=time()
            log_now("Physical exercise done at")