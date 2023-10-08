import random
import tkinter as tk 
from PIL import Image, ImageTk

class pokemon():
    def __init__(self, name, gen):
        self.name = name
        self.gen = gen
    
    def __str__(self):
        return self.name + " is from Gen " + self.gen
#Dictionary for Pokemon and corresponding image and generations
mons = {"Staraptor":("Projects/staraptor.png", "Gen 4"),
"Regirock":("Projects/regirock.jpg", "Gen 3")}

#Choosing a random mon from a list generated from the keys in our dictionary
monchoice = random.choice(list(mons.keys()))
#Choosing the monchoice value that corresponds with the randomly chosen key in the mons dictionary (in this case the value is a list), then chooses the respective value in the list
monim=mons[monchoice][0]
mongen=mons[monchoice][1]


# GUI 
window =tk.Tk()
window.geometry("650x650")
window.configure(bg="black")
window.title("Gen Quiz")

#Image
starap = Image.open(monim)
tkstarap = ImageTk.PhotoImage(starap)
imglabel = tk.Label(window, image=tkstarap)
imglabel.pack()

#Entry Field
entry = tk.Entry(window)
entry.pack()

# Get the user input
def userInput():
    inp = entry.get()
    if inp==mongen:
        print('Correct')
    else:
        print('fail')
    return(inp)

getInput =tk.Button(window, text="Submit", command=userInput)
getInput.pack()

window.mainloop()