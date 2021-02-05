import canvas
import random
import time
# ******** Variable *********
WIDTH_WIN, HEIGHT_WIN = 350, 350
GAME_STATE = [None, None, None, None, None, None, None, None, None]
COUNT_WIN, COUNT_LOST = 0, 0
X_POS, Y_POS, WIDTH = 20, 20, 310 # координаты и ширина игрового поля, пришлось оглобалить
MODE = 'menu' # Режим, в котором игра находится ('menu' или 'game')
MENU_WIDTH = 200 # ширина окна меню
# Список элементов меню, заполняется параметками при старте. Название пункта, x, y, width, height - 
# - нужны для отрисовки кнопок и проверки нажатия в функции click
# Добавляя в этот список пункт меню, он автоматически добавится в меню.
MENU = [
    ['START GAME', 0, 0, 0, 0],
    ['RECORD', 0, 0, 0, 0],
    ['EXIT', 0, 0, 0, 0]
    ]
initMenu = False  # Флаг инициализации меню
# ******** Function *********

# Функция с адаптивным дизайном
# x_pos, y_pos - координаты верхнего левого угла игрового поля
# width - ширина поля равная высоте (квадрат)
# размер крестика и нолика расчитывается в процентном соотношении
# от ширины поля, 10 процентов от ширины - width * 0.1

# Функция рисования кнопки
def button(caption, x, y, width, height):
    canvas.fill_style('Black')
    canvas.fill_rect(x, y, width+2, height+2) # Тень
    canvas.fill_style('PaleTurquoise')
    canvas.fill_rect(x, y, width, height)
    canvas.fill_style('Black')
    canvas.fill_text(caption, x + width/2 + 1, y + width//7 + 1, 'Tahoma', width//9, 'center') # Тень
    canvas.fill_style('DarkGreen')
    canvas.fill_text(caption, x + width/2, y + width//7, 'Tahoma', width//9, 'center')

# Функция инициализации и рисования меню    
def draw_menu(x, y, width):
    canvas.clear()
    global MENU
    global initMenu
    height = width
    if initMenu:
        canvas.fill_style('Black')
        canvas.fill_rect(x, y, width+2, height+2)
        canvas.fill_style('Grey')
        canvas.fill_rect(x, y, width, height)
        for el in MENU:
            button(el[0], el[1], el[2], el[3], el[4])
    else:
        initMenu = True
        count = len(MENU)
        for i in range(count):
            MENU[i][1] = x + (width - width*0.8)/2
            MENU[i][2] = y + (i+1) * height/(count+1) - width*0.8*0.2/2
            MENU[i][3] = width*0.8
            MENU[i][4] = width*0.8*0.2

def message(caption, x, y, width):
    canvas.clear()
    height = width*0.2
    canvas.fill_style('Black')
    canvas.fill_rect(x, y-height/2, width+2, height+2)
    canvas.fill_style('Grey')
    canvas.fill_rect(x, y-height/2, width, height)
    if caption == 'YOU WIN':
        color1 = 'DarkBlue'
        color2 = 'DeepSkyBlue'
    elif caption == 'YOU LOST':
        color1 = 'DarkRed'
        color2 = 'Red'
    else:
        color1 = 'Black'
        color2 = 'Green'
    canvas.fill_style(color1)
    canvas.fill_text(caption, x + width//2 + 2, y + height*0.3 + 2, 'Tahoma', width//6, 'center')
    canvas.fill_style(color2)
    canvas.fill_text(caption, x + width//2, y + height*0.3, 'Tahoma', width//6, 'center')

# Функция рисования игрового поля
def draw_state(statusList: list, x_pos=50, y_pos=50, width=250):
    canvas.clear()
    height = width # высота поля равно ширине
    widKl = width//3 # ширина клетки
    x = widKl//2 + x_pos # начальные координата середины клетки
    y = x
    index = 0 # индекс списка
    # отрисовка линий
    canvas.line_width(2)
    canvas.set_color('Grey')
    for n in [1,2]:
        canvas.move_to(n*widKl+x_pos, 0 + y_pos)
        canvas.line_to(n*widKl+x_pos, height+y_pos)
        canvas.move_to(0 + x_pos, n*widKl + y_pos)
        canvas.line_to(width + x_pos, n*widKl + y_pos)

    canvas.line_width(5)
    for i in range(3):
        for j in range(3):
            el = statusList[index]
            index += 1
            # расчет координат середины текущей клетки
            _x = x + widKl*j
            _y = y + widKl*i
            if el is not None:
                if el == 'o':
                    canvas.set_color('Green')
                    canvas.circle(_x, _y, width * 0.1)
                if el == 'x':
                    canvas.set_color('Blue')
                    wNol = width * 0.1
                    canvas.move_to(_x-wNol, _y+wNol)
                    canvas.line_to(_x+wNol, _y-wNol)
                    canvas.move_to(_x-wNol, _y-wNol)
                    canvas.line_to(_x+wNol, _y+wNol)

# ------------------------------------------    
def get_bot_move(statusGame: list):
    index = []
    ret = None
    for i, el in enumerate(statusGame):
        if el is None:
            index.append(i)
    if index: 
        return random.choice(index)
    else:
        return None
# ------------------------------------------
def get_winner(statusGame:list):
    x_win = ['x', 'x', 'x']
    o_win = ['o', 'o', 'o']
    for j, i in enumerate(range(0, 7, 3)):
        # Проверяем горизонтальные и вертикальные линии
        if statusGame[i: i+3] == x_win or [statusGame[j], statusGame[j+3], statusGame[j+6]] == x_win:
            return 'x_win'
        if statusGame[i: i+3] == o_win or [statusGame[j], statusGame[j+3], statusGame[j+6]] == o_win:
            return 'o_win'
    # Проверяем диагонали
    if [statusGame[0], statusGame[4], statusGame[8]] == x_win or [statusGame[2], statusGame[4], statusGame[6]] == x_win:
        return 'x_win'
    if [statusGame[0], statusGame[4], statusGame[8]] == o_win or [statusGame[2], statusGame[4], statusGame[6]] == o_win:
        return 'o_win'
    # Если все клетки заняты
    if all(statusGame):
        return 'draw'
    # Если не один из вариантов не сработал, возвращаем None
    return None

# ------------------------------------------

def newGameInit(statusGame: list):
    draw_state(GAME_STATE, X_POS, Y_POS, WIDTH)
    for index in range(len(statusGame)):
        statusGame[index] = None
    time.sleep(3)
    canvas.clear()
    draw_state(GAME_STATE, X_POS, Y_POS, WIDTH)

# ------------------------------------------
def click(x, y):
    global MENU
    global MODE
    global COUNT_WIN
    global COUNT_LOST
    if MODE == 'menu':
        for el in MENU:
            if el[1] + el[3] > x > el[1] and el[2] + el[4] > y > el[2]:
                if el[0] == 'START GAME':
                    MODE = 'game'
                    newGameInit(GAME_STATE)
                elif el[0] == 'EXIT':
                    MODE = 'exit'
                elif el[0] == 'RECORD':
                    message(f'WIN: {COUNT_WIN}', (WIDTH_WIN - 200)/2, HEIGHT_WIN//2, 200)
                    MODE = 'message'
                    return
    elif MODE == 'game':
        widKl = WIDTH//3
        index = 0
        for i in range(3):
            for j in range(3):
                if widKl*j + widKl > x-X_POS > widKl*j and widKl*i + widKl > y-Y_POS > widKl*i:
                    if GAME_STATE[index] is None:
                        GAME_STATE[index] = 'x'
                        win = get_winner(GAME_STATE)
                        if win == 'x_win':
                            COUNT_WIN += 1
                            draw_state(GAME_STATE, X_POS, Y_POS, WIDTH)
                            canvas.draw()
                            time.sleep(1)
                            message('YOU WIN', (WIDTH_WIN - 200)/2, HEIGHT_WIN//2, 200)
                            MODE = 'message'
                            return
                        elif win == 'draw':
                            message('DRAW', (WIDTH_WIN - 200)/2, HEIGHT_WIN//2, 200)
                            MODE = 'message'
                            return
                        tmp = get_bot_move(GAME_STATE)          
                        if tmp is not None:
                            GAME_STATE[tmp] = 'o'
                            tmp = get_winner(GAME_STATE)
                            if tmp == 'o_win':
                                COUNT_LOST += 1
                                draw_state(GAME_STATE, X_POS, Y_POS, WIDTH)
                                canvas.draw()
                                time.sleep(1)
                                message('YOU LOST', (WIDTH_WIN - 200)/2, HEIGHT_WIN//2, 200)
                                MODE = 'message'
                                return
                            elif tmp == 'draw':
                                message('DRAW', (WIDTH_WIN - 200)/2, HEIGHT_WIN//2, 200)
                                MODE = 'message'
                                return
                index += 1

# ******** General programm *********

canvas.set_onclick(click)
while MODE is not 'exit':
    if MODE == 'menu':
        draw_menu((WIDTH_WIN - MENU_WIDTH)/2, (HEIGHT_WIN - MENU_WIDTH)/2, MENU_WIDTH)
        canvas.draw()
    elif MODE == 'game':
        draw_state(GAME_STATE, X_POS, Y_POS, WIDTH)
        canvas.draw()
    elif MODE == 'message':
        canvas.draw()
        time.sleep(3)
        MODE = 'menu'