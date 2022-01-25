from mcpi.minecraft import Minecraft
mc = Minecraft.create('mc2.tokyocodingclub.com')
import time

x = 103
y = 64
z = 35

#mc.setBlocks(x, y, z, x+30, y+40, z+30,brick)
#mc.setBlocks(x+1, y+1, z+1, x+29, y+39, z+29, 0)

# brick block
brick = 45

# second floor
def secondFloor(yp):
    for xf in range(x+1, x+30):
        for zf in range(z+1, z+30):
            if xf % 3 == 0 and zf % 3 == 0:
                mc.setBlock(xf, y+yp, zf, 89)
            else:
                mc.setBlock(xf,y+yp, zf, 5)

#secondFloor(20)
#secondFloor(10)

# stair colors
purple = 203
red = 163
white = 156
tan = 135

sc = [purple, red, white, tan]

# make stairs
def buildStairs(xs, w, color):
    zs  = z + 27
    for ys in range(y+1, y+25):
        mc.setBlocks(x+xs, ys, zs, x+xs, ys, zs+w, color)
        xs+=1

# buildStairs(5, 2, sc[1])

cbx = 104
cby = 66
cbz = 53
pb = 0

changing = True

while changing:
    cb = mc.getBlock(cbx, cby, cbz)
    if cb != pb and cb != 0:
        buildStairs(5, 2, cb)
        pb = cb

    time.sleep(0.5)









































'''
changing = False
pb = 0
cbx, cby, cbz = 104, 66, 53
'''
'''
while changing:
    cb = mc.getBlock(cbx, cby, cbz)
    mc.postToChat(cb)
    if cb != pb and cb != 0:
        buildStairs(5, 2, cb)
        pb = cb
    time.sleep(0.5)

me = mc.getPlayerEntityId('TCC_02')
mc.entity.setPos(me, x, y, z)
'''








    


