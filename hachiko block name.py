from mcpi.minecraft import Minecraft
mc = Minecraft.create('server_name_here')

x, y, z = 75, 125, 65

h = [
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1]
]

a = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1]
]

c = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 1]
]

i = [
    [1, 1, 1, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
]

k = [
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1]
]

o = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]

hachiko = [h, a, c, h, i, k, o]

lo = 0
for letter in hachiko:
    yo = 0
    for arr in letter:
        xo = 0
        for num in arr:
            mc.setBlock(x + lo + xo, y + yo, z, 0)
            xo += 1
        yo -= 1
    lo += 5
