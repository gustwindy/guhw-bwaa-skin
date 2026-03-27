from PIL import Image,ImageDraw,ImageFont
import utils
import json

rankings = {
    "XH": "#ecfbff",
    "X": "#e6fcff",
    "SH": "#feffdc",
    "S": "#fffb00",
    "A": "#92ffd2",
    "B": "#7dcbff",
    "C": "#e195ff",
    "D": "#ff6464",
    "F": "#962020"
}

def build():
    log = utils.logger("rankings")
    ranking_bg = Image.open("assets/rankingbg.png")
    for name,color in rankings.items():
        big = utils.create_text(name[0],256,color)
        small = utils.create_text(name[0],64,color)
        
        big = utils.scale_to_fit(big,720)
        
        bg = utils.set_color(ranking_bg,utils.hex_to_rgb(color.lstrip("#")))
        w,h = bg.size
        sw,sh = small.size
        bg.paste(small,((w//3)-(sw//2),(h//2)-(sh//2)),mask=small)
        utils.save_2x(big,f"build/ranking-{name}.png")
        utils.save_2x(bg,f"build/ranking-{name}-small.png")