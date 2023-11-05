import random
import tkinter as tk
from PIL import Image, ImageTk

#Dictionary for Pokemon and corresponding image and generations
mons = {"Staraptor":("Projects/staraptor.png", "Gen 4"),
"Regirock":("Projects/regirock.jpg", "Gen 3")}

#Function for getting random mon and values
def monGrabs():
    global monchoice, monim, mongen
    #Choosing a random mon from a list generated from the keys in our dictionary
    monchoice = random.choice(list(mons.keys()))
    #Choosing the monchoice value that corresponds with the randomly chosen key in the mons dictionary (in this case the value is a list), then chooses the respective value in the list
    monim=mons[monchoice][0]
    mongen=mons[monchoice][1]
    return monchoice,monim,mongen

def updateQuiz():
    monGrabs()
    imglabel.destroy()
    packImg(monim)
    entry.delete(0, 'end')

monGrabs()

#GUI
window=tk.Tk()
window.geometry("650x650")
window.configure(bg="black")
window.title("Gen Quiz")

#number correct
correct=0

def packImg(img1):
    global tkppic, imglabel
    #Image
    ppic = Image.open(img1)
    ppic=ppic.resize((400,400))
    tkppic = ImageTk.PhotoImage(ppic)
    imglabel = tk.Label(window, image=tkppic)
    imglabel.image = tkppic
    imglabel.pack()

packImg(monim)

#Entry Field
entry = tk.Entry(window)
entry.pack()

#Get the user input
def userInput():
    global correct
    inp = entry.get()
    if inp==mongen:
        print('Correct')
        correct += 1
        print(correct)
    else:
        print('Fail')
    updateQuiz()

getInput =tk.Button(window, text="Submit", command=userInput)
getInput.pack() 

window.mainloop()