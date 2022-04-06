from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
import os
import random
import itertools
import pickle


def createCanvas():
    root = Tk()
    canvas = Canvas(root, width=1200, height=700, background= "white")
    canvas.pack()
    return root, canvas


def showImages(canvas, root, pair):
    global img1, img2, im1, im2
    img1Path = os.path.join("images", pair[0])
    img2Path = os.path.join("images", pair[1])
    im1 = ImageTk.PhotoImage(Image.open(img1Path))
    im2 = ImageTk.PhotoImage(Image.open(img2Path))

    img1 = Label(root, image=im1)
    img2 = Label(root, image=im2)

    canvas.create_image(50, 150, anchor=NW, image=im1)
    canvas.create_image(700, 150, anchor=NW, image=im2)
    canvas.pack()


def createRatingButtons(root):
    buttonFont = font.Font(size=50)
    textFont = font.Font(size=30)

    b1 = Button(root, text="1", bg="white", font=buttonFont, highlightbackground="white",
                fg="black", width=2, bd=0, padx=0, pady=0, command=lambda: getRating(1, [b1,b2,b3,b4,b5,b6, labelLeft, labelRight]))
    b1.place(x=50, y=300)

    labelLeft = Label(root, text='Least similar', font=textFont, bg="white", fg="black")
    labelLeft.place(x=20, y=400)

    b2 = Button(root, text="2", bg="white", font=buttonFont, highlightbackground="white",
                fg="black", width=2, bd=0, padx=0, pady=0, command=lambda: getRating(2, [b1,b2,b3,b4,b5,b6, labelLeft, labelRight]))
    b2.place(x=250, y=300)

    b3 = Button(root, text="3", bg="white", font=buttonFont, highlightbackground="white",
                fg="black", width=2, bd=0, padx=0, pady=0, command=lambda: getRating(3, [b1,b2,b3,b4,b5,b6, labelLeft, labelRight]))
    b3.place(x=450, y=300)

    b4 = Button(root, text="4", bg="white", font=buttonFont, highlightbackground="white",
                fg="black", width=2, bd=0, padx=0, pady=0, command=lambda: getRating(4, [b1,b2,b3,b4,b5,b6, labelLeft, labelRight]))
    b4.place(x=650, y=300)

    b5 = Button(root, text="5", bg="white", font=buttonFont, highlightbackground="white",
                fg="black", width=2, bd=0, padx=0, pady=0, command=lambda: getRating(5, [b1,b2,b3,b4,b5,b6, labelLeft, labelRight]))
    b5.place(x=850, y=300)

    b6 = Button(root, text="6", bg="white", font=buttonFont, highlightbackground="white",
                fg="black", width=2, bd=0, padx=0, pady=0, command=lambda: getRating(6, [b1,b2,b3,b4,b5,b6, labelLeft, labelRight]))
    b6.place(x=1050, y=300)

    labelRight = Label(root, text='Most similar', font=textFont, bg="white", fg="black")
    labelRight.place(x=1020, y=400)


def getRating(rating, buttons):
    ratings.append(rating)
    for button in buttons:
        button.place_forget()

    doTrial()


def doTrial():
    if len(pairs) == 0:
        root.destroy()
        return
    pair = pairs.pop(0)
    pairsShown.append(pair)
    showImages(canvas, root, pair)
    root.update()
    root.after(8000, canvas.delete('all'))

    createRatingButtons(root)


if __name__ == '__main__':
    info = input("Enter dyad number, pre/post (0/1), subject number(0/1): [separated by space]\n")
    dyad, session, subject = info.split(" ")

    with open('stimuli.pkl', 'rb') as f:
        allCombos = pickle.load(f)

    stimuli, story, nonStory = allCombos[int(dyad)]

    pairs = list(itertools.combinations(stimuli, 2))
    random.shuffle(pairs)

    ratings = []
    pairsShown = []
    root, canvas = createCanvas()

    doTrial()
    root.mainloop()

    print(ratings)
    print(pairsShown)

    #print(pairsShown)
    #print(stimuli)
    #print(ratings)
    #print(story)
    #print(nonStory)

