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

print('\n#list slicing')
a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print('''
a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
output:''')
print('b:', b)
print('c:', c)

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print("\n\"a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]\"")
print("a[2:5]\toutput:", a[2:5])
print("a[3][:2]\toutput:", a[3][:2])

print('#\n리스트 연산')
a = [1, 2, 3]
b = [4, 5, 6]
a + b
print('''
"a = [1, 2, 3]"
"b = [4, 5, 6]"
a + b\toutput:''', a + b)
print('a * 3\toutput:', a * 3)
print('len(a)\toutput:', len(a))
print('str(a[2]) + "hi"\toutput:', str(a[2]) + "hi")

print('\n#리스트 수정 삭제')
a = [1, 2, 3, 4, 5]
a[2] = 9
print("""
\"a = [1, 2, 3, 4, 5]\"

a[2] = 9
print(a)\toutput:""", a)
a = [1, 2, 3, 4, 5]
del a[1]
print('''
del a[1]
print(a)\toutput:''', a)
a = [1, 2, 3, 4, 5]
del a[2:]
print('''del a[2:]
print(a)\toutput:''', a)

print('\n#리스트 관련 함수')
a = [1, 2, 3]
a.append(4)
print('''
"a = [1, 2, 3]"

a.append(4)
print(a)\toutput:''', a)
a.append([5,6])
print('''a.append([5,6])
print(a)\toutput:''', a)

a = [1, 4, 3, 2]
a.sort()
print('''
"a = [1, 4, 3, 2]"
a.sort()
print(a)\toutput:''', a)

a = ['a', 'c', 'b']
a.sort()
print("""
\"a = ['a', 'c', 'b']\"
a.sort()
print(a)\toutput:""", a)

a = ['c', 'b', 'a']
a.reverse()
print("""
\"a = ['c', 'b', 'a']\"
a.reverse()
print(a)\toutput:""", a)

a = [1, 2, 3]
a.index(3)
print('''
a = [1, 2, 3]
a.index(3)\toutput:''', a.index(3))
print('a.index(1)\toutput:', a.index(1))

a = [1, 2, 3]
a.insert(0, 4)
print('''
"a = [1, 2, 3]"
a.insert(0, 4)
print(a)\toutput:''', a)
a.insert(3, 5)
print('''a.insert(3, 5)
print(a)\toutput:''', a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print('''
"a = [1, 2, 3, 1, 2, 3]"
a.remove(3)
print(a)\toutput:''', a)
a.remove(3)
print('''a.remove(3)
print(a)\toutput''', a)

a = [1,2,3]
print('''
"a = [1,2,3]"
a.pop() \toutput:''', a.pop())
print('print(a)\toutput:',a)

a = [1,2,3]
print('''
"a = [1,2,3]"
a.pop(1)\toutput:''', a.pop(1))
print('print(a)\toutput:', a)

a = [1,2,3,1]
a.count(1)
print('''
"a = [1,2,3,1]"
a.count(1)\toutput:''', a.count(1))

a = [1,2,3]
a.extend([4,5])
print('''
"a = [1,2,3]"
a.extend([4,5])
print(a)\toutput:''', a)
b = [6, 7]
a.extend(b)
print('''"b = [6, 7]"
a.extend(b)
print(a)\toutput:''', a)