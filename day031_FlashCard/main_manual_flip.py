# ------------------------------------------------------
# Flash Cards
# ------------------------------------------------------
'''
- flash card for learning (languages, capital cities, flags, etc.)
- front side of the card reveals a Deutsch word from the 5000 most frequent words
- for flipping the card, click 'Flip card'
- back side of the card reveals the English meaning of the Deutsch word
- if the user know the word, choose 'right', otherwise choose 'wrong'
- the 'wrong' words are saved in a file for next learning
'''
# ------------------------------------------------------

# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
from tkinter import *
import pandas as pd
import random
# ------------------------------------------------------

# ------------------------------------------------------
# Define constants
# ------------------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
FONT_FLIP = ("Arial", 20, "bold")
# ------------------------------------------------------

# ------------------------------------------------------
# Read data
# ------------------------------------------------------
current_card = {}
data_to_learn = {}

try:
    data_de = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/deutsch_words_5000.csv")
    data_to_learn = original_data.to_dict(orient="records")
else:
    data_to_learn = data_de.to_dict(orient="records")
# ------------------------------------------------------


# ------------------------------------------------------
# Define functions
# ------------------------------------------------------
def next_card():
    global current_card
    current_card = random.choice(data_to_learn)
    canvas.itemconfig(language_text, text="Deutsch", fill="black")
    canvas.itemconfig(word_text, text=current_card["Deutsch"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    button_flip.config(state=NORMAL)


def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    button_flip.config(state=DISABLED)


def is_known():
    data_to_learn.remove(current_card)
    # print(len(data_to_learn))
    data = pd.DataFrame(data_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    button_flip.config(state=NORMAL)
    next_card()
# ------------------------------------------------------


# ------------------------------------------------------
# GUI
# ------------------------------------------------------
# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="Title", fill="black", font=FONT_LANGUAGE)
word_text = canvas.create_text(400, 263, text="word", fill="black", font=FONT_WORD)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

# Button
icon_unknown = PhotoImage(file="images/wrong.png")
button_unknown = Button(image=icon_unknown, command=next_card)
button_unknown.grid(row=1, column=0)

button_flip = Button(text="Flip card", width=10, font=FONT_FLIP, command=flip_card)
button_flip.grid(row=1, column=1)

icon_known = PhotoImage(file="images/right.png")
button_known = Button(image=icon_known, command=is_known)
button_known.grid(row=1, column=2)


next_card()

# Mainloop
window.mainloop()
# ------------------------------------------------------
