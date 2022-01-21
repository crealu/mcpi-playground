from mcpi.minecraft import Minecraft
mc = Minecraft.create('mc2.tokyocodingclub.com')
import time

bgx = 134
bgy = 84
bgz = 63

#mc.setBlocks(bgx, bgy, bgz, bgx+30, bgy, bgz-10, 2)

flowers = {
    'orchid': [38, 1],
    'allium': [38, 2],
    'dandelion': [37],
    'poppy': [38]
}

zc = 0
for f in flowers:
    print(flowers[f])
    if len(flowers[f]) == 2:
        mc.setBlocks(bgx+1, bgy+1, bgz-5-zc, bgx+19, bgy+1, bgz-6-zc, 0)
    else:
        mc.setBlocks(bgx+1, bgy+1, bgz-5-zc, bgx+19, bgy+1, bgz-6-zc, 0)
    zc -= 2
    time.sleep(0.5)
    
#mc.setBlocks(bgx+1, bgy+1, bgz+1, bgx+29, bgy+1, bgz-5, 38, flowers['orchid'])
#mc.setBlocks(bgx+1, bgy+1, bgz-5, bgx+29, bgy+1, bgz-10, 38, flowers['allium'])

#me = mc.getPlayerEntityId('TCC_09')
#mc.entity.setPos(me, bgx, bgy, bgz)
