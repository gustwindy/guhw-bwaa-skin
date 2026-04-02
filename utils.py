from PIL import Image,ImageDraw,ImageFont

def save_2x(img: Image.Image,path: str,big_path = None):
    img.save(big_path or path.replace(".","@2x."))
    w,h = img.size
    img.resize((w//2,h//2)).save(path)
    print("\t\t\t+",path)

def save_anim(img: Image.Image,path: str,frames: int,include_none = False,last_empty = False):
    for i in range(frames):
        save_2x(img,path.replace(".",f"-{i}."))#,path.replace(".",f"@2x-{i}.")) #what is going on
    if include_none:
        save_2x(img,path)
    if last_empty:
        save_2x(Image.new("RGBA",img.size),path.replace(".",f"-{frames}."))

def set_opacity(img: Image.Image,opacity: float):
    img = img.convert("RGBA")
    r, g, b, a = img.split()
    a = a.point(lambda x: int(x * opacity))
    img.putalpha(a)
    return img

def set_color(img: Image.Image, color: tuple):
    img = img.convert("RGBA")
    r, g, b, a = img.split()
    colored = Image.new("RGBA", img.size, (*color, 255))
    colored.putalpha(a)
    return colored

hex_to_rgb = lambda h: (int(h.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))

dummy = ImageDraw.Draw(Image.new("RGB",(1,1)))
def create_text(text,size,color="white",font="assets/font.ttf"):
    font = ImageFont.truetype(font, size)
    x,y,w,h = dummy.textbbox((0,0),text,font=font,font_size=size)
    
    img = Image.new("RGBA",(w+6,h+6))
    draw = ImageDraw.Draw(img)
    draw.text((3,3),text,font=font,fill=color,font_size=size,stroke_fill="black",stroke_width=2)
    
    return img

def scale_to_fit(img: Image.Image,max_size: int):
    ratio = min(max_size / img.width, max_size / img.height)
    return img.resize((int(img.width * ratio), int(img.height * ratio)), Image.LANCZOS)

def logger(name):
    print(f"\t{name}")
    
    return lambda a: print(f"\t\t{a}")