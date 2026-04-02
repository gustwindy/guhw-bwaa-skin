import shutil
import os
from parts import gameplay, judgement, mods, move_over, rankings, skin_ini, sounds, text

shutil.rmtree("dist",True)
os.mkdir("dist")

def build_variant(variant):
    print(" ! ---- making variant",variant)
    print("-- clearing old version")
    shutil.rmtree("build",True)
    os.mkdir("build")

    print("-- building skin")
    skin_ini.build(variant)
    judgement.build(variant)
    move_over.build()
    rankings.build()
    gameplay.build(variant)
    sounds.build()
    mods.build()
    text.build()

    print("-- preparing for distribution")

    print("-- .osz")
    #os.system("zip -r \"dist/z~◊《 bwaa 》~《 guhw's skin 》~ ◊~z.osk\" build/")
    os.system(f"zip -rj \"dist/zzz._.bwaa_{variant}._.guhw_skin._.zzz.osk\" build/*") # i guess we gotta do this now

    print(f"-- done with {variant}! dist/ & build/")


build_variant("performance")
build_variant("default")