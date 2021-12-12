'''
Created on 22 nov 2021

@author: Jorge Muñoz
'''
import time

print('¡Pomodoro empieza ahora!')
for i in range(4):
    t = 25*60
    while t:
        mins = t//60
        secs = t%60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(''+timer, end='\r')
        time.sleep(1)
        t -= 1
print('¡Tiempo de descanso!')
t = 5*60
while t:
    mins = t//60
    secs = t%60
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(''+timer, end='\r')
    time.sleep(1)
    t -= 1
print('¡Hora de trabajar!')

#Modificado en Visual Studio Code por segunda vez