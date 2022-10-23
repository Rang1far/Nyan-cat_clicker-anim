from tkinter import *
from PIL import Image, ImageTk
from winsound import *

# Function to change sprites and score

def change_sprite():
    global sprite_now
    global score

    score = score + 1
    show_score.set(str(score))

    if sprite_now <= 6:
        sprite_now = sprite_now + 1
    else:
        sprite_now = 1

    if sprite_now == 1:
        show_sprite.configure(image=sprite1)
    elif sprite_now == 2:
        show_sprite.configure(image=sprite2)
    elif sprite_now == 3:
        show_sprite.configure(image=sprite3)
    elif sprite_now == 4:
        show_sprite.configure(image=sprite4)
    elif sprite_now == 5:
        show_sprite.configure(image=sprite5)
    elif sprite_now == 6:
        show_sprite.configure(image=sprite6)

# GUI set

window = Tk()
window.title("Nyan cat animation")

# Give sprites to Tkinter

sprite1 = ImageTk.PhotoImage(Image.open("1.png").resize((360, 360), Image.ANTIALIAS))
sprite2 = ImageTk.PhotoImage(Image.open("2.png").resize((360, 360), Image.ANTIALIAS))
sprite3 = ImageTk.PhotoImage(Image.open("3.png").resize((360, 360), Image.ANTIALIAS))
sprite4 = ImageTk.PhotoImage(Image.open("4.png").resize((360, 360), Image.ANTIALIAS))
sprite5 = ImageTk.PhotoImage(Image.open("5.png").resize((360, 360), Image.ANTIALIAS))
sprite6 = ImageTk.PhotoImage(Image.open("6.png").resize((360, 360), Image.ANTIALIAS))

# Seting all vars

sprite_now = 1
score = 0
show_score = StringVar()

# Setting all to window

Label(window, textvariable=show_score, height=10, width=15).pack()

show_sprite = Label(window, image=sprite1)
show_sprite.pack()

Button(window, text="Nyan!", command=change_sprite, width=25, height=5).pack()

# Playing music & set to 0 score (showing it)

PlaySound("Music.wav", SND_ASYNC)
show_score.set("0")

mainloop()
