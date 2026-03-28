from PIL import Image
import utils
import json

def build():
    log = utils.logger("copying no change files")
    with open("assets/move_over.json") as f:
        move = json.load(f)
    for orig,tos in move.items():
        img = Image.open(f"assets/{orig}.png")
        for to in tos:
            path = f"build/{to}.png"
            if orig == "nothing":
                img.save(path)
                continue
            utils.save_2x(img,path)