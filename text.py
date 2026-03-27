from PIL import Image,ImageDraw,ImageFont
import utils
import json

def build():
    log = utils.logger("generating text")
    with open("assets/texts.json") as f:
        sizes = json.load(f)
    for font_size,texts in sizes.items():
        for filename,text in texts.items():
            utils.save_2x(utils.create_text(text,int(font_size)),f"build/{filename}.png")