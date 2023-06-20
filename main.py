import random
import string
from tkinter import *  
from tkinter import ttk
#tkinter init
window = Tk()
window.geometry("250x250")
window.title("Generator")

#tkinter functions
def on_slider_move(value):
    global sliderNum
    sliderLabel.config(text=f"Length Of Password: {value}")
    sliderNum = slider.get()

def numberChecker():
    global yesNumbers
    if checkbox_num.get():
        yesNumbers = True
    else:
        yesNumbers = False
    print(yesNumbers)   

def letterChecker():
    global yesLetters
    if checkbox_letter.get():
        yesLetters = True
    else:
        yesLetters = False
    print(yesLetters)

def symbolChecker():
    global yesSymbols
    if checkbox_symbol.get():
        yesSymbols = True
    else:
        yesSymbols = False
    print(yesSymbols)

def createButton():
    count = 0
    finalOutput = []
    length = sliderNum
    print(length)
    for i in range(length):
        randomChoice = random.randint(0,2)
        if randomChoice == 0:
            randomNumber = random.randint(0,10)
            finalOutput.append(randomNumber)
        elif randomChoice == 1:
            randomLetter = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            finalOutput.append(randomLetter)
        else: 
            randomSymbol = random.choice("!""#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~")
            finalOutput.append(randomSymbol)
    print(finalOutput)
    count += 1

    global finalOutputLabel
    finalOutputLabel = Label(window, text= finalOutput)
    finalOutputLabel.pack()

def clear_label():
    finalOutputLabel.config(text="")
    finalOutputLabel.pack()
        
###rest of tkinter###
label = Label(window, text="Secure Random Password Generator")
label.pack()

#password length
passwordLength = IntVar()
slider = Scale(window, variable = passwordLength, from_=0, to=50, orient='horizontal', command=on_slider_move)
slider.pack()
sliderLabel = Label()
sliderLabel.pack()

#numbers envolved
checkbox_num = IntVar()
numbersEnvolved = Checkbutton(text="Numbers", variable=checkbox_num ,command = numberChecker)
numbersEnvolved.pack()

#letters envolved
checkbox_letter= IntVar()
lettersEnvolved = Checkbutton(text="Letters?", variable = checkbox_letter, command = letterChecker)
lettersEnvolved.pack()

#special characters envolved
checkbox_symbol = IntVar()
symbolEnvolved = Checkbutton(text = "Symbols?", variable = checkbox_symbol, command = symbolChecker)
symbolEnvolved.pack()

#create password button
createPassword = Button(window, text = "Create Password", command = createButton)
createPassword.pack()

#clear text
clearText = Button(window, text="Clear", command=clear_label)
clearText.pack()

#output
window.pack_propagate(False)
window.mainloop()