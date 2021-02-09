import canvas
import time
import random
circles = []
for i in range (5):
    x = random.randint(20,330)
    y = random.randint(20,330)
    dx = random.choice([-6,5])
    dy = random.choice([-6,5])
    catalog = {'x': x,'y': y,'dx': dx,'dy': dy}
    circles.append(catalog)
while True:
    canvas.clear()
    for k in circles:
            k['x'] +=  k['dx']
            if k['x'] > 330 or k['x'] < 20:
                k['dx'] = - k['dx']
            k['y'] += k['dy']
            if k['y'] > 330 or k['y'] < 20:
                k['dy'] = - k['dy']
            canvas.circle(k['x'],k['y'],20)
            canvas.draw()
    time.sleep(0.01)