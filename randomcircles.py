import time
import canvas
import random

colors = ("Blue","Red","Fuchsia","Green","Purple","Black")

while True:
    x = random.randint(0, 350)
    y = random.randint(0, 350)

    for r in range(150, 185, 5):
        randomColors = random.choice(colors)

        canvas.circle(x,y, r)
        canvas.set_color(randomColors)

        canvas.draw()
        time.sleep(0.05)
        