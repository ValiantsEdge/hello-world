import random
import tkinter as tk 
from PIL import Image, ImageTk


class pokemon():
    def __init__(self, name, gen):
        self.name = name
        self.gen = gen
    
    def __str__(self):
        return self.name + " is from Gen " + self.gen
# This dict can prob be removed
mons = {"Staraptor":"Gen 4"}
#modify these to pull from the below dictionary
mons1 = list(mons.items())
randommon = random.choice(mons1)
monim = random.choice(list(mons.keys()))
print(randommon)
#this dict should be the one with gen and image path
imagebase = {"Staraptor":"Projects/staraptor.png",
"Hoopa":"Gen 6"}
def get_image():
    selection=imagebase.get(monim)
    return selection

# GUI 
window =tk.Tk()
window.geometry("650x650")
window.configure(bg="black")
window.title("Gen Quiz")

#Image
starap = Image.open(get_image())
tkstarap = ImageTk.PhotoImage(starap)
imglabel = tk.Label(window, image=tkstarap)
imglabel.pack()

#Entry Field
entry = tk.Entry(window)
entry.pack()

# Get the user input
def userInput():
    inp = entry.get()
    return(inp)

getInput =tk.Button(window, text="Submit", command=userInput)
getInput.pack()

window.mainloop()

