x = ''

while len(x) < 5:
    y = input('Ввод данных: ')
    if y == '0':
        continue
    if y == '1':
        break

    x += y

else:
    print(x)

print('Программа работает дальше')