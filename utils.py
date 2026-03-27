from PIL import Image

def save_2x(img: Image,path: str):
    img.save(path.replace(".","@2x."))
    w,h = img.size
    img.resize((w//2,h//2)).save(path)