import datetime
import time
try:
    m_t = input('time H:M\n')
    my_d = datetime.datetime.strptime(m_t,'%H:%M')
    my_d = my_d.time()
    print('Пользователь был заблокирован до: {}'.format(my_d))
    while True:
        now = datetime.datetime.now()
        now = now.time()
        if now > my_d:
            print('Пользователь разбанен')
            break

except:
    print("Ошибка формата, обратитесь к администратору!")