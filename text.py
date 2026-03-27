from PIL import Image,ImageDraw,ImageFont
import utils
import json

font = ImageFont.FreeTypeFont("assets/font.ttf",64)
def build():
    log = utils.logger("generating text")
    dummy = ImageDraw.Draw(Image.new("RGB",(1,1)))
    with open("assets/texts.json") as f:
        sizes = json.load(f)
    for font_size,texts in sizes.items():
        for filename,text in texts.items():
            x,y,w,h = dummy.textbbox((0,0),text,font=font,font_size=font_size)
            
            img = Image.new("RGBA",(w+6,h+6))
            draw = ImageDraw.Draw(img)
            draw.text((3,3),text,font=font,font_size=font_size,stroke_fill="black",stroke_width=2)
            
            utils.save_2x(img,f"build/{filename}.png")

build()