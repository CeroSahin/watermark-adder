from PIL import Image, ImageDraw, ImageFont


def watermark_adder(filename):
    im = Image.open(filename)
    width, heigth = im.size

    # defining the font size according to the height of the image
    if heigth > 2000:
        font_size = 70
    elif heigth > 1000:
        font_size = 60
    else:
        font_size = 30

    # make the im editable
    drawing = ImageDraw.Draw(im)
    font = ImageFont.truetype("AmaticSC-Bold.ttf", font_size)

    # getting the size of the watermark
    text = "© Ceren The Future Developer"
    text_w, text_h = drawing.textsize(text=text, font=font)

    # specifying the watermark coordinates
    x = 50
    y = heigth - text_h - 100

    # create a transparent background for the text
    c_text = Image.new(mode="RGB", size=(10 + text_w, 10 + text_h), color="#000000")
    draw = ImageDraw.Draw(c_text)
    draw.text((0, 0), text=text, fill="#ffffff", font=font)
    c_text.putalpha(100)

    # paste the watermark photo to im
    im.paste(c_text.rotate(45), (x, y), c_text.rotate(45))
    im.save(filename + ".thumbnail")
    im.show()
