print('#정수형')
a = 123
print(a)
a = -123
print(a)
a = 0
print(a,'\n')

print('\n#실수형')
a = 1.2
print(a)
a = -3.45
print(a)
a = 4.24E10
print('a = 4.24E10,', a)
a = 4.24e-10
print('a = 4.24e-10,', a, '\n')

print('\n8진수와 16진수')
a = 0o177
print('a = 0o177,', a)
a = 0x8ff
print('a = 0x8ff,', a)
b = 0xABC
print('b = 0xABC,',b)

print('\n#연산')
a = 3
b = 4
print('"a = 3, b = 4"')
print('사칙연산')
print('a + b =', a + b)
print('a - b = ', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a ** b =', a**b)
a = 7
b = 3
print('"a = 7, b = 3"')
print('a %% b =', a % b)
print('a / b = ', a / b, 'a // b =', a // b)