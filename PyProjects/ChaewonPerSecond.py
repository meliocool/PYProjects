# Yo! this is a program with a working GUI
# To count how many times you clicked on S21 Kim Chaewon from tripleS!
# Silly Click Per Seconds program basically

from tkinter import *
import time
from PIL import Image, ImageTk

chaewon_count = 0
start = None
def click():
    global chaewon_count, start
    chaewon_count += 1
    try:
        if chaewon_count == 1:
            start = time.time()
        
        timePassed = time.time() - start
        if timePassed > 0:
            cpm = chaewon_count / timePassed
            cpmDisplay.config(text=f'Chaewon Per Second: {cpm: .2f}')
            numOfChaewons.config(text=f'Chaewon is clicked {chaewon_count} times')
        else:
            cpmDisplay.config(text=f'Chaewon is thinking...')
    except:
        cpmDisplay.config(text='Chaewon is tired :(')

window = Tk()
window.title("Chaewon Per Second") 

icon = Image.open('C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\PyProjects\\images\\Screenshot (1202).png') 
icon_resized = icon.resize((50,60))
iconPI = ImageTk.PhotoImage(icon_resized)
window.iconphoto(True,iconPI) 

img = Image.open('C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\PyProjects\\images\\Screenshot (1202).png')
resized = img.resize((600,500))
chaewon = ImageTk.PhotoImage(resized)

cpmDisplay = Label(window, text='Click Chaewon!', font=('Arial', 30, 'bold'), fg='black')
numOfChaewons = Label(window, text='CPS', font=('Arial', 30, 'bold'), fg='black') 

button = Button(window, 
                command=click,
                bg='black',
                image=chaewon,
                relief=RAISED,
                bd=10,
                padx=20,
                pady=20)

cpmDisplay.pack()
numOfChaewons.pack()
button.pack()

window.mainloop()