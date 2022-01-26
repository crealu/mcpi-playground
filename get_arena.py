from mcpi.minecraft import Minecraft
mc = Minecraft.create('server_name')

import random
import time

f = open('got_arena.txt', 'w+')

arena_x = -214
arena_y =  139
arena_z =  677

whole_arena = []

f.write('my_arena = [ \n')

whole_arena = [
    [x1, x2,

def get_arena():
    for x in range(arena_x, arena_x+20):
        for y in range(arena_y, arena_y+10):
            for z in range(arena_z, arena_z+20):
                block = mc.getBlock(x, y, z)
                f.write(str(block) + ',\n')
        f.write('\n')
    print('got')

get_arena()
f.close()
