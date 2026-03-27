import shutil
import os
import judgement
import mods
import move_over

print("-- clearing old version")
shutil.rmtree("build",True)
os.mkdir("build")
shutil.copy("assets/skin.ini","build/skin.ini")

print("-- building skin")

mods.build()
move_over.build()
judgement.build()

print("-- preparing for distribution")
shutil.rmtree("dist",True)
os.mkdir("dist")

print("-- .osz")
os.system("zip -r \"dist/z~◊《 Bwaa 》~《 guhw's skin 》~ ◊~z.osz\" build/")

print("-- done! dist/*.osz & build/")