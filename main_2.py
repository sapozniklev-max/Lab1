def uzor():
    CSI = '\x1b['
    RESET = f'{CSI}0m'
    COLOR = f'{CSI}41m'
    height = 9
    width = 17
    
    for y in range(height):
        for x in range(width):
            if (x + y) % 8 == 0 or (x - y) % 8 == 0:
                print(f"{COLOR}  {RESET}", end="")
            else:
                print("  ", end="")
        if y == 0: print(' Фигура С')
        else: print() 

if __name__ == '__main__':
    uzor()