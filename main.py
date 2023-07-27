from tkinter import *
import pandas
import random



BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- Save Your Progress ------------------------------- #
def next_card_right():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(data_list)
    canvas.itemconfig(title_text, text="French",fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(image_screen, image=image_lock)
    flip_timer = screen.after(3000, flip_card)
    data_list.remove(current_card)
    data = pandas.DataFrame(data_list)
    data.to_csv("data/words_to_learn.csv",index=False)






# ---------------------------- Flip the Cards! ------------------------------- #

current_card = {}

def flip_card():
    canvas.itemconfig(image_screen,image=image_flip)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

# ---------------------------- Create New Flash Cards ------------------------------- #

try:
    data_words_2 = pandas.read_csv("data/words_to_learn.csv")
    data_list = pandas.DataFrame.to_dict(data_words_2, orient="records")
except FileNotFoundError:
    data_words = pandas.read_csv("data/french_words.csv")
    data_list = pandas.DataFrame.to_dict(data_words, orient="records")


def next_card():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(data_list)
    canvas.itemconfig(title_text, text="French",fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(image_screen, image=image_lock)
    flip_timer = screen.after(3000, flip_card)

# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Flashy")
screen.config(pady=50, padx= 50, background=BACKGROUND_COLOR)
flip_timer = screen.after(3000, flip_card)


canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
image_lock =PhotoImage(file="images/card_front.png")
image_flip = PhotoImage(file="images/card_back.png")
image_screen = canvas.create_image(400, 263, image=image_lock)
title_text = canvas.create_text(400, 150, text="Title" , font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card_right)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, background=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)





next_card()
screen.mainloop()

















