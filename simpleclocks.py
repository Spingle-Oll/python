import canvas
import datetime
while True:
    data = datetime.datetime.now()
    data_str = data.strftime('%H:%M:%S')
    canvas.stroke_rect(70, 105, 200, 100)
    canvas.fill_text(data_str,170,160, font = 'Monospace', 
    size = 25, align="center")
    canvas.draw()
    canvas.clear()