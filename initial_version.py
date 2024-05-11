from gtts import gTTS
from tkinter import *
from tkinter import messagebox
import os
from PIL import Image, ImageTk

root = Tk()
root.title("Text to Speech Generator")

# Prevent the window from being maximized
root.resizable(False, False)

# Load the background image
image = Image.open("background2.png")
bg_image = ImageTk.PhotoImage(image)
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Ensure the label stays at the back
bg_label.lower()

canvas = Canvas(root, width=400, height=300)
canvas.pack()

# Function to generate a unique filename for each output


def get_unique_filename():
    count = 0
    while True:
        filename = f"Recording{count}.mp3"
        if not os.path.exists(filename):
            return filename
        count += 1


def textToSpeech():
    text = entry.get()
    if text.strip():  # Ensure there is text to convert
        language = "en"
        filename = get_unique_filename()
        output = gTTS(text=text, lang=language, slow=False)
        output.save(filename)
        os.system(f"start wmplayer {filename}")
        status_label.config(text="Success! The voice is ready!", fg="green")
    else:
        status_label.config(text="Error: Please enter some text.", fg="red")


entry = Entry(root)
canvas.create_window(200, 140, window=entry)

button = Button(text="Start", command=textToSpeech)
canvas.create_window(200, 180, window=button)

status_label = Label(root, text="", fg="green")
canvas.create_window(200, 100, window=status_label)

root.mainloop()
