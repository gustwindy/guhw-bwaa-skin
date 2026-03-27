import shutil
import os
import gameplay
import judgement
import mods
import move_over
import rankings
import sounds
import text

print("-- clearing old version")
shutil.rmtree("build",True)
os.mkdir("build")
shutil.copy("assets/skin.ini","build/skin.ini")

print("-- building skin")

judgement.build()
move_over.build()
rankings.build()
gameplay.build()
sounds.build()
mods.build()
text.build()

print("-- preparing for distribution")
shutil.rmtree("dist",True)
os.mkdir("dist")

print("-- .osz")
#os.system("zip -r \"dist/z~◊《 bwaa 》~《 guhw's skin 》~ ◊~z.osz\" build/")
os.system("zip -rj \"dist/zzz._.bwaa._.guhw_skin._.zzz.osz\" build/*") # i guess we gotta do this now

print("-- done! dist/*.osz & build/")