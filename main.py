import shutil
import os

shutil.rmtree("build",True)
os.mkdir("build")
shutil.copy("assets/skin.ini","build/skin.ini")

shutil.rmtree("dist",True)
os.mkdir("dist")
os.system("zip -r \"dist/z~◊《 Gale 》~《 guhw's skin 》~ ◊~z.osz\" build/")