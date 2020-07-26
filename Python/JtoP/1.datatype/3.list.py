print('#리스트란')
odd = [1, 3, 5, 7, 9]
a = []
b = ['Life', 'is', 'too', 'short']
c = [1, 2, 'Life', 'is']
d = [1, 2, ['Life', 'is']]
print('odd = [1, 3, 5, 7, 9]\toutput:', odd)
print('a = []\toutput:', a)
print("b = ['Life', 'is', 'too', 'short']\toutput:", b)
print("c = [1, 2, 'Life', 'is']\toutpput:", c)
print("d = [1, 2, ['Life', 'is']]\toutput:", d)

print('\n리스트 인덱싱')
a = [1, 2, 3]
print('''"a = [1, 2, 3]"
a[0]\toutput:''', a[0])
print('a[0] + a[2]\toutput:', a[0] + a[2])
print('a[-1]\toutput:', a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print("""
\"a = [1, 2, 3, ['a', 'b', 'c']]\"
a[0]\toutput:""", a[0])
print('a[-1]\toutput:', a[-1])
print('a[3]\toutput:', a[3])
print('a[-1][0]\toutput:',  a[-1][0])
print('a[-1][1]\toutput:',  a[-1][1])
print('a[-1][2]\toutput:',  a[-1][2])

a = [1, 2, ['a', 'b', ['Life', 'is']]]
print("""
a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[2][2][0]\toutput:""", a[2][2][0])
print('a[2][2][1]\toutput:', a[2][2][1])
print('a[2][0][0]\toutput:', a[2][0][0])
print('a[2][1][0]\toutput:', a[2][1][0])