from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)


card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_button = PhotoImage(file="./images/right.png")
wrong_button = PhotoImage(file="./images/wrong.png")





canvas = Canvas(width= 800, height=526)


canvas.create_image(400, 263, image=card_front)
canvas.grid(column=1, row=1,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 40, "italic"))



right_button = Button(image=right_button)
right_button.grid(column= 1, row=2)

wrong_button = Button(image=wrong_button)
wrong_button.grid(column= 2, row=2)





window.mainloop()

