from time import sleep
import os

def anim_1(h,w):
    s = []
    for x in range(w):
        for y in range(h):
            if (x + y) / 8 == 2.0 or (x - y) == 0:
                print(f"{COLOR}  {RESET}")
            else:
                print("  ")
            if x != 0:
                print(end = f"{CSI}{x*2}C")
        print(end = f"{CSI}1;{(x+1)*2+1}H")
        sleep(0.1)

        
def anim_2(h,w):
    s = []
    for x in range(w):
        for y in range(h):
            if (x + y) == 8 or (x - y) == 8:
                print(f"{COLOR}  {RESET}")
            else:
                print()
            if x != 0:
                print(end = f"{CSI}{x*2}C")
        print(end = f"{CSI}1;{(x+1)*2+1}H")
        sleep(0.1)


def uzor_animated():
    height = 9
    width = 17
    os.system("cls")
    anim_1(height,width)
    anim_2(height,width)

CSI = '\x1b['
RESET = f'{CSI}0m'
COLOR = f'{CSI}41m'


if __name__ == '__main__':
    uzor_animated()