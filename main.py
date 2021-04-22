from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

GREY = "#d8e3e7"
BLUE = "#51c4d3"
DARK_BLUE = "#126e82"
VERY_DARK_BLUE = "#132c33"
FONT_NAME = "Courier"


# ------------- FUNCTIONALITY ------------------ #
def watermark_adder(filename):
    im = Image.open(filename)
    width, heigth = im.size

    # defining the font size according to the height of the image
    if heigth > 2000 and width > 2000:
        font_size = 70
    elif heigth > 1000 and width > 1000:
        font_size = 60
    else:
        font_size = 10

    # make the im editable
    drawing = ImageDraw.Draw(im)
    font = ImageFont.truetype("playfair.ttf", font_size)

    # getting the size of the watermark
    entry_text = entry.get()
    if entry_text == "":
        text = "© joylead"
    else:
        text = f"© {entry_text}"

    text_w, text_h = drawing.textsize(text=text, font=font)

    # specifying the watermark coordinates
    x = width - text_w - 10
    y = heigth - text_h - 10

    # create a transparent background for the text
    c_text = Image.new(mode="RGB", size=(text_w, text_h), color="#000000")
    draw = ImageDraw.Draw(c_text)
    draw.text((0, 0), text=text, fill="#ffffff", font=font)
    c_text.putalpha(100)

    # paste the watermark photo to im
    im.paste(c_text, (x, y), c_text)
    im.save(filename)
    im.show()


def upload():
    filename = filedialog.askopenfilename(filetypes=(("png files", "*.png*"), ("jpeg files", "*.jpg*")))
    watermark_adder(filename)


# -------------- UI -------------- #
window = Tk()
window.title("Watermark Adder")
window.minsize(width=500, height=300)
window.config(bg=GREY, padx=20, pady=20)


title_label = Label(text="Welcome to the watermark adder!", font=(FONT_NAME, 20), bg=GREY, pady=20)
title_label.pack()

copyright_label = Label(text="Copyright Text", font=(FONT_NAME, 15), bg=GREY, pady=10)
copyright_label.pack()

entry = Entry(text="Watermark Text: ", font=(FONT_NAME, 10), bg=VERY_DARK_BLUE, fg=GREY)
entry.pack()
upload_button = Button(text="Upload Image", command=upload)
upload_button.pack()

window.mainloop()
