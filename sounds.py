import shutil

import utils
import os

def build():
    log = utils.logger("copying sounds")
    for i in os.walk("assets/sounds"):
        folder,_,files = i
        for v in files:
            shutil.copy(f"{folder}/{v}",f"build/{v}")