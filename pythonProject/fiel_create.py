try:
    fp = open('field.txt', 'r')
    fp.read()
except FileNotFoundError:
    print('系统正在维护...')
