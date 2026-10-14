import os
from time import sleep

def tap_cursor(x,y):
    print(f"{CSI}{x};{y}H", end='',flush=True)

def func():
    os.system('cls')
    print(' '*22 + 'y = 2x')

    max_y, max_x = 8, 4 #макс поммодулю значения графика функции
    os_x, os_y = 10, 20  #координаты начала оси координат

    for i in range(-max_y, max_y+1): # ось Y
        y = os_x-i
        tap_cursor(y, os_y)
        if i != 0:
            print("|", end='')
            if i % 2 == 0:
                print(f"{CSI}3D{i}")
    tap_cursor(os_x-max_y-1, os_y)
    print("^ Y")

    tap_cursor(os_x, os_y-(max_x*3)) # ось X
    print("-" * (3*max_x) + "+" + "-" * (3*max_x) + ">" + "X")
    for i in range(-max_x,max_x+1):
        if i == 0: continue
        x = os_y+(i*3)
        if i < 0:
            tap_cursor(os_x+1, x-1)
            print(i)
        else:
            tap_cursor(os_x+1, x)
            print(i)

    sleep(2)
    for x in range(-max_x, max_x+1): # обозначаем функ.
        y = 2*x
        tap_cursor(os_x-y, os_y+(x*3))
        print("*", end='', flush=True)
        sleep(0.4)


    tap_cursor(20,20)
        


CSI = '\x1b['
RESET = f'{CSI}0m'
COLOR = f'{CSI}41m'

if __name__ == "__main__":
    func()