import random
import tkinter as tk 
from PIL import Image, ImageTk


class pokemon():
    def __init__(self, name, gen):
        self.name = name
        self.gen = gen
    
    def __str__(self):
        return self.name + " is from Gen " + self.gen

mons = {"Staraptor":"Gen 4",
"Hoopa":"Gen 6"}
mons1 = list(mons.items())
randommon = random.choice(mons1)
print(randommon)

# GUI 
window =tk.Tk()
window.geometry("650x650")
window.configure(bg="black")
window.title("Gen Quiz")

starap = Image.open("Projects/staraptor.png")
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

