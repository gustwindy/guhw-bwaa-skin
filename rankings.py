from PIL import Image,ImageDraw,ImageFont
import utils
import json

rankings = {
    "XH": "#ecfbff",
    "X": "#e6fcff",
    "SH": "#fdffa0",
    "S": "#fffb00",
    "A": "#92ffd2",
    "B": "#7dcbff",
    "C": "#e195ff",
    "D": "#ff6464",
    "F": "#962020"
}

def build():
    log = utils.logger("rankings")
    for name,color in rankings.items():
        big = utils.create_text(name,84,color)
        small = utils.create_text(name,40,color)
        
        utils.save_2x(big,f"build/ranking-{name}.png")
        utils.save_2x(small,f"build/ranking-{name}-small.png")

build()