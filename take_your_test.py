x1 = str(input ('question 1: '))
y1 = str(input ('answer 1: '))
x2 = str(input ('question 2: '))
y2 = str(input ('answer 2: '))
x3 = str(input ('question 3: '))
y3 = str(input ('answer 3: '))
x4 = str(input ('question 4: '))
y4 = str(input ('answer 4: '))
x5 = str(input ('question 5: '))
y5 = str(input ('answer 5: '))
x6 = str(input ('question 6: '))
y6 = str(input ('answer 6: '))
x7 = str(input ('question 7: '))
y7 = str(input ('answer 7: '))
x8 = str(input ('question 8: '))
y8 = str(input ('answer 8: '))
x9 = str(input ('question 9: '))
y9 = str(input ('answer 9: '))
x10 = str(input ('question 10: '))
y10 = str(input ('answer 10: '))

r = 10

S = str(input('s for start: '))

print('test 0-10')

name = str (input('name: '))

print('1.', x1, '\n')
z1 = str(input())
if (z1 == y1):
    r = r
else:
    r = r - 1

print('2.', x2,'\n')
z2 = str(input())
if (z2 == y2):
    r = r

else:
    r = r - 1
print('3.', x3,' \n')
z3 = str(input())
if (z3 == y3):
    r = r

else:
    r = r - 1

print('4', x4,' \n')
z4 = str(input())
if (z4 == y4):
    r = r
else:
    r = r - 1

print('5.', x5,' \n')
z5 = str(input())
if (z5 == y5):
    r = r
else:
    r = r - 1

print('6.', x6,' \n')
z6 = str(input())
if (z6 == y6):
    r = r
else:
    r = r - 1

print('7.', x7,' \n')
z7 = str(input())
if (z7 == y7):
    r = r
else:
    r = r - 1

print('8.', x8,' \n')
z8 = str(input())
if (z8 == y8):
    r = r
else:
    r = r - 1

print('9.', x9,' \n')
z9 = str(input())
if (z9 == y9):
    r = r
else:
    r = r - 1

print('10.', x10,' \n')
z10 = str(input())
if (z10 == y10):
    r = r
else:
    r = r - 1

print(name,"'s", 'note: ', r)
conti = input("press any key ")
