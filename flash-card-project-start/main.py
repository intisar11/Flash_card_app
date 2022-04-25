from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

card ={}

data = pd.read_csv("../flash-card-project-start/data/french_words.csv")

df = pd.DataFrame(data)

dict_data = df.to_dict(orient="records")


def next_card():
    global card, timer
    window.after_cancel(timer)
    card = random.choice(dict_data)
    canvas.itemconfig(card_title, text= "French", fill="black")
    canvas.itemconfig(card_word, text=card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    timer = window.after(3000, func=flip_card)


def is_known():
    dict_data.remove(card)
    next_card()








def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")
    canvas.itemconfig(canvas_image, image= card_back)



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)


card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_button = PhotoImage(file="images/right.png")
wrong_button = PhotoImage(file="./images/wrong.png")





canvas = Canvas(width= 800, height=526)


canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=1, row=1,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "italic"))



button_1 = Button(image=right_button, highlightthickness=0, command=next_card)
button_1.grid(column=2, row=2)

button_2 = Button(image=wrong_button, command=next_card, highlightthickness= 0)
button_2.grid(column=1, row=2)

next_card()









window.mainloop()

