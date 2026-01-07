import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time()*100))
    name = '{}.png'.format(name)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,text='Click Screenshot',command=screenshot)
button.pack(side=tk.LEFT)
close = tk.Button(frame,text="Exit",command=quit)
close.pack(side=tk.LEFT)

root.mainloop()