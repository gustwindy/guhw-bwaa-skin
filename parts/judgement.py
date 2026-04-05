from PIL import Image
import utils
import math

def easeOutExpo(t):
    return -math.pow(2, -10 * t) + 1

def easeInExpo(t):
    return math.pow(2, 10 * (t - 1))

def build(variant):
    log = utils.logger("judgement")
    
    if variant.startswith("default"):
        effect = Image.open("assets/gameplay/hit/variants/normal/effect.png")
        judgement = {
            "50": ["#FFBD32", Image.open("assets/gameplay/hit/variants/normal/50.png")],
            "100": ["#93FF93", Image.open("assets/gameplay/hit/variants/normal/100.png")],
            "0": ["#FF4B8B", Image.open("assets/gameplay/hit/variants/normal/0.png")]
        }
        
        for key,v in judgement.items():
            color,img = v
            for f in range(60):
                anim = utils.set_color(effect,utils.hex_to_rgb(color))
                t_half_in = utils.unit(0, 40, f)
                t_judge_in = utils.unit(0, 30, f)
                t_judge_out = utils.unit(40, 60, f)
                t_half_out = utils.unit(40, 60, f)

                scale = 0.4+(easeOutExpo(t_judge_in)*0.6)
                w, h = img.size
                scaled_img = img.resize((int(w*scale), int(h*scale)))

                if t_half_in < 1:
                    anim = utils.set_opacity(anim, easeOutExpo(t_half_in))
                    p = utils.set_opacity(scaled_img, easeOutExpo(t_judge_in))
                    offset = ((anim.width - p.width)//2, (anim.height-p.height)//2)
                    anim.paste(p,offset,mask=p)
                else:
                    drop = int(easeInExpo(t_judge_out)*20)
                    anim = utils.set_opacity(anim,1-easeInExpo(t_half_out))
                    p = utils.set_opacity(scaled_img,1-easeInExpo(t_half_out)).rotate(easeInExpo(t_half_out)*-15)
                    offset = ((anim.width-p.width)//2, ((anim.height-p.height)//2) + drop)
                    anim.paste(p,offset,mask=p)
            
                utils.save_2x(anim,f"build/hit{key}-{f}.png")
                if key == "100":
                    utils.save_2x(anim,f"build/hit{key}k-{f}.png")
        
    elif variant == "performance":
        miss = utils.set_opacity(Image.open("assets/gameplay/hit/0.png"),0.5)
        h100 = utils.set_opacity(Image.open("assets/gameplay/hit/100.png"),0.25)
        h50 = utils.set_opacity(Image.open("assets/gameplay/hit/50.png"),0.25)
        
        utils.save_anim(miss,"build/hit0.png",20,True,True)
        utils.save_anim(h50,"build/hit50.png",10,True,True)
        utils.save_anim(h100,"build/hit100.png",10,True,True)
        utils.save_anim(h100,"build/hit100k.png",10,True,True)