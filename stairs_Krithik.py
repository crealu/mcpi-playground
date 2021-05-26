from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z

bottomStep = 0
topStep = 256
stepWidth = x + 3
melonBlock = 103
stone = 1
mc.setBlock(x, y, z, melonBlock)

for s in range(bottomStep, topStep):
  for sw in range(x, stepWidth):
    mc.setBlock(sw, y+s, z+s, melonBlock)
