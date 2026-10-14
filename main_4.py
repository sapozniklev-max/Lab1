CSI = '\x1b['
RESET = f'{CSI}0m'
COLOR = f'{CSI}46m'

si = open('sequence.txt')
s = list(map(float, si.readlines()))

sum_ch = 0
sum_nch = 0
for i in range(len(s)):
    if i % 2 == 0: sum_ch += abs(s[i])
    else: sum_nch += abs(s[i])

total = sum_ch + sum_nch
procent_ch, procent_nch = round((sum_ch/total)*100), round((sum_nch/total)*100)

print(f"сумма чисел на четных позициях {procent_ch}% от общей суммы")
print(f"сумма чисел на нечетных позициях {procent_nch}% от общей суммы\n")

print('    ДИАГРАММА СУММ \n')

height = 10
for level_10_procent in range(height,0,-1):
    level_10_procent *= 10
    field_ch, field_nch = '   ', '   '
    if procent_ch >= level_10_procent: field_ch = f"{COLOR}    {RESET}"
    if procent_nch >= level_10_procent: field_nch = f"{COLOR}    {RESET}"
    if level_10_procent !=100: print(f"{CSI}43;1m {level_10_procent}%{RESET}|  {field_ch} {field_nch}")
    else: print(f"{CSI}43;1m{level_10_procent}%{RESET}|  {field_ch} {field_nch}")
print(f" 0%+----------------")
print("      Чет.  Нечет.")



