from tkinter import *
import time

print('rever <1>')

def drand():
	a = time.time()
	b = a * (time.time() - (a * 31))
	c = round((b / (a / 2) - a + b - (a * a)) * (b + a))
	d = abs(c + a * (c - b)) + (c % a) - 31 / a
	e = str(round(d))
	f = e[17] + e[16] + e[18]
	g = int(f)
	return g

def enter():
	l2['text'] = str(drand())

root=Tk()

root.title('dinikai\'s random generator')

l1=Label(text='dinikai\'s random generator', font='Courier 22').pack()
b=Button(text='Сгенерировать', font='Courier 14', command=enter).pack()
l2=Label(font='Courier 16')
l2.pack()

root.mainloop()
