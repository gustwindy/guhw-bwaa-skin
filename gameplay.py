from PIL import Image
import utils

def build():
    log = utils.logger("hitcircles")
    small_amount = 0.7
    
    circle = Image.open("assets/circles/hitcircle.png")
    approach = Image.open("assets/circles/approach.png")
    color_circle = Image.open("assets/circles/colorcircle.png")
    utils.save_2x(utils.set_opacity(Image.open("assets/circles/slidermove.png"),0.25),"build/sliderb.png")

    w,h = circle.size
    res_x,res_y = (w*small_amount)/0.8, (h*small_amount)/0.8
    plain_hit_circle = circle.resize((int(res_x),int(res_y)))
    color_circle = color_circle.resize((int(res_x),int(res_y)))
    utils.save_2x(approach.resize((int(res_x*0.8),int(res_y*0.8))),"build/approachcircle.png")
    
    red_circle = utils.set_color(color_circle, (255,10,10))
    blue_circle = utils.set_color(color_circle, (11,213,255))
    
    red_circle.paste(plain_hit_circle,mask=plain_hit_circle)
    blue_circle.paste(plain_hit_circle,mask=plain_hit_circle)
    
    for i in range(10):
        if i == 1:
            utils.save_2x(red_circle,f"build/default-{i}.png")
            continue
        utils.save_2x(blue_circle,f"build/default-{i}.png")
    
    follow = Image.open("assets/followpoint.png")
    empty = Image.open("assets/nothing.png")
    for i in range(60):
        empty.save(f"build/followpoint-{i}.png")
    for i in range(30):
        utils.save_2x(utils.set_opacity(follow,1-(abs(i-15)/15)),f"build/followpoint-{15+i}.png")