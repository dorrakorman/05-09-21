# 05-09-21a = int(input('enter 1st number'))
b = int(input('enter 2st number'))
c = int(input('enter 3st number'))
if a >= b:
    if a >= c:
        print(a, 'is biggest')
    else:
        print(c, 'is biggest')
else:
    if b >= c:
        print(b, 'is biggest')
    else:
        print(c, 'is biggest')


a = int(input('enter a number'))
if a < 0:
    print('your number is negative')
else:
    print('your number is positive')

a = int(input('enter number is divided by 10'))
if a % 5:
     print('your number is divided by 5')
else:
    print('your number is divided by 2')











