from PIL import Image
import utils

def build(variant):
    log = utils.logger("hitcircles")
    small_amount = 0.7
    follow = Image.open("assets/gameplay/followpoint.png")
    
    if variant == "default":
        follow = Image.open("assets/gameplay/followpoint-grey.png")
        circle = Image.open("assets/gameplay/circles/variants/normal/hitcircle.png")
        approach = Image.open("assets/gameplay/circles/variants/normal/approach.png")
        color_circle = Image.open("assets/gameplay/circles/variants/normal/colorcircle.png")
        
        utils.save_2x(approach,"build/approachcircle.png")
        utils.save_2x(circle,"build/hitcircleoverlay.png")
        utils.save_2x(color_circle,"build/hitcircle.png")
        
        
        cursor = Image.open("assets/gameplay/circles/variants/normal/cursor.png")
        cursor_middle = Image.open("assets/gameplay/circles/variants/normal/cursoroverlay.png")
        #trail = Image.open("assets/gameplay/circles/variants/normal/cursortrail.png")
        w,h = cursor.size
        res = (w//3,h//3)
        
        utils.save_2x(cursor.resize(res),"build/cursor.png")
        utils.save_2x(cursor_middle.resize(res),"build/cursormiddle.png")
        #utils.save_2x(trail,"build/cursortrail.png")
        
        for i in range(10):
            number = utils.create_text(str(i),128,font="assets/otherfont.ttf")
            w,h = number.size
            center = Image.new("RGBA",(w,h))
            
            center.paste(number,(0,-20))
            utils.save_2x(center,f"build/default-{i}.png")
    
    elif variant == "performance":
        circle = Image.open("assets/gameplay/circles/hitcircle.png")
        approach = Image.open("assets/gameplay/circles/approach.png")
        color_circle = Image.open("assets/gameplay/circles/colorcircle.png")

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
    
    utils.save_2x(utils.set_opacity(Image.open("assets/gameplay/circles/slidermove.png"),0.25),"build/sliderb.png")
    empty = Image.open("assets/nothing.png")
    for i in range(60):
        empty.save(f"build/followpoint-{i}.png")
    for i in range(30):
        utils.save_2x(utils.set_opacity(follow,1-(abs(i-15)/15)),f"build/followpoint-{15+i}.png")