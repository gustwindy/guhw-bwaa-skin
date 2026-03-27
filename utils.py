from PIL import Image

def save_2x(img: Image.Image,path: str):
    img.save(path.replace(".","@2x."))
    w,h = img.size
    img.resize((w//2,h//2)).save(path)
    print("\t\t\t+",path)

def save_anim(img: Image.Image,path: str,frames: int):
    for i in range(frames):
        save_2x(img,path.replace(".",f"-{i}."))

def set_opacity(img: Image.Image,opacity: float):
    img = img.convert("RGBA")
    r, g, b, a = img.split()
    a = a.point(lambda x: int(x * opacity))
    img.putalpha(a)
    return img


def logger(name):
    print(f"\t{name}")
    
    return lambda a: print(f"\t\t{a}")