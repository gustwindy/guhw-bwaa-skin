from PIL import Image, ImageDraw, ImageFont
import utils
import os

mods = {
    "targetpractice": "tp",
    "suddendeath": "sd",
    "spunout": "so",
    "scorev2": "v2",
    "relax2": "ap",
    "relax": "rx",
    "random": "rd",
    "perfect": "pf",
    "nofail": "nf",
    "nightcore": "nc",
    "hidden": "hd",
    "hardrock": "hr",
    "halftime": "ht",
    "flashlight": "fl",
    "fadein": "fi",
    "easy": "ez",
    "doubletime": "dt",
    "cinema": "cn",
    "autoplay": "au"
}
font = ImageFont.FreeTypeFont("assets/font.ttf",64)

def build():
    log = utils.logger("creating mod icons")
    for real,name in mods.items():
        icon = f"assets/mods/{name}.png"
        exists = os.path.exists(icon)
        if not exists:
            log(f"there isn {icon}")
            continue
        
        img = Image.open(icon).resize((200,200))
        draw = ImageDraw.Draw(img)
        color = img.resize((1,1)).convert("RGB").getpixel((0,0))
        
        draw.text((0,0),name.upper(),font=font,fill=color,stroke_fill="white",stroke_width=2)
        
        utils.save_2x(img,f"build/selection-mod-{real}.png")