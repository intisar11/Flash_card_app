from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("../flash-card-project-start/data/french_words.csv")

df = pd.DataFrame(data)

dict_data = df.to_dict(orient="records")


def next_card():
    card = random.choice(dict_data)
    canvas.itemconfig(card_title, text= "French")
    canvas.itemconfig(card_word, text=card["French"])




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)


card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_button = PhotoImage(file="images/right.png")
wrong_button = PhotoImage(file="./images/wrong.png")





canvas = Canvas(width= 800, height=526)


canvas.create_image(400, 263, image=card_front)
canvas.grid(column=1, row=1,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "italic"))



button_1 = Button(image=right_button, highlightthickness=0, command=next_card)
button_1.grid(column=2, row=2)

button_2 = Button(image=wrong_button, highlightthickness= 0)
button_2.grid(column=1, row=2)

next_card()







window.mainloop()

