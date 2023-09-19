from playsound import playsound
import time
from datetime import datetime
alaram = f"{input('Hours: ')}:{input('Min: ')}"

while True:
    current_time = datetime.now().time().strftime('%H:%M')
    if current_time == alaram:
        playsound('C:\\Users\\thila\\OneDrive\\Desktop\\python\\Alaram_setter\\alaram.mp3')
        break
    time.sleep(30)