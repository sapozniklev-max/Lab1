def flag():
    CSI = '\x1b['
    color = ['41','47','44']
    width = 20
    RESET = f'{CSI}49m'
    for i in range(3):
        for j in range(2):
            if i == 0 and j == 0:
                print(f"{CSI}{color[i]}m{' '*width}{RESET}   Нидерланды")
            else:
                print(f"{CSI}{color[i]}m{' '*width}{RESET}")
    

if __name__ == '__main__':
    flag()