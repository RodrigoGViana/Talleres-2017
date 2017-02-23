# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 18:40:58 2017

@author: Rodrigo
"""
#%% Ejemplo if, elif, else
number = 23
guess = int(input('Enter an integer : '))

if guess == number:
	print('Congratulations, you guessed it.')
	print('(but you do not win any prizes!)')
elif guess < number:
	print('No, it is a little higher than that')
else:
	print('No, it is a little lower than that')

print('Done')

#%% Ejemplo while
number = 23
running = True # boolean

while running:
	guess = int(input('Enter an integer : '))
	if guess == number:
		print('Congratulations, you guessed it.')
		running = False
	elif guess < number:
		print('No, it is higher than that.')
	else:
		print('No, it is lower than that.')
print('Done')

#%% Ejemplo for
for i in range(1, 5):
	print(i)
else:
	print('The for loop is over')

#%% Ejemplo matplotlib
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(1,10,500)
y = np.sin(2*t)

plt.plot(t, y)
plt.show()

#%% Ejemplo matplotlib 2

import numpy as np
import matplotlib.pyplot as plt

Escalon = np.loadtxt('Sis_subamortiguado.txt', delimiter=',')

plt.plot(Escalon[0], Escalon[1], linewidth=2.0)
plt.xlabel('Tiempo')
plt.ylabel('Respuesta')
plt.title('Sistema subamortiguado')
plt.axis([0, 20, 0, 0.35])

plt.plot((0,20),(0.20,0.20), '--k', label='Estado estacionario')
plt.legend(loc='best')

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 12,
        }

plt.text(2, 0.05, 'Es posible incorporar texto.', fontdict=font)
plt.show()