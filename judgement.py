from PIL import Image
import utils

def build():
    log = utils.logger("judgement")
    miss = utils.set_opacity(Image.open("assets/gameplay/hit/0.png"),0.5)
    h100 = utils.set_opacity(Image.open("assets/gameplay/hit/100.png"),0.25)
    h50 = utils.set_opacity(Image.open("assets/gameplay/hit/50.png"),0.25)
    
    utils.save_anim(miss,"build/hit0.png",20,True,True)
    utils.save_anim(h50,"build/hit50.png",10,True,True)
    utils.save_anim(h100,"build/hit100.png",10,True,True)
    utils.save_anim(h100,"build/hit100k.png",10,True,True)