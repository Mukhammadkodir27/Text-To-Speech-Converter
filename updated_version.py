from gtts import gTTS
from tkinter import *
from tkinter import messagebox
import os
from PIL import Image, ImageTk

root = Tk()
root.title("Text to Speech Generator")

# Load the background image
image = Image.open("background3.png")
bg_image = ImageTk.PhotoImage(image)

# Adjust the window size to match the image size
root.geometry(f"{bg_image.width()}x{bg_image.height()}")

# Prevent the window from being maximized
root.resizable(False, False)

# Setting up the background label
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


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
entry.place(relx=0.5, rely=0.5, anchor=CENTER)

button = Button(root, text="Start", command=textToSpeech)
button.place(relx=0.5, rely=0.6, anchor=CENTER)

status_label = Label(root, text="", fg="green")
status_label.place(relx=0.5, rely=0.4, anchor=CENTER)

root.mainloop()
