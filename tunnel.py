from mcpi.minecraft import Minecraft
mc = Minecraft.create('server_name')

def buildTunnel(x, y, z, endOfTunnel):
    airBlock = 0
    stoneBlock = 1
    tnt = 46
    tunnelStart = 0
    tunnelEnd = endOfTunnel

    for tw in range(tunnelStart, tunnelEnd):
        mc.setBlocks(x, y, z + tw, x + 4, y + 4, z + tw, stoneBlock)
        mc.setBlocks(x + 1, y + 1, z + tw, x + 3, y + 3, z + tw, airBlock)
        mc.setBlock(x + 3, y + 1, z + tw, tnt)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

buildTunnel(x, y, z, 200)
