from mcpi.minecraft import Minecraft
mc = Minecraft.create('server_name')
import random
import time

def buildStairs():
    x, y, z, = -469, 69, 633
    yn = 0
    for zn in range(z, z+ 50):
        for xn in range(x, x+3):
            mc.setBlock(xn, y+yn, zn, 7)
        yn += 1

x0 = -1
y0 = 188
z0 = 1325

rr = 5
rir = rr - 1
rings = []

start_time = 0
finish_time = 0

def build_ring(x, y, z):
    mc.setBlocks(x+rr, y+rr, z, x-rr, y-rr, z+5, 41)
    mc.setBlocks(x+rir, y+rir, z, x-rir, y-rir, z+5, 0)
    rings.append([x, y, z])

def build_course():
    for zl in range(z0, z0+200):
        if (zl % 20 == 0):
            rand_x = random.randint(x0, x0+20)
            rand_y = random.randint(y0, y0+20)
            build_ring(rand_x, rand_y,  zl)

build_course()

c = mc.getPlayerEntityId('TCC_05')
r  = mc.getPlayerEntityId('TCCMinecraft009')

print(rings)
c_count = 0
r_count = 0

running = True
while running:
    cp = mc.entity.getPos(c)
    rp = mc.entity.getPos(r)

    for ring in rings:
        if (cp.z >= ring[2]):
            rings.pop(0)
            if (cp.x < ring[0]+rr and cp.x > ring[0]-rr):
                if (cp.y < ring[1]+rr and cp.y > ring[1]-rr):
                    mc.postToChat("passed through the ring")
                    c_count += 1
                    mc.postToChat("C score: " + str(c_count))

        if (rp.z >= ring[2]):
            if (rp.x < ring[0]+rr and rp.x > ring[0]-rr and rp.y < ring[1]+rr and rp.y > ring[1]-rr):
                r_count += 1
                mc.postToChat("R score: " + str(r_count))

    time.sleep(0.25)
